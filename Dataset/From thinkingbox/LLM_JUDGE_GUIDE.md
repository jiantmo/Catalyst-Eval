# LLM Judge 评估指南

## 概述

本文档说明如何使用 LLM Judge 对 thinkingbox 测试用例进行评估。由于 SEVAL 框架不记录工具调用列表（而 thinkingbox 会记录），我们需要通过 LLM Judge 的方式，基于对话内容和响应描述来判断三个关键指标。

## 三个核心指标

### 1. **Task Completion Rate（任务完成率）**

#### 定义
评估系统是否成功完成用户请求的任务。

#### 评估标准
- ✅ **成功完成**：系统执行了请求的操作（创建、读取、更新、删除或工作流操作）
- ✅ **合理失败**：无法完成时，清楚解释原因和缺少的前提条件
- ✅ **多步骤任务**：所有必要步骤按正确顺序执行
- ✅ **确认反馈**：提供完成确认和相关标识符（如订单号、凭证号）

#### LLM Judge 提示词模板

```
You are evaluating whether an AI assistant successfully completed a task.

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

**Output Format:**
{
  "task_completed": true/false,
  "reason": "brief explanation",
  "score": 0-100
}
```

### 2. **Groundedness（事实准确性）**

#### 定义
评估响应是否基于实际检索的数据，而非虚构或推测的信息。

#### 评估标准
- ✅ **数据来源**：响应基于实际 ERP 系统检索的数据
- ✅ **可追溯性**：所有数据点（数字、日期、ID、状态）可以追溯到工具输出
- ✅ **明确未知**：数据不可用时明确说明，而非编造合理的信息
- ✅ **无推测**：不包含超出工具返回数据的推测或推断

#### LLM Judge 提示词模板

```
You are evaluating whether an AI assistant's response is grounded in actual data.

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

**Output Format:**
{
  "is_grounded": true/false,
  "confidence": 0-100,
  "evidence": ["specific data points mentioned"],
  "concerns": ["any red flags found"],
  "reason": "brief explanation"
}
```

### 3. **Tool Accuracy（工具调用准确性）**

#### 定义
评估系统是否调用了正确的工具，使用了正确的参数。

#### 评估标准
- ✅ **工具选择**：为任务调用了适当的工具（如创建任务使用创建工具，而非读取工具）
- ✅ **参数正确**：工具参数根据用户输入正确填充（法人实体、ID、数量、日期等）
- ✅ **无冗余调用**：没有进行冗余或不必要的工具调用
- ✅ **依赖顺序**：多个工具按逻辑依赖顺序调用

#### LLM Judge 提示词模板

```
You are evaluating whether an AI assistant called the right tools with correct parameters.

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
   - CREATE tasks → should use create/insert tools
   - READ tasks → should use read/query/get tools
   - UPDATE tasks → should use update/patch tools
   - DELETE tasks → should use delete tools
   - WORKFLOW → should use workflow action tools

2. Are the tool parameters correct based on user input?
   - Legal entity (company): {extract from query}
   - IDs/Numbers: {extract from query}
   - Quantities/Amounts: {extract from query}
   - Dates: {extract from query}

3. Does the response indicate appropriate tool usage?
   - Success message patterns
   - Data retrieval patterns
   - Error handling patterns

4. Are there signs of redundant or unnecessary calls?
   - Multiple reads of the same data
   - Unnecessary validation calls

**Output Format:**
{
  "task_type": "CREATE|READ|UPDATE|DELETE|WORKFLOW",
  "expected_tools": ["list of expected tool types"],
  "tool_usage_correct": true/false,
  "parameter_accuracy": 0-100,
  "redundancy_detected": true/false,
  "reason": "brief explanation"
}
```

## 综合评估流程

### Step 1: 预处理查询
```python
def preprocess_query(query, metadata):
    """提取查询中的关键信息"""
    return {
        'task_type': extract_task_type(query),
        'entities': extract_entities(query),  # company, IDs, amounts, dates
        'operation': extract_operation(query),
        'context': metadata
    }
```

### Step 2: 执行三个指标的评估
```python
def evaluate_response(query, response, expected_behaviors):
    """使用 LLM Judge 评估三个指标"""

    # 1. Task Completion
    task_completion_result = llm_judge(
        prompt=task_completion_template.format(
            query=query,
            response=response,
            validation_questions=expected_behaviors
        )
    )

    # 2. Groundedness
    groundedness_result = llm_judge(
        prompt=groundedness_template.format(
            query=query,
            response=response,
            validation_questions=expected_behaviors
        )
    )

    # 3. Tool Accuracy
    tool_accuracy_result = llm_judge(
        prompt=tool_accuracy_template.format(
            query=query,
            response=response,
            validation_questions=expected_behaviors
        )
    )

    return {
        'task_completion': task_completion_result,
        'groundedness': groundedness_result,
        'tool_accuracy': tool_accuracy_result
    }
```

