"""
Convert thinkingbox test cases to SEVAL YAML format

This script parses Python test files from thinkingbox and converts them
into a YAML format suitable for LLM evaluation with three key metrics:
- task_completion: Whether the task was completed successfully
- groundedness: Whether the response is grounded in actual data
- tool_accuracy: Whether the correct tools were called with correct parameters
"""

import ast
import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Any


def extract_docstring_field(docstring: str, field: str) -> str:
    """Extract a specific field from a docstring."""
    if not docstring:
        return ""

    # Match field: | followed by content (multiline)
    pattern = rf'{field}:\s*\|\s*((?:.*\n)*?)(?=\s*\w+:|$)'
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

    # Extract test functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
            docstring = ast.get_docstring(node)
            if not docstring or 'query:' not in docstring:
                continue

            # Extract query from docstring
            query = extract_docstring_field(docstring, 'query')
            user_context = extract_docstring_field(docstring, 'user_context')

            if query:
                test_case = {
                    'test_name': node.name,
                    'query': query,
                    'scenario': scenario,
                    'file': os.path.basename(filepath)
                }

                if user_context:
                    test_case['user_context'] = user_context

                # Extract validation questions from the function body
                validation_questions = []
                for stmt in ast.walk(node):
                    if isinstance(stmt, ast.Call):
                        # Look for judgeAgent.validate or judge.text_yesno calls
                        if hasattr(stmt.func, 'attr'):
                            if stmt.func.attr in ['validate', 'text_yesno']:
                                for keyword in stmt.keywords:
                                    if keyword.arg == 'validation_question':
                                        if isinstance(keyword.value, ast.Constant):
                                            validation_questions.append(keyword.value.value)
                                # For positional arguments in text_yesno
                                if stmt.func.attr == 'text_yesno' and len(stmt.args) >= 2:
                                    if isinstance(stmt.args[1], ast.Constant):
                                        validation_questions.append(stmt.args[1].value)

                if validation_questions:
                    test_case['validation_questions'] = validation_questions

                test_cases.append(test_case)

    return test_cases


def generate_yaml_output(test_cases: List[Dict[str, Any]]) -> str:
    """Generate YAML output with metrics and queries."""

    # Define the three metrics
    metrics = [
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

    # Build queries list
    queries = []
    for tc in test_cases:
        query_entry = {
            'query': tc['query'],
            'tags': ['groundedness', 'task_completion', 'tool_accuracy'],
            'metadata': {
                'test_name': tc['test_name'],
                'scenario': tc['scenario'],
                'source_file': tc['file']
            }
        }

        # Add validation questions as expected_behaviors
        if tc.get('validation_questions'):
            query_entry['expected_behaviors'] = tc['validation_questions']

        # Add user context if available
        if tc.get('user_context'):
            query_entry['user_context'] = tc['user_context']

        queries.append(query_entry)

    # Combine metrics and queries
    output = metrics + queries

    # Convert to YAML with custom formatting
    yaml_str = yaml.dump(output,
                         default_flow_style=False,
                         sort_keys=False,
                         allow_unicode=True,
                         width=120)

    return yaml_str


def main():
    # Directory containing test case files
    test_case_dir = Path(__file__).parent / "test_case"

    if not test_case_dir.exists():
        print(f"Error: Test case directory not found: {test_case_dir}")
        return

    # Collect all test cases
    all_test_cases = []
    test_files = sorted(test_case_dir.glob("*.py"))

    print(f"Found {len(test_files)} Python files")
    print("=" * 60)

    for filepath in test_files:
        if filepath.name.startswith('__'):
            continue

        print(f"Processing: {filepath.name}")
        test_cases = extract_test_cases_from_file(str(filepath))
        print(f"  Found {len(test_cases)} test cases")
        all_test_cases.extend(test_cases)

    print("=" * 60)
    print(f"Total test cases extracted: {len(all_test_cases)}")

    # Generate YAML output
    yaml_content = generate_yaml_output(all_test_cases)

    # Write to output file
    output_file = Path(__file__).parent / "thinkingbox_seval_converted.yaml"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(yaml_content)

    print(f"\nYAML file generated: {output_file}")
    print(f"File size: {len(yaml_content)} bytes")

    # Print summary statistics
    scenarios = {}
    for tc in all_test_cases:
        scenario = tc.get('scenario', 'unknown')
        scenarios[scenario] = scenarios.get(scenario, 0) + 1

    print("\nTest cases by scenario:")
    for scenario, count in sorted(scenarios.items()):
        print(f"  {scenario}: {count}")


if __name__ == '__main__':
    main()
