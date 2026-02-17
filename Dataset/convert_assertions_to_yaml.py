"""
Convert thinkingbox test cases to standard YAML format with LLM Judge assertions

This script parses Python test files and converts assert statements into
natural language assertions that LLM Judge can evaluate.

Output format:
- query: "user query"
  tags:
  - groundedness
  - task_completion
  - tool_accuracy
  assertions:
  - text: "natural language assertion"
    level: critical
"""

import ast
import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional


class AssertionExtractor(ast.NodeVisitor):
    """Extract assertions from test function AST"""

    def __init__(self):
        self.assertions = []
        self.validation_questions = []

    def visit_Assert(self, node):
        """Visit assert statements"""
        # Try to extract meaningful assertion text
        assertion_text = self._extract_assertion_text(node)
        if assertion_text:
            self.assertions.append(assertion_text)
        self.generic_visit(node)

    def visit_Call(self, node):
        """Visit function calls to find judge.text_yesno and judgeAgent.validate"""
        try:
            # Check for judge.text_yesno(x.response, "question")
            if (hasattr(node.func, 'attr') and
                node.func.attr in ['text_yesno', 'validate']):

                # Extract validation_question from keyword args
                for keyword in node.keywords:
                    if keyword.arg == 'validation_question':
                        if isinstance(keyword.value, ast.Constant):
                            self.validation_questions.append(keyword.value.value)

                # Extract question from positional args in text_yesno
                if node.func.attr == 'text_yesno' and len(node.args) >= 2:
                    if isinstance(node.args[1], ast.Constant):
                        self.validation_questions.append(node.args[1].value)
        except:
            pass

        self.generic_visit(node)

    def _extract_assertion_text(self, node: ast.Assert) -> Optional[str]:
        """Convert assert statement to natural language"""
        try:
            test = node.test

            # Handle: assert judge.text_yesno(...) - already handled in visit_Call
            if isinstance(test, ast.Call):
                return None

            # Handle: assert x.effects["service"]["key"] == {...}
            if isinstance(test, ast.Compare):
                left = test.left
                ops = test.ops
                comparators = test.comparators

                # Check if it's comparing to a dict
                if (len(comparators) > 0 and
                    isinstance(comparators[0], ast.Dict) and
                    isinstance(left, ast.Subscript)):

                    dict_value = comparators[0]
                    assertion = self._extract_effect_assertion(left, dict_value, ops[0])
                    return assertion

                # Check for items() comparison: assert dict.items() >= {...}.items()
                if (isinstance(left, ast.Call) and
                    hasattr(left.func, 'attr') and
                    left.func.attr == 'items'):

                    # Get the dict being compared
                    base = left.func.value
                    if isinstance(comparators[0], ast.Call):
                        comp_dict = comparators[0].func.value
                        if isinstance(comp_dict, ast.Dict):
                            assertion = self._extract_items_comparison(base, comp_dict)
                            return assertion

            # Handle: assert "key" in x.effects["service"]
            if isinstance(test, ast.Compare) and isinstance(test.ops[0], ast.In):
                return None  # Skip "in" checks as they're usually setup

            # Handle: assert x.effects["service"].get("key", [])
            if isinstance(test, ast.Call):
                return None  # Skip get() checks

        except Exception as e:
            # If parsing fails, skip this assertion
            pass

        return None

    def _extract_effect_assertion(self, subscript: ast.Subscript,
                                  expected: ast.Dict,
                                  op: ast.cmpop) -> str:
        """Extract assertion from effect comparison"""
        try:
            # Parse the effect path: x.effects["service"]["accounts"]["123"]
            path_parts = []
            current = subscript

            while isinstance(current, ast.Subscript):
                if isinstance(current.slice, ast.Constant):
                    path_parts.insert(0, current.slice.value)
                current = current.value

            # Extract expected values from dict
            expected_values = {}
            for key, value in zip(expected.keys, expected.values):
                if isinstance(key, ast.Constant) and isinstance(value, ast.Constant):
                    expected_values[key.value] = value.value

            # Generate natural language assertion
            if "account" in str(path_parts).lower():
                # Account balance assertion
                account_num = path_parts[-1] if path_parts else "unknown"
                balance = expected_values.get('balance', 'unknown')
                account_type = expected_values.get('account_type', 'account')
                return f"The {account_type} account {account_num} should have a balance of ${balance}"

            # Generic assertion
            service = path_parts[0] if len(path_parts) > 0 else "system"
            return f"The {service} should have the expected state: {expected_values}"

        except:
            return "The system state should match the expected values"

    def _extract_items_comparison(self, base: ast.Subscript,
                                  expected: ast.Dict) -> str:
        """Extract assertion from items() comparison"""
        try:
            # Parse expected values
            expected_values = {}
            for key, value in zip(expected.keys, expected.values):
                if isinstance(key, ast.Constant) and isinstance(value, ast.Constant):
                    expected_values[key.value] = value.value

            # Generate natural language based on transaction type
            if expected_values.get('transaction_type') == 'transfer':
                from_acct = expected_values.get('from_account', 'unknown')
                to_acct = expected_values.get('to_account', 'unknown')
                amount = expected_values.get('amount', 'unknown')
                return f"The system should execute a transfer of ${amount} from account {from_acct} to account {to_acct}"

            # Bill payment
            if 'payee_account' in expected_values:
                amount = expected_values.get('amount', 'unknown')
                payee = expected_values.get('payee_account', 'unknown')
                return f"The system should schedule a bill payment of ${amount} to {payee}"

            # Generic
            return f"The system should execute the operation with parameters: {expected_values}"

        except:
            return "The system should execute the requested operation with correct parameters"


