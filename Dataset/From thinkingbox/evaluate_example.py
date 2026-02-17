"""
示例评估脚本：使用 LLM Judge 评估测试用例

这个脚本展示了如何：
1. 加载 YAML 测试用例
2. 获取系统响应（模拟）
3. 使用 LLM Judge 评估三个指标
4. 生成评估报告

注意：需要设置 OPENAI_API_KEY 环境变量
"""

import yaml
import json
import os
from typing import Dict, List, Any
from collections import defaultdict


# ============================================================================
# LLM Judge 提示词模板
# ============================================================================

TASK_COMPLETION_TEMPLATE = """You are evaluating whether an AI assistant successfully completed a task.

**User Query:**
{query}

**Assistant Response:**
{response}

**Expected Behaviors:**
{validation_questions}

**Evaluation Criteria:**
1. Did the assistant complete the requested action?
2. If unable to complete, did it explain why clearly?
3. For multi-step tasks, were all steps executed in order?
4. Did the assistant provide confirmation with relevant IDs?

**Output a JSON object with:**
- "task_completed": true/false
- "reason": "brief explanation"
- "score": 0-100

Output only valid JSON, no other text."""


GROUNDEDNESS_TEMPLATE = """You are evaluating whether an AI assistant's response is grounded in actual data.

**User Query:**
{query}

**Assistant Response:**
{response}

**Expected Behaviors:**
{validation_questions}

**Evaluation Criteria:**
1. Does the response contain specific data points (numbers, dates, IDs)?
2. Does the response avoid vague or generic statements?
3. If data is unavailable, does it explicitly state this?
4. Are there any signs of hallucination or speculation?

**Red Flags for Hallucination:**
- Invented IDs, numbers, or dates
- Phrases like "probably", "might be", "typically"
- Providing data without evidence of retrieval
- Contradictions with expected behaviors

**Output a JSON object with:**
- "is_grounded": true/false
- "confidence": 0-100
- "evidence": ["list of specific data points"]
- "concerns": ["list of red flags"]
- "reason": "brief explanation"

Output only valid JSON, no other text."""


TOOL_ACCURACY_TEMPLATE = """You are evaluating whether an AI assistant called the right tools with correct parameters.

**User Query:**
{query}

**Assistant Response:**
{response}

**Expected Behaviors:**
{validation_questions}

**Task Type Analysis:**
First, identify the task type from the query:
- CREATE: "create", "add", "new"
- READ: "find", "show", "get", "what is", "check"
- UPDATE: "update", "change", "modify", "edit"
- DELETE: "delete", "remove"
- WORKFLOW: "submit", "approve", "recall", "cancel"

**Evaluation Criteria:**
1. Based on the task type, what tools should be called?
2. Are the tool parameters correct based on user input?
3. Does the response indicate appropriate tool usage?
4. Are there signs of redundant or unnecessary calls?

**Output a JSON object with:**
- "task_type": "CREATE|READ|UPDATE|DELETE|WORKFLOW"
- "expected_tools": ["list of expected tool types"]
- "tool_usage_correct": true/false
- "parameter_accuracy": 0-100
- "redundancy_detected": true/false
- "reason": "brief explanation"

Output only valid JSON, no other text."""


# ============================================================================
# LLM Judge 实现（支持多种 LLM 提供商）
# ============================================================================

def llm_judge_openai(prompt: str, model: str = "gpt-4o") -> dict:
    """使用 OpenAI API 作为 LLM Judge"""
    try:
        import openai

        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert evaluator for AI assistant responses. Provide objective and accurate assessments. Output valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,  # 确保一致性
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return {"error": str(e)}


