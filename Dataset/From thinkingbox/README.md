# Thinkingbox 测试用例转换说明

## 📁 文件结构

```
From thinkingbox/
├── test_case/                          # 原始 thinkingbox 测试用例（Python 格式）
│   ├── banking.py                      # 银行场景（11 个测试）
│   ├── fno_testing_eval.py             # F&O 评估测试（102 个测试）
│   ├── fno_general_CRUD.py             # F&O CRUD 操作（95 个测试）
│   ├── fno_expense_agent.py            # F&O 费用代理（110 个测试）
│   ├── fno_general_CRU.py              # F&O CRU 操作（68 个测试）
│   └── ... 其他测试文件
├── convert_to_yaml.py                  # 转换脚本
├── thinkingbox_seval_converted.yaml    # 转换后的 YAML（398 个测试用例）
├── LLM_JUDGE_GUIDE.md                  # LLM Judge 评估指南
└── README.md                           # 本文档

参考文件：
../LMChecklist/lmc_mcp_server_evals.yaml  # YAML 格式参考
```

## 📊 统计信息

### 测试用例总数：**398**

### 按文件分布：
- `fno_expense_agent.py`: 110 个测试
- `fno_testing_eval.py`: 102 个测试
- `fno_general_CRUD.py`: 95 个测试
- `fno_general_CRU.py`: 68 个测试
- `banking.py`: 11 个测试
- `weather.py`: 5 个测试
- `cloud_drive.py`: 4 个测试
- `fno_expense_agent_hotel.py`: 1 个测试
- `banking_email.py`: 1 个测试
- `fno_testing_new_and_unvalidated.py`: 1 个测试

### 场景分类：
- **F&O (Dynamics 365 Finance & Operations)**: ~376 个测试
  - 客户管理 (CustTable)
  - 产品管理 (EcoResDistinctProduct)
  - 费用管理 (TrvExpenseLines)
  - 采购管理 (Purchase Requisitions)
  - 总账管理 (GL Accounts)

- **Retail Banking**: ~11 个测试
  - 账户转账
  - 余额查询
  - 账单支付

- **其他**: ~11 个测试
  - 天气查询
  - 云盘操作
  - 邮件管理

## 🎯 三个关键指标

### 1. Task Completion Rate（任务完成率）
- 评估系统是否成功完成用户请求的任务
- 关注任务执行的成功性和完整性

### 2. Groundedness（事实准确性）
- 评估响应是否基于实际检索的数据
- 防止幻觉和编造信息

### 3. Tool Accuracy（工具调用准确性）
- 评估系统是否调用了正确的工具
- 验证工具参数的正确性

## 🔄 转换流程

### 原始格式（Thinkingbox Python）
```python
def test_create_CustTableListPage(x: TestContext, judge: Judge, judgeAgent: JudgeAgent):
    """!
    query: |
        # Task
        Create a new customer record in the USMF company...

        # Data
        {
          "company": "USMF",
          "CustomerAccount": "DE-006",
          "Name": "Sample Test Customer"
        }
    """
    judgeAgent.validate(
        session_id=x.session_id,
        agent_response=x.response,
        validation_question="Was the customer created successfully?",
    )
```

### 转换后格式（SEVAL YAML）
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
```

## 🚀 使用方法

### 1. 生成 YAML 文件

```bash
cd "c:\github\Catalyst Eval\Dataset\From thinkingbox"
python convert_to_yaml.py
```

输出：`thinkingbox_seval_converted.yaml`

### 2. 查看 YAML 结构

```python
import yaml