def extract_docstring_field(docstring: str, field: str) -> str:
    """Extract a specific field from a docstring."""
    if not docstring:
        return ""

    # Match field: | followed by content (multiline)
    pattern = rf'{field}:\s*\|?\s*((?:.*\n)*?)(?=\s*\w+:|$)'
    match = re.search(pattern, docstring, re.MULTILINE)
    if match:
        content = match.group(1).strip()
        # Remove leading whitespace from each line
        lines = content.split('\n')
        return '\n'.join(line.strip() for line in lines)
    return ""


def extract_test_cases_from_file(filepath: str) -> List[Dict[str, Any]]:
    """Extract all test cases from a Python test file."""
    test_cases = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return []

    # Extract scenario from module docstring
    scenario = "unknown"
    if ast.get_docstring(tree):
        module_doc = ast.get_docstring(tree)
        scenario_match = re.search(r'scenario:\s*(\w+)', module_doc)
        if scenario_match:
            scenario = scenario_match.group(1)

    # Map scenario names to friendly names
    scenario_map = {
        'retail_banking': 'Retail Banking',
        'fno': 'F&O Operations',
        'unknown': 'General'
    }
    scenario = scenario_map.get(scenario, scenario)

    # Extract test functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
            docstring = ast.get_docstring(node)
            if not docstring or 'query:' not in docstring:
                continue

            # Extract query from docstring
            query = extract_docstring_field(docstring, 'query')
            if not query:
                continue

            # Extract assertions from function body
            extractor = AssertionExtractor()
            for stmt in node.body:
                extractor.visit(stmt)

            # Combine all assertions
            all_assertions = []

            # Add effect assertions (converted to natural language)
            for assertion in extractor.assertions:
                all_assertions.append({
                    'text': assertion,
                    'level': 'critical'
                })

            # Add validation questions
            for question in extractor.validation_questions:
                all_assertions.append({
                    'text': question,
                    'level': 'critical'
                })

            # If no assertions found, add a generic one
            if not all_assertions:
                all_assertions.append({
                    'text': 'The system should complete the requested task successfully',
                    'level': 'critical'
                })

            test_case = {
                'query': query,
                'tags': ['groundedness', 'task_completion', 'tool_accuracy'],
                'assertions': all_assertions,
                'metadata': {
                    'test_name': node.name,
                    'scenario': scenario,
                    'source_file': os.path.basename(filepath)
                }
            }

            test_cases.append(test_case)

    return test_cases


