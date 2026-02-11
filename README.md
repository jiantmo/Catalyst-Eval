# Dynamics 365 F&O Catalyst Evaluation Dataset

这是一个用于评估 Dynamics 365 Finance & Operations (F&O) AI 助手的数据集，包含采购和财务记录两大业务流程的问答对。

## 📁 文件说明

### 原始数据
- **`OrigData/Catalyst_FnO.csv`** - 原始CSV格式数据集（275条记录）
  - 包含完整的元数据字段
  - 适合人工审阅和编辑

### 评估数据集
- **`Catalyst_FnO_Eval.json`** - 标准JSON格式（推荐用于评估）
  - 结构化的问答对
  - 易于程序化处理
  - 包含39个评估样本

- **`Catalyst_FnO_Eval_Dataset.md`** - 人类可读的Markdown格式
  - 详细的样本展示
  - 包含评估指标建议
  - 便于审阅和文档化

- **`Catalyst_FnO_Dataset.md`** - 完整的Markdown文档
  - 包含所有样本的详细说明
  - 业务流程分类
  - 数据特征分析

### 工具脚本
- **`convert_to_json.py`** - CSV到JSON转换脚本
  - 用于重新生成评估数据集
  - 自动统计样本分布

### 项目配置
- **`CLAUDE.md`** - Claude Code 项目指南
  - 数据结构说明
  - 业务领域知识
  - 数据质量考虑因素

## 📊 数据集统计

| 指标 | 数值 |
|------|------|
| 总样本数 | 39 |
| 采购流程样本 | 15 |
| 财务流程样本 | 24 |
| 操作类型 | Create, Read, Delete, Act, Query |
| 法人实体 | USMF |
| 时间范围 | 2026年1月 |

## 🔄 业务流程覆盖

### 1. 采购申请到收货 (Requisition to Receipt)
完整的采购生命周期：
- ✅ 创建采购申请
- ✅ 添加/修改行项目
- ✅ 提交审批
- ✅ 审批流程
- ✅ 创建采购订单
- ✅ 确认订单
- ✅ 过账产品收据
- ✅ 过账供应商发票
- ✅ 取消/撤回操作

### 2. 试算平衡 (Trial Balance)
财务记录和报告：
- ✅ 总账账户查询
- ✅ 凭证追踪
- ✅ 快照管理
- ✅ 未过账项目检查
- ✅ 期间对比分析
- ✅ 故障诊断
- ✅ 对账摘要

## 🚀 快速开始

### 使用JSON格式（推荐）

```python
import json

# 加载数据集
with open('Catalyst_FnO_Eval.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# 遍历样本
for sample in dataset['samples']:
    question = sample['question']
    expected_response = sample['expected_response']
    scenario = sample['scenario']

    # 运行你的评估逻辑
    # ...
```

### 使用Python进行评估

```python
def evaluate_response(question, generated_response, expected_response):
    """评估生成的响应"""
    metrics = {
        'accuracy': calculate_accuracy(generated_response, expected_response),
        'completeness': check_completeness(generated_response, expected_response),
        'format_consistency': check_format(generated_response)
    }
    return metrics

# 评估示例
with open('Catalyst_FnO_Eval.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

results = []
for sample in dataset['samples']:
    # 使用你的模型生成响应
    generated = your_model.generate(sample['question'])

    # 评估
    metrics = evaluate_response(
        sample['question'],
        generated,
        sample['expected_response']
    )

    results.append({
        'id': sample['id'],
        'scenario': sample['scenario'],
        'metrics': metrics
    })
```

## 📋 数据集结构

### JSON Schema

```json
{
  "name": "string",
  "description": "string",
  "version": "string",
  "samples": [
    {
      "id": "integer",
      "scenario": "string",
      "product_area": "string",
      "type": "string",
      "question": "string",
      "expected_response": "string",
      "conversation_pattern": "string | null"
    }
  ]
}
```

### 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | Integer | 样本唯一标识符 |
| `scenario` | String | 业务场景名称 |
| `product_area` | String | D365 F&O产品领域 |
| `type` | String | 操作类型（Create/Read/Delete/Act） |
| `question` | String | 用户问题 |
| `expected_response` | String | 期望的AI响应 |
| `conversation_pattern` | String/Null | 多轮对话模式描述 |

## 🎯 评估指标建议

### 1. 响应准确性（Accuracy）
- 是否正确识别操作类型
- 实体ID和属性是否正确
- 数值计算（金额、数量）是否准确

### 2. 响应完整性（Completeness）
- 是否包含所有必要字段
- 状态变化是否清晰
- 是否提供确认信息

### 3. 格式一致性（Format Consistency）
- 结构化信息格式统一
- 项目符号、状态标记使用
- 日期、金额格式一致

### 4. 多轮对话能力（Multi-turn Capability）
- 上下文维持（如采购申请ID）
- 依赖关系处理
- 下一步操作建议

### 5. 业务逻辑理解（Business Logic Understanding）
- 状态流转符合规则
- 前置条件识别
- 必填/可选字段判断

## 🔧 重新生成数据集

如果你修改了原始CSV文件，可以重新生成JSON格式：

```bash
python convert_to_json.py
```

## 📖 关键业务概念

### 采购模块
- **采购申请**: 6位数字ID (000081, 000082)
- **采购订单**: 8位数字ID (00000200, 00000205)
- **物料编码**: C0001, C0002, C0003, C0004
- **供应商**: US-111 (Contoso office supply)
- **产品收据**: PR-YYMMDD-XX 格式

### 财务模块
- **总账账户**: 4位数字 (1110, 1300, 6110)
- **凭证**: 6位数字ID (000123)
- **快照ID**: TB_YYYY_MM 格式
- **发票**: INV-XXXXX 格式

## 🔄 状态流转

### 采购申请状态
```
Draft → In Review → Approved → (Cancelled)
         ↓
       Draft (撤回)
```

### 采购订单状态
```
Open order → Confirmed → Received → Invoiced
```

## 📝 许可和使用

本数据集用于 Dynamics 365 F&O Catalyst AI 助手的评估和训练。

## 🤝 贡献

如果发现数据质量问题或希望添加新的样本：

1. 修改 `OrigData/Catalyst_FnO.csv`
2. 运行 `python convert_to_json.py` 重新生成
3. 验证生成的JSON格式
4. 提交更改

## 📞 联系方式

如有问题或建议，请通过项目issues反馈。
