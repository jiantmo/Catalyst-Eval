# 快速开始指南

## 🎯 目标

将 398 个 thinkingbox 测试用例转换为 SEVAL YAML 格式，并使用 LLM Judge 评估三个关键指标：
- **Task Completion Rate**（任务完成率）
- **Groundedness**（事实准确性）
- **Tool Accuracy**（工具调用准确性）

## 📦 生成的文件

```
From thinkingbox/
├── thinkingbox_seval_converted.yaml    # ✅ 转换后的 YAML（398 个测试用例）
├── convert_to_yaml.py                  # 🔧 转换脚本
├── evaluate_example.py                 # 🔧 示例评估脚本
├── LLM_JUDGE_GUIDE.md                  # 📖 LLM Judge 详细指南
├── README.md                           # 📖 完整说明文档
└── QUICKSTART.md                       # 📖 本快速指南
```

## ⚡ 快速使用

### 步骤 1: 查看转换后的 YAML

```bash
cd "c:\github\Catalyst Eval\Dataset\From thinkingbox"

# 查看 YAML 文件前 50 行
head -n 50 thinkingbox_seval_converted.yaml

# 或使用 Python 分析
python -c "
import yaml
data = yaml.safe_load(open('thinkingbox_seval_converted.yaml', 'r', encoding='utf-8'))
metrics = [d for d in data if d.get('metric')]
queries = [d for d in data if 'query' in d and 'metric' not in d]
print(f'Metrics: {len(metrics)}')
print(f'Queries: {len(queries)}')
print(f'\nFirst query:')
print(queries[0]['query'][:200] + '...')
"
```

### 步骤 2: 运行示例评估（使用模拟响应）

```bash
# 设置 API Key（选择一个）
export OPENAI_API_KEY='your-key-here'          # 使用 OpenAI
# 或
export ANTHROPIC_API_KEY='your-key-here'       # 使用 Anthropic Claude

# 运行评估（仅评估前 5 个测试用例作为示例）
python evaluate_example.py --limit 5

# 查看结果
cat evaluation_results.json | jq '.summary'
```

### 步骤 3: 查看评估结果

```python
import json

with open('evaluation_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 查看汇总
print("=== Summary ===")
print(json.dumps(data['summary'], indent=2))

# 查看第一个测试的详细结果
print("\n=== First Test Result ===")
print(json.dumps(data['results'][0], indent=2))
```

## 📊 YAML 格式示例

### Metrics 定义（文件开头）

```yaml
- tag: groundedness
  metric: true
  assertions:
  - text: response is based on actual ERP data retrieved from the system
    level: critical
  - text: all data points can be traced back to tool outputs
    level: critical

- tag: task_completion
  metric: true
  assertions:
  - text: the system successfully completes the requested action
    level: critical

- tag: tool_accuracy
  metric: true
  assertions:
  - text: the system calls the appropriate tools for the task
    level: critical
```

### Query 条目示例

```yaml
- query: |
    # Task
    Create a new customer record in the USMF company...

    # Data
    {
      "company": "USMF",
      "CustomerAccount": "DE-006",
      "Name": "Sample Test Customer"
    }
  tags:
  - groundedness
  - task_completion
  - tool_accuracy
  metadata:
    test_name: test_create_CustTableListPage
    scenario: fno
    source_file: fno_testing_eval.py
  expected_behaviors:
  - Was the customer created successfully?
  - Does the customer record contain all required fields?
```

## 🔧 自定义评估

### 修改 LLM Judge 提示词

编辑 `evaluate_example.py` 中的提示词模板：

```python
TASK_COMPLETION_TEMPLATE = """
Your custom evaluation prompt...
"""
```

### 使用真实系统响应

替换 `get_mock_response()` 函数：

```python
def get_real_response(query: str, test_name: str) -> str:
    """从实际系统获取响应"""
    # 调用你的 AI 系统
    response = your_ai_system.chat(query)
    return response
```

### 添加自定义评估逻辑

```python
def custom_evaluate(query, response, expected_behaviors):
    """自定义评估逻辑"""

    # 使用正则表达式检查特定模式
    import re
    if re.search(r'successfully created', response, re.I):
        task_completed = True
    else:
        task_completed = False

    # 检查是否包含特定数据点
    data_points = re.findall(r'\b\d+\b', response)
    is_grounded = len(data_points) > 0

    # 推断工具调用
    if 'create' in query.lower() and 'created' in response.lower():
        tool_correct = True
    else:
        tool_correct = False

    return {
        'task_completion': {'score': 100 if task_completed else 0},
        'groundedness': {'confidence': 100 if is_grounded else 0},
        'tool_accuracy': {'parameter_accuracy': 100 if tool_correct else 0}
    }
```