def llm_judge_anthropic(prompt: str, model: str = "claude-3-5-sonnet-20241022") -> dict:
    """使用 Anthropic Claude API 作为 LLM Judge"""
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        message = client.messages.create(
            model=model,
            max_tokens=1024,
            temperature=0.0,
            system="You are an expert evaluator for AI assistant responses. Provide objective and accurate assessments. Output valid JSON only.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract JSON from response
        response_text = message.content[0].text
        # Find JSON in the response
        import re
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
        else:
            return {"error": "No JSON found in response"}
    except Exception as e:
        print(f"Error calling Anthropic API: {e}")
        return {"error": str(e)}


def llm_judge(prompt: str, provider: str = "openai") -> dict:
    """统一的 LLM Judge 接口"""
    if provider == "openai":
        return llm_judge_openai(prompt)
    elif provider == "anthropic":
        return llm_judge_anthropic(prompt)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


# ============================================================================
# 评估函数
# ============================================================================

def evaluate_response(query: str, response: str, expected_behaviors: List[str], provider: str = "openai") -> Dict[str, Any]:
    """使用 LLM Judge 评估三个指标"""

    validation_text = "\n".join(f"- {b}" for b in expected_behaviors) if expected_behaviors else "No specific validation questions provided."

    # 1. Task Completion
    print("  Evaluating task completion...")
    task_completion_result = llm_judge(
        TASK_COMPLETION_TEMPLATE.format(
            query=query,
            response=response,
            validation_questions=validation_text
        ),
        provider=provider
    )

    # 2. Groundedness
    print("  Evaluating groundedness...")
    groundedness_result = llm_judge(
        GROUNDEDNESS_TEMPLATE.format(
            query=query,
            response=response,
            validation_questions=validation_text
        ),
        provider=provider
    )

    # 3. Tool Accuracy
    print("  Evaluating tool accuracy...")
    tool_accuracy_result = llm_judge(
        TOOL_ACCURACY_TEMPLATE.format(
            query=query,
            response=response,
            validation_questions=validation_text
        ),
        provider=provider
    )

    return {
        'task_completion': task_completion_result,
        'groundedness': groundedness_result,
        'tool_accuracy': tool_accuracy_result
    }


# ============================================================================
# 模拟响应生成（仅用于演示）
# ============================================================================

def get_mock_response(query: str, test_name: str) -> str:
    """生成模拟响应（实际使用时应该从系统获取真实响应）"""

    # 简单的模拟逻辑
    if "create" in query.lower():
        return f"Successfully created the record as requested. All required fields have been populated correctly."
    elif "find" in query.lower() or "get" in query.lower() or "show" in query.lower():
        return f"I found the requested information. Here are the details: [Account: US-001, Credit Limit: $500,000.0, Status: Active]"
    elif "update" in query.lower():
        return f"Successfully updated the record with the new values provided."
    elif "delete" in query.lower():
        return f"The record has been successfully deleted from the system."
    else:
        return f"I've completed your request. The operation was successful."


# ============================================================================
# 批量评估
# ============================================================================

def batch_evaluate(yaml_file: str, output_file: str = "evaluation_results.json", provider: str = "openai", limit: int = None):
    """批量评估所有测试用例"""

    # 加载 YAML
    print(f"Loading test cases from: {yaml_file}")
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 分离 metrics 和 queries
    queries = [d for d in data if 'query' in d and 'metric' not in d]

    if limit:
        queries = queries[:limit]
        print(f"Limiting evaluation to first {limit} test cases")

    print(f"Found {len(queries)} test cases to evaluate")
    print(f"Using LLM provider: {provider}")
    print("=" * 60)

    results = []
    errors = []

    for i, query_entry in enumerate(queries):
        test_name = query_entry['metadata']['test_name']
        print(f"\n[{i+1}/{len(queries)}] Processing: {test_name}")

        try:
            # 获取响应（这里使用模拟，实际应该从系统获取）
            response = get_mock_response(query_entry['query'], test_name)
            print(f"  Response: {response[:100]}...")

            # 评估
            evaluation = evaluate_response(
                query=query_entry['query'],
                response=response,
                expected_behaviors=query_entry.get('expected_behaviors', []),
                provider=provider
            )

            results.append({
                'query': query_entry['query'],
                'response': response,
                'test_name': test_name,
                'source_file': query_entry['metadata']['source_file'],
                'evaluation': evaluation
            })

            # 显示评估结果摘要
            tc_score = evaluation['task_completion'].get('score', 0)
            gr_score = evaluation['groundedness'].get('confidence', 0)
            ta_score = evaluation['tool_accuracy'].get('parameter_accuracy', 0)
            print(f"  ✓ Task Completion: {tc_score}/100")
            print(f"  ✓ Groundedness: {gr_score}/100")
            print(f"  ✓ Tool Accuracy: {ta_score}/100")

        except Exception as e:
            print(f"  ✗ Error: {e}")
            errors.append({
                'test_name': test_name,
                'error': str(e)
            })

    print("\n" + "=" * 60)
    print("Evaluation completed!")
    print(f"Successfully evaluated: {len(results)}/{len(queries)}")
    if errors:
        print(f"Errors: {len(errors)}")

    # 保存结果
    output_data = {
        'results': results,
        'errors': errors,
        'summary': aggregate_results(results)
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")

    # 打印汇总
    print("\n" + "=" * 60)
    print("=== Evaluation Summary ===")
    summary = output_data['summary']
    print(f"Task Completion Rate: {summary['task_completion_rate']:.2f}%")
    print(f"Groundedness Rate: {summary['groundedness_rate']:.2f}%")
    print(f"Tool Accuracy Rate: {summary['tool_accuracy_rate']:.2f}%")

    return output_data


def aggregate_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """计算汇总统计"""

    if not results:
        return {
            'task_completion_rate': 0.0,
            'groundedness_rate': 0.0,
            'tool_accuracy_rate': 0.0,
            'by_file': {}
        }

    # 总体指标
    task_scores = [r['evaluation']['task_completion'].get('score', 0) for r in results]
    ground_scores = [r['evaluation']['groundedness'].get('confidence', 0) for r in results]
    tool_scores = [r['evaluation']['tool_accuracy'].get('parameter_accuracy', 0) for r in results]

    # 按文件分组
    by_file = defaultdict(lambda: {'count': 0, 'task_scores': [], 'ground_scores': [], 'tool_scores': []})
    for r in results:
        file = r['source_file']
        by_file[file]['count'] += 1
        by_file[file]['task_scores'].append(r['evaluation']['task_completion'].get('score', 0))
        by_file[file]['ground_scores'].append(r['evaluation']['groundedness'].get('confidence', 0))
        by_file[file]['tool_scores'].append(r['evaluation']['tool_accuracy'].get('parameter_accuracy', 0))

    # 计算每个文件的平均分
    by_file_summary = {}
    for file, data in by_file.items():
        by_file_summary[file] = {
            'count': data['count'],
            'task_completion_rate': sum(data['task_scores']) / len(data['task_scores']),
            'groundedness_rate': sum(data['ground_scores']) / len(data['ground_scores']),
            'tool_accuracy_rate': sum(data['tool_scores']) / len(data['tool_scores'])
        }

    return {
        'total_test_cases': len(results),
        'task_completion_rate': sum(task_scores) / len(task_scores),
        'groundedness_rate': sum(ground_scores) / len(ground_scores),
        'tool_accuracy_rate': sum(tool_scores) / len(tool_scores),
        'by_file': by_file_summary
    }


# ============================================================================
# 主函数
# ============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Evaluate test cases using LLM Judge')
    parser.add_argument('--yaml', default='thinkingbox_seval_converted.yaml', help='Path to YAML test cases file')
    parser.add_argument('--output', default='evaluation_results.json', help='Output file for results')
    parser.add_argument('--provider', choices=['openai', 'anthropic'], default='openai', help='LLM provider to use')
    parser.add_argument('--limit', type=int, help='Limit number of test cases to evaluate (for testing)')

    args = parser.parse_args()

    # 检查 API key
    if args.provider == 'openai' and not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-api-key'")
        return

    if args.provider == 'anthropic' and not os.getenv('ANTHROPIC_API_KEY'):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set it with: export ANTHROPIC_API_KEY='your-api-key'")
        return

    # 运行评估
    batch_evaluate(
        yaml_file=args.yaml,
        output_file=args.output,
        provider=args.provider,
        limit=args.limit
    )


if __name__ == '__main__':
    main()