with open('thinkingbox_seval_converted.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# 前 3 项是 metrics 定义
metrics = data[:3]

# 其余是测试查询
queries = data[3:]

print(f"Metrics: {len(metrics)}")
print(f"Queries: {len(queries)}")
```

### 3. 使用 LLM Judge 评估

参考 `LLM_JUDGE_GUIDE.md` 中的详细说明和代码示例。

## ⚠️ 关键差异：Thinkingbox vs SEVAL

| 特性 | Thinkingbox | SEVAL |
|------|------------|-------|
| **工具调用记录** | ✅ 记录所有工具调用和参数 | ❌ 不记录工具调用 |
| **效果验证** | ✅ 通过 `x.effects` 直接验证 | ❌ 只能通过响应文本判断 |
| **断言方式** | Python assert 语句 | YAML assertions + LLM Judge |
| **验证问题** | `judgeAgent.validate()` | `expected_behaviors` 字段 |

### 解决方案：LLM Judge

由于 SEVAL 不记录工具调用，我们使用 **LLM Judge** 的方式：

1. **通过响应文本推断工具调用**
   - 分析响应中的成功/失败模式
   - 识别数据检索/修改的证据

2. **使用验证问题（expected_behaviors）**
   - 从原始测试的 `validation_question` 提取
   - 作为 LLM Judge 的评估依据

3. **基于任务类型的启发式规则**
   - CREATE 任务 → 应该有创建确认
   - READ 任务 → 应该返回具体数据
   - UPDATE 任务 → 应该有更新确认
   - DELETE 任务 → 应该有删除确认

## 📝 YAML 格式详解

### Metrics 定义（前 3 项）
```yaml
- tag: groundedness          # 指标标签
  metric: true               # 标记为 metric
  assertions:                # 断言列表
  - text: "..."              # 断言描述
    level: critical          # 严重级别
```

### Query 条目（其余项）
```yaml
- query: "用户查询文本"
  tags:                      # 关联的指标
  - groundedness
  - task_completion
  - tool_accuracy
  metadata:                  # 元数据
    test_name: "测试函数名"
    scenario: "场景名称"
    source_file: "源文件名"
  expected_behaviors:        # 预期行为（验证问题）
  - "验证问题 1"
  - "验证问题 2"
  user_context: "用户上下文"  # 可选
```

## 🔍 数据质量检查

### 查询分布检查
```python
import yaml
from collections import Counter

with open('thinkingbox_seval_converted.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

queries = [d for d in data if 'query' in d and 'metric' not in d]

# 按源文件统计
files = Counter(q['metadata']['source_file'] for q in queries)
print("Test cases by file:")
for file, count in files.most_common():
    print(f"  {file}: {count}")

# 按场景统计
scenarios = Counter(q['metadata']['scenario'] for q in queries)
print("\nTest cases by scenario:")
for scenario, count in scenarios.items():
    print(f"  {scenario}: {count}")

# 检查是否有 expected_behaviors
with_behaviors = sum(1 for q in queries if 'expected_behaviors' in q)
print(f"\nQueries with expected_behaviors: {with_behaviors}/{len(queries)}")
```

## 🎓 下一步工作

### 1. 场景分类修正
当前所有测试的 scenario 都是 "unknown"，需要：
- 从模块级 docstring 正确提取 scenario
- 或基于文件名自动推断 scenario

### 2. 集成实际测试运行
- 使用 SEVAL 框架运行测试
- 收集系统响应
- 应用 LLM Judge 评估

### 3. 建立评估基准
- 人工评估部分测试用例
- 与 LLM Judge 结果对比
- 优化评估标准和提示词

### 4. 持续迭代
- 根据评估结果调整 assertions
- 添加更多场景和测试用例
- 优化 LLM Judge 的准确性

## 📚 参考资料

- **SEVAL 框架文档**：了解如何运行评估
- **LLM Judge 最佳实践**：提高评估一致性和准确性
- **Dynamics 365 F&O 文档**：理解业务场景和操作

## ❓ 常见问题

### Q1: 为什么 scenario 都是 "unknown"？
A: 当前转换脚本从模块 docstring 提取 scenario，但可能格式匹配有问题。可以手动修正或基于文件名推断。

### Q2: 如何处理没有 validation_question 的测试？
A: 这些测试只有 Python assert 语句。可以：
1. 手动添加 expected_behaviors
2. 基于 assert 语句自动生成验证问题
3. 仅依赖 general assertions 进行评估

### Q3: LLM Judge 的准确性如何？
A: 取决于：
1. 提示词的质量
2. 使用的模型（推荐 GPT-4 或更强）
3. 评估标准的清晰度
建议先用人工评估建立基准。

### Q4: 如何知道调用了哪些工具？
A: 在没有工具调用日志的情况下：
1. 分析响应文本的模式
2. 根据任务类型推断
3. 查找响应中的确认信息
4. 使用 expected_behaviors 作为辅助判断

---

**生成时间**: 2026-02-13
**转换脚本版本**: 1.0
**测试用例总数**: 398