## 📈 理解评估结果

### 结果文件结构

```json
{
  "results": [
    {
      "query": "用户查询...",
      "response": "系统响应...",
      "test_name": "test_create_customer",
      "source_file": "fno_testing_eval.py",
      "evaluation": {
        "task_completion": {
          "task_completed": true,
          "reason": "Customer was successfully created",
          "score": 100
        },
        "groundedness": {
          "is_grounded": true,
          "confidence": 95,
          "evidence": ["DE-006", "Sample Test Customer"],
          "concerns": [],
          "reason": "All data points are specific"
        },
        "tool_accuracy": {
          "task_type": "CREATE",
          "expected_tools": ["create_customer"],
          "tool_usage_correct": true,
          "parameter_accuracy": 100,
          "redundancy_detected": false,
          "reason": "Correct create operation"
        }
      }
    }
  ],
  "errors": [],
  "summary": {
    "total_test_cases": 398,
    "task_completion_rate": 87.5,
    "groundedness_rate": 92.3,
    "tool_accuracy_rate": 89.1,
    "by_file": {
      "fno_testing_eval.py": {
        "count": 102,
        "task_completion_rate": 88.2,
        "groundedness_rate": 93.1,
        "tool_accuracy_rate": 90.4
      }
    }
  }
}
```

### 指标解读

#### Task Completion Rate (87.5%)
- **含义**：87.5% 的测试用例成功完成了任务
- **关注点**：失败的测试是否合理？是否缺少功能？

#### Groundedness Rate (92.3%)
- **含义**：92.3% 的响应基于实际数据
- **关注点**：7.7% 的响应可能包含幻觉或推测

#### Tool Accuracy Rate (89.1%)
- **含义**：89.1% 的测试调用了正确的工具
- **关注点**：10.9% 的测试可能调用了错误的工具或参数不正确

## 🚨 常见问题

### Q1: 模拟响应的评估不准确？
**A:** 模拟响应仅用于演示。使用真实系统响应才能得到有意义的评估结果。

### Q2: LLM Judge 评估结果不一致？
**A:**
- 使用 `temperature=0` 确保确定性
- 使用更强大的模型（GPT-4, Claude 3.5 Sonnet）
- 优化提示词，提供更清晰的评估标准

### Q3: 如何提高评估准确性？
**A:**
1. 使用人工评估的子集建立基准
2. 与 LLM Judge 结果对比
3. 迭代优化提示词
4. 添加更多示例和边界条件

### Q4: 如何处理 API 成本？
**A:**
- 先用少量测试验证（`--limit 10`）
- 使用更便宜的模型（如 GPT-3.5）进行初步筛选
- 只用强模型评估困难案例
- 考虑本地 LLM（如 Llama 3）

## 📚 下一步

### 1. 集成实际测试系统
```python
# 连接到你的 Catalyst AI 系统
from your_system import CatalystAI

catalyst = CatalystAI()

def get_real_response(query: str) -> str:
    return catalyst.chat(query)
```

### 2. 建立人工评估基准
- 随机选择 50-100 个测试用例
- 人工评估并标注
- 与 LLM Judge 结果对比
- 计算一致性（Cohen's Kappa）

### 3. 持续监控和改进
- 定期运行评估
- 跟踪指标变化趋势
- 识别常见失败模式
- 优化系统和评估标准

### 4. 扩展评估维度
考虑添加更多评估指标：
- **Response Quality**：响应质量和可读性
- **Latency**：响应时间
- **Error Handling**：错误处理能力
- **User Experience**：用户体验评分

## 🔗 相关文档

- **README.md**：完整的项目说明和背景
- **LLM_JUDGE_GUIDE.md**：详细的 LLM Judge 使用指南
- **convert_to_yaml.py**：转换脚本源码和注释
- **evaluate_example.py**：评估脚本源码和注释

## 💡 最佳实践

### ✅ DO
- 使用真实系统响应进行评估
- 从小规模开始（`--limit 10`）
- 保存所有评估结果用于分析
- 定期更新提示词和评估标准
- 建立人工评估基准

### ❌ DON'T
- 不要仅依赖模拟响应
- 不要忽略评估失败的案例
- 不要频繁更改评估标准（影响可比性）
- 不要过度优化单个指标
- 不要忽视边界案例和错误处理

---

**开始评估！** 🚀

```bash
# 快速测试（5 个案例）
python evaluate_example.py --limit 5

# 完整评估（398 个案例，需要时间和 API 费用）
python evaluate_example.py
```