### Step 3: 聚合结果
```python
def aggregate_results(all_evaluations):
    """计算整体指标"""
    return {
        'task_completion_rate': sum(e['task_completion']['score'] for e in all_evaluations) / len(all_evaluations),
        'groundedness_rate': sum(e['groundedness']['confidence'] for e in all_evaluations) / len(all_evaluations),
        'tool_accuracy_rate': sum(e['tool_accuracy']['parameter_accuracy'] for e in all_evaluations) / len(all_evaluations)
    }
```

## 实现示例

### 使用 OpenAI API 实现 LLM Judge

```python
import openai
import json

def llm_judge(prompt: str, model: str = "gpt-4") -> dict:
    """使用 OpenAI API 作为 LLM Judge"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert evaluator for AI assistant responses. Provide objective and accurate assessments."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,  # 确保一致性
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)
```

### 批量评估脚本

```python
import yaml

def batch_evaluate(yaml_file: str):
    """批量评估所有测试用例"""

    # 加载 YAML
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 分离 metrics 和 queries
    metrics = [d for d in data if d.get('metric')]
    queries = [d for d in data if 'query' in d and 'metric' not in d]

    print(f"Evaluating {len(queries)} test cases...")

    results = []
    for i, query_entry in enumerate(queries):
        print(f"Processing {i+1}/{len(queries)}: {query_entry['metadata']['test_name']}")

        # 这里需要实际的响应数据
        # response = get_response_from_system(query_entry['query'])
        response = "Mock response for testing"  # 替换为实际响应

        evaluation = evaluate_response(
            query=query_entry['query'],
            response=response,
            expected_behaviors=query_entry.get('expected_behaviors', [])
        )

        results.append({
            'query': query_entry['query'],
            'test_name': query_entry['metadata']['test_name'],
            'evaluation': evaluation
        })

    # 保存结果
    with open('evaluation_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # 计算汇总统计
    summary = aggregate_results(results)
    print("\n=== Evaluation Summary ===")
    print(f"Task Completion Rate: {summary['task_completion_rate']:.2f}%")
    print(f"Groundedness Rate: {summary['groundedness_rate']:.2f}%")
    print(f"Tool Accuracy Rate: {summary['tool_accuracy_rate']:.2f}%")

    return results, summary
```

## 关键挑战与解决方案

### 挑战 1: 没有工具调用日志
**问题**：SEVAL 不记录实际的工具调用，只有响应文本

**解决方案**：
1. 通过响应文本的模式识别推断工具调用
2. 查找关键指标：
   - 创建成功："created", "added", "new record"
   - 读取成功：具体的数据值
   - 更新成功："updated", "changed"
   - 删除成功："deleted", "removed"

### 挑战 2: 参数准确性验证
**问题**：无法直接验证传递给工具的参数

**解决方案**：
1. 在响应中查找用户提供的参数
2. 验证响应是否确认了正确的参数值
3. 使用 `expected_behaviors` 中的验证问题

### 挑战 3: LLM Judge 的一致性
**问题**：LLM 评估可能不一致

**解决方案**：
1. 使用 `temperature=0` 确保确定性
2. 提供详细的评估标准和示例
3. 多次评估取平均值（可选）
4. 使用更强大的模型（如 GPT-4）作为 Judge

## 输出格式

### 单个测试用例评估结果
```json
{
  "test_name": "test_create_CustTableListPage",
  "query": "Create a new customer record...",
  "source_file": "fno_testing_eval.py",
  "evaluation": {
    "task_completion": {
      "task_completed": true,
      "reason": "Customer DE-006 was successfully created",
      "score": 100
    },
    "groundedness": {
      "is_grounded": true,
      "confidence": 95,
      "evidence": ["Customer DE-006", "Sample Test Customer", "USMF"],
      "concerns": [],
      "reason": "All data points match expected values"
    },
    "tool_accuracy": {
      "task_type": "CREATE",
      "expected_tools": ["create_customer", "CustomersV3"],
      "tool_usage_correct": true,
      "parameter_accuracy": 100,
      "redundancy_detected": false,
      "reason": "Correct create operation with all required parameters"
    }
  }
}
```

### 汇总报告
```json
{
  "summary": {
    "total_test_cases": 398,
    "task_completion_rate": 85.5,
    "groundedness_rate": 92.3,
    "tool_accuracy_rate": 88.7
  },
  "by_scenario": {
    "fno": {
      "count": 376,
      "task_completion_rate": 86.2,
      "groundedness_rate": 93.1,
      "tool_accuracy_rate": 89.4
    },
    "retail_banking": {
      "count": 11,
      "task_completion_rate": 90.9,
      "groundedness_rate": 95.0,
      "tool_accuracy_rate": 87.3
    }
  },
  "by_operation_type": {
    "CREATE": {"count": 150, "avg_score": 87.5},
    "READ": {"count": 120, "avg_score": 91.2},
    "UPDATE": {"count": 80, "avg_score": 85.3},
    "DELETE": {"count": 48, "avg_score": 88.9}
  }
}
```

## 下一步

1. **集成实际响应数据**：需要运行测试用例获取系统的实际响应
2. **优化 LLM Judge 提示词**：根据实际评估结果调整提示词
3. **建立基准**：使用人工评估的子集建立准确性基准
4. **持续改进**：根据评估结果迭代优化提示词和评估标准