def generate_metrics_definitions() -> List[Dict[str, Any]]:
    """Generate the three metrics definitions"""
    return [
        {
            'tag': 'groundedness',
            'metric': True,
            'assertions': [
                {
                    'text': 'response is based on actual ERP data retrieved from the system rather than hallucinated or assumed information',
                    'level': 'critical'
                },
                {
                    'text': 'all data points (numbers, dates, IDs, statuses) in the response can be traced back to tool outputs',
                    'level': 'critical'
                },
                {
                    'text': 'when data is unavailable or cannot be retrieved, the system explicitly states this rather than making up plausible-sounding information',
                    'level': 'critical'
                },
                {
                    'text': 'response does not include speculative or inferred information beyond what the tools returned',
                    'level': 'critical'
                }
            ]
        },
        {
            'tag': 'task_completion',
            'metric': True,
            'assertions': [
                {
                    'text': 'the system successfully completes the requested action (create, read, update, delete, or workflow action) when feasible',
                    'level': 'critical'
                },
                {
                    'text': 'if the task cannot be completed, the system clearly explains why and what prerequisites or permissions are missing',
                    'level': 'critical'
                },
                {
                    'text': 'for multi-step tasks, all necessary steps are executed in the correct sequence',
                    'level': 'critical'
                },
                {
                    'text': 'the system provides confirmation of successful task completion with relevant identifiers',
                    'level': 'critical'
                }
            ]
        },
        {
            'tag': 'tool_accuracy',
            'metric': True,
            'assertions': [
                {
                    'text': 'the system calls the appropriate tools for the task (e.g., using create tools for creation tasks, not read tools)',
                    'level': 'critical'
                },
                {
                    'text': 'tool parameters are correctly populated based on user input (legal entity, IDs, quantities, dates, etc.)',
                    'level': 'critical'
                },
                {
                    'text': 'the system does not make redundant or unnecessary tool calls',
                    'level': 'critical'
                },
                {
                    'text': 'when multiple tools are needed, they are called in a logical dependency order',
                    'level': 'critical'
                }
            ]
        }
    ]


def main():
    # Source directory
    test_case_dir = Path(__file__).parent / "From thinkingbox" / "test_case"

    if not test_case_dir.exists():
        print(f"Error: Test case directory not found: {test_case_dir}")
        return

    # Collect all test cases
    all_test_cases = []
    test_files = sorted(test_case_dir.glob("*.py"))

    print("=" * 70)
    print("Converting thinkingbox test cases to YAML format")
    print("=" * 70)
    print(f"\nFound {len(test_files)} Python files")

    for filepath in test_files:
        if filepath.name.startswith('__'):
            continue

        print(f"\nProcessing: {filepath.name}")
        test_cases = extract_test_cases_from_file(str(filepath))
        print(f"  Extracted {len(test_cases)} test cases")

        # Show sample assertions for first test
        if test_cases and len(test_cases) > 0:
            sample = test_cases[0]
            print(f"  Sample: {sample['metadata']['test_name']}")
            print(f"    Query: {sample['query'][:80]}...")
            print(f"    Assertions: {len(sample['assertions'])}")
            for i, assertion in enumerate(sample['assertions'][:2], 1):
                print(f"      {i}. {assertion['text'][:70]}...")

        all_test_cases.extend(test_cases)

    print("\n" + "=" * 70)
    print(f"Total test cases extracted: {len(all_test_cases)}")

    # Generate metrics + test cases
    metrics = generate_metrics_definitions()
    output_data = metrics + all_test_cases

    # Write to YAML file
    output_file = Path(__file__).parent / "thinkingbox_converted_with_assertions.yaml"

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(output_data,
                 f,
                 default_flow_style=False,
                 sort_keys=False,
                 allow_unicode=True,
                 width=120)

    print(f"\n✅ YAML file generated: {output_file}")
    print(f"   File contains: {len(metrics)} metrics + {len(all_test_cases)} queries")

    # Statistics
    scenarios = {}
    total_assertions = 0
    for tc in all_test_cases:
        scenario = tc['metadata']['scenario']
        scenarios[scenario] = scenarios.get(scenario, 0) + 1
        total_assertions += len(tc['assertions'])

    print(f"\n📊 Statistics:")
    print(f"   Total queries: {len(all_test_cases)}")
    print(f"   Total assertions: {total_assertions}")
    print(f"   Avg assertions per query: {total_assertions / len(all_test_cases):.1f}")

    print(f"\n   By scenario:")
    for scenario, count in sorted(scenarios.items()):
        print(f"      {scenario}: {count} queries")


if __name__ == '__main__':
    main()
