# FnO AI Agent: Skill Graph Architecture

---

# Part 1 — The Execution Gap

## 1.1 Observed Eval Results

Multiple evaluation runs against the FnO Declarative Agent (DA) using the SEVAL framework have produced consistently poor results:

| Eval job | Queries | Control pass rate | Treatment pass rate |
|----------|---------|-------------------|---------------------|
| 200TrialBalance-FnODA_Accuracy_Only_20260303 | 206 | **11/206 (5.3%)** | **2/206 (1.0%)** |

The pattern is not limited to Trial Balance. Across all eval tracks, the DA struggles whenever a query requires more than a trivial single-entity lookup.

## 1.2 Two Failure Modes

The execution gap manifests in two distinct ways depending on the operation type.

### Analytical failure: the LLM gives up and returns a formula

**Query**: *"What percent of YTD expense is represented by the single largest invoice?"*
**Expected**: Largest invoice $4,200.00 ÷ YTD $64,495.00 = **6.5%**
**Actual**: *"I'm missing the required data. Here is the formula: Percentage = (Largest Invoice / Total YTD Expense) × 100"*

The LLM knows the formula. It does not retrieve the data. The eval judge confirms:
> *"No relevant finance or expense data is available."*

To answer correctly, the agent must:
1. Know that GL transaction data lives in `GeneralJournalAccountEntry`
2. Fetch all expense-account lines with `TransDate ge 2026-01-01`
3. Aggregate client-side (FnO OData does not support `$aggregate`)
4. Compute the ratio — but none of this happens

### Transactional failure: wrong entity, missing fields, broken sequence

**Query**: *"Create a purchase requisition with items C0001 and C0002"*

The correct execution is:
```
step 1: data_create_entities → PurchaseRequisitionHeaders
          required fields: RequisitionName, BuyerGroupId, CompanyDataAreaId, RequestedDate
step 2: data_create_entities → PurchaseRequisitionLines  (using RequisitionId from step 1)
          required fields: ItemNumber, PurchaseQuantity, PurchaseUnitSymbol, ProcurementCategory
step 3: workflow action → submit for approval
```

Without knowing the entity names, required fields, and step dependencies, the LLM either calls the wrong entity, omits required fields, or attempts all steps in a single call.

## 1.3 Why the Current Setup Cannot Bridge This Gap

The FnO MCP server exposes two families of **generic, atomic primitives**:

**`data_*`** — OData CRUD:
```
data_find_entities(odataPath, odataQueryOptions)
data_create_entities(odataPath, entityDefinitionsJson)
data_update_entities(updatedOdataPathAndFieldValuesJson)
data_delete_entities(odataPaths)
data_find_entity_type(tableSearchFilter)
data_get_entity_metadata(entitySetName, ...)
```

**`form_*`** — UI interaction:
```
form_open_menu_item, form_click_control, form_set_control_values, ...
```

These tools are intentionally generic — FnO has thousands of entities and it is not feasible to expose one tool per entity. But this puts the entire burden of FnO domain knowledge on the LLM at inference time:

- Which OData entity name maps to which business concept?
- Which fields are required for each entity?
- What is the correct step sequence for multi-step operations?
- Which accounts classify as "expense"? What does "YTD" mean in FnO data terms?
- How to aggregate when OData does not support server-side aggregation?

Without a layer that encodes this knowledge, the LLM either hallucinates or gives up. **The tools exist. The knowledge bridge does not.**

---

# Part 2 — The Skill Graph

## 2.1 Architecture Overview

The solution is a **Skill Graph** between the LLM and the tool layer. The LLM handles intent and parameter extraction; Skills encode the FnO domain knowledge and orchestrate tool calls.

```
User
  │
  ▼
Agent Runtime
  ├── Intent Router      classifies query type and selects skill
  ├── Parameter Extractor  pulls company, date range, IDs from natural language
  └── Response Composer  formats tool results into natural language
  │
  ▼
Skill Graph
  ├── Transactional Skills   document CRUD + workflow actions
  └── Analytical Skills      aggregation + computation + derived metrics
  │
  ▼
Tool Layer (MCP Servers)
  ├── FnO MCP     generic OData CRUD + form interaction  (transactional)
  └── BPA MCP     pre-computed analytics, time-series, KPIs  (analytical)
  │
  ▼
FnO (Dynamics 365 Finance & Operations)
```

**Key principle**: the LLM never sees OData entity names, field names, or aggregation logic. It sees only business-level Skill interfaces. All FnO-specific knowledge lives in the Skill layer.

## 2.2 ERP Decomposition

To design Skills that cover FnO without exploding in count, the domain must be decomposed along two dimensions simultaneously.

### Vertical dimension: business hierarchy

```
Domain          Procurement · Finance · Sales · Inventory · HR · Production · ...
    ↓
Process         Procure-to-Pay (P2P) · Record-to-Report (R2R) · Order-to-Cash (O2C) · ...
    ↓
Business Object Purchase Requisition · GL Account · Sales Order · Vendor Invoice · ...
```

This gives the **business context**: what module, what process, what entity.

### Horizontal dimension: access pattern

Every operation on every business object falls into one of four access patterns:

| Pattern | Description | FnO example |
|---------|-------------|-------------|
| **Master Data Lookup** | Read static reference data | Vendors, items, GL chart of accounts, dimensions |
| **Transactional CRUD** | Create/read/update/delete business documents | Create PO, update PR line, delete draft journal |
| **Workflow Action** | Trigger state transitions or posting | Submit PR, Approve PO, Post invoice, Confirm receipt |
| **Analytical Query** | Aggregate, compute, and derive metrics across records | YTD expense, period variance, invoice ratio, trend |

The access pattern determines **which MCP server** handles the operation and **what kind of Skill** is needed.

### The 2D map: where Skills live

```
                  Master Data   Transactional   Workflow      Analytical
                  Lookup        CRUD            Action        Query
                ┌─────────────┬───────────────┬─────────────┬────────────────┐
Procurement     │ Vendor,      │ Create/Update │ Submit PR   │ Spend by vendor│
                │ Item catalog │ PR, PO lines  │ Confirm PO  │ PO aging       │
                ├─────────────┼───────────────┼─────────────┼────────────────┤
Finance (R2R)   │ GL accounts  │ Journal entry │ Post voucher│ Trial balance  │
                │ Dimensions   │ CRUD          │ Period close│ YTD variance   │
                ├─────────────┼───────────────┼─────────────┼────────────────┤
Sales (O2C)     │ Customers    │ Create/Update │ Confirm SO  │ Revenue trend  │
                │ Price lists  │ SO lines      │ Ship, Invoice│ Margin analysis│
                └─────────────┴───────────────┴─────────────┴────────────────┘
                     ↑                ↑               ↑              ↑
                FnO MCP          FnO MCP          FnO MCP        BPA MCP
              (data_find_*)   (data_create_*    (workflow       (pre-computed
                              data_update_*)     actions)        analytics)
```

## 2.3 Tool Ecosystem: Two MCP Servers, Two Roles

The key architectural insight is that **transactional and analytical operations require different tools**:

**FnO MCP** — generic OData primitives, correct for transactional work:
- Designed for per-entity CRUD and form interaction
- Returns raw records; no server-side aggregation
- Appropriate for: Master Data Lookup, Transactional CRUD, Workflow Actions

**BPA MCP** — Business Performance Analytics server, designed for analytical work:
- Pre-computed aggregations, KPIs, time-series views
- Understands business concepts like "YTD expense", "period variance"
- Does not require the client to fetch raw records and aggregate
- Appropriate for: Analytical Queries across Finance, Sales, Procurement

Routing to the wrong server causes the failure mode seen in evals: sending an analytical question to FnO MCP forces the LLM to attempt raw-record aggregation, which it cannot reliably do.

## 2.4 Skill Design per Access Pattern

### Master Data Lookup Skill
- **Knows**: entity name, key fields, cross-company rules
- **Input**: object type + optional filters
- **Calls**: `data_find_entities` on FnO MCP
- **Scale strategy**: one parameterized skill with entity mapping table; RAG over entity catalog for long tail

```yaml
skill: lookup_master_data
input: { object_type: "Vendor|Item|GLAccount|...", filters: {...}, company: string }
entity_map:
  Vendor:    { entity: VendorV2, select: VendorAccountNumber,Name,VendorGroupId }
  Item:      { entity: ReleasedProductsV2, select: ItemNumber,ProductName,ItemType }
  GLAccount: { entity: MainAccounts, select: MainAccountId,Name,AccountType }
```

### Transactional CRUD Skill
- **Knows**: entity name, required fields, header/lines dependency, read-only field list
- **Input**: operation type + business fields extracted by LLM
- **Calls**: `data_create_entities` / `data_update_entities` / `data_find_entities` on FnO MCP
- **Scale strategy**: explicit skills per high-frequency document type; field mapping in code

```yaml
skill: create_purchase_requisition
steps:
  - tool: data_create_entities
    entity: PurchaseRequisitionHeaders
    required: [RequisitionName, BuyerGroupId, CompanyDataAreaId, RequestedDate]
  - tool: data_create_entities
    entity: PurchaseRequisitionLines
    required: [RequisitionId, ItemNumber, PurchaseQuantity, PurchaseUnitSymbol]
    dependsOn: step[0].RequisitionId
```

### Workflow Action Skill
- **Knows**: action endpoint, preconditions (status must be X before action Y), side effects
- **Input**: document ID + action name
- **Calls**: specific workflow endpoints on FnO MCP
- **Scale strategy**: explicit skills per action per document type (~20–40 total); deterministic, not LLM-driven

```yaml
skill: submit_purchase_requisition
precondition: status == Draft
steps:
  - tool: data_update_entities
    entity: PurchaseRequisitionHeaders(RequisitionId='{id}')
    action: SubmitToWorkflow
postcondition: status == InReview
```

### Analytical Skill
- **Knows**: which BPA MCP tool answers which business question, date semantics, dimension filters
- **Input**: metric name + dimensions + date range
- **Calls**: BPA MCP (not FnO MCP)
- **Scale strategy**: explicit skills per KPI family; BPA MCP handles aggregation — no client-side computation needed

```yaml
skill: ytd_expense_analysis
tool: bpa_mcp.get_expense_summary
input_map:
  date_range: period param
  filters:    account classification = expense
returns: [total, by_account, by_vendor, largest_invoice]
```

The YTD expense eval failure (5.3% pass rate) is directly caused by the absence of this skill — the analytical query is sent to FnO MCP instead of BPA MCP, and the LLM cannot aggregate the raw records.

## 2.5 The Skill Graph for FnO

Skills compose, not just execute. A complex business query may chain multiple skills:

```
"Show me which vendors drove the biggest expense increase this month vs last month"
    │
    ├── Analytical Skill: get_expense_by_vendor(period=this_month)   → BPA MCP
    ├── Analytical Skill: get_expense_by_vendor(period=last_month)   → BPA MCP
    └── Compose: compute delta, rank by increase, format response
```

```
"Create a PR for the top-spending vendor this quarter"
    │
    ├── Analytical Skill: get_top_vendor_by_spend(period=this_quarter)  → BPA MCP
    └── Transactional Skill: create_purchase_requisition(vendor=result) → FnO MCP
```

This is the Skill Graph: a graph of reusable capabilities where Skills can call other Skills, and routing to the correct underlying MCP server is handled by the Skill, not the LLM.

---

# Part 3 — Implementation

## 3.1 Skill Implementation Patterns

Three patterns exist, with different reliability/flexibility tradeoffs:

| Pattern | LLM sees | Execution | Reliability | Flexibility |
|---------|----------|-----------|-------------|-------------|
| **System prompt text** | All OData details described in prose | LLM generates tool calls | Low — LLM can deviate | High |
| **High-level tool definition** | Business-level interface only | Code executes tool calls | Medium-high | Medium |
| **Pure code routing** | Only final result | Classifier + code | Highest | Low |

**Pattern 1 (system prompt)**: Skill knowledge is written as natural language instructions. The LLM still owns execution and can hallucinate entity names or forget OData rules. Narrows the gap, does not close it.

**Pattern 2 (high-level tool — recommended)**:
```
LLM sees:   ytd_expense_analysis(company, date_range)
Code does:  calls BPA MCP with correct parameters, returns structured result
LLM never sees: BPA tool names, parameter schemas, aggregation logic
```
The LLM's role is reduced to intent classification and parameter extraction. All domain-specific execution is in code.

**Pattern 3 (pure code routing)**: An embedding-based classifier matches the query to a skill without LLM reasoning. Used for highest-risk irreversible operations (post invoice, delete, cancel) where reliability is non-negotiable.

**Recommended**: Pattern 2 as the default. Pattern 3 for irreversible actions.

## 3.2 Skill Protocol Landscape

The industry has a standard for the **Tool layer** (MCP) but no equivalent for the **Skill layer**.

**MCP Composition** (most pragmatic): build a Skill-layer MCP server that internally calls atomic MCP servers. The LLM interacts only with the orchestrator; the FnO MCP and BPA MCP are invisible to it.

```python
# Skill-layer MCP server
@server.call_tool()
async def ytd_expense_analysis(company: str, year: int):
    return await bpa_client.call_tool("get_expense_summary", {
        "company": company, "period": f"YTD-{year}"
    })

@server.call_tool()
async def create_purchase_requisition(company: str, name: str, items: list):
    header = await fno_client.call_tool("data_create_entities", {...})
    lines  = await fno_client.call_tool("data_create_entities", {...})
    return {"requisitionId": header["RequisitionId"]}
```

**Google A2A Protocol** (emerging): agent-to-agent protocol where each agent publishes a capability card. Complements MCP — MCP for tool invocation, A2A for skill discovery and delegation across agents.

**Framework abstractions** (LangChain, Semantic Kernel, AutoGen): all have internal Skill/Plugin concepts, but none are interoperable. Avoid deep coupling to any one framework.

Likely convergence: **MCP for tools + A2A for skills/agents** as complementary open standards.

## 3.3 Solving the Scale Problem

FnO has thousands of operations across dozens of modules. Static enumeration of one Skill per operation is not feasible. The asymmetric treatment:

| Operation type | Scale | Solution |
|----------------|-------|----------|
| **Master Data Lookup** | Large but uniform | One parameterized Skill + entity mapping table; RAG for long tail |
| **Transactional CRUD** | Large but uniform pattern | Explicit Skills for top-20 document types; RAG over FnO entity metadata for the rest |
| **Workflow Actions** | ~20–40 finite operations | All explicit, deterministic, hardcoded |
| **Analytical Queries** | Unbounded questions, finite KPI families | BPA MCP handles the aggregation; Skills map question intent to BPA tool |

**RAG over FnO entity metadata**: pre-index all entity names, descriptions, and key fields using `data_find_entity_type` + `data_get_entity_metadata`. At query time, retrieve the 2–3 most relevant entities and inject only that metadata into context. Covers the long tail without bloating the Skill registry.

**Fine-tuning** (longer term): embed FnO entity knowledge directly into model weights. Microsoft does this internally for Copilot for Finance & Operations. Eliminates runtime retrieval overhead but requires significant training data and ongoing maintenance as FnO schema evolves.

## 3.4 Recommended Architecture

```
User query
    │
    ▼
Intent Router  (LLM: classify access pattern + extract parameters)
    │
    ├─[Analytical]──────────────────────────────────────────────────┐
    │                                                               │
    │   Analytical Skill                                            │
    │   (maps business metric to BPA MCP tool)                      │
    │       │                                                       │
    │       ▼                                                       │
    │   BPA MCP                                                     │
    │   (pre-computed aggregations, KPIs, time-series)              │
    │                                                               │
    ├─[Workflow Action]──────────────────────────────────────────────┤
    │                                                               │
    │   Workflow Skill  (deterministic, explicit per action)        │
    │   (checks preconditions → calls action endpoint)              │
    │       │                                                       │
    │       ▼                                                       │
    │   FnO MCP                                                     │
    │                                                               │
    ├─[Transactional CRUD / Master Data]──────────────────────────── ┤
    │                                                               │
    │   Matches known Skill?                                        │
    │   ├── Yes → execute explicit Skill  (code, deterministic)     │
    │   └── No  → retrieve entity metadata via RAG                  │
    │              inject into LLM context                          │
    │              LLM generates OData call                         │
    │       │                                                       │
    │       ▼                                                       │
    │   FnO MCP                                                     │
    │                                                               │
    └───────────────────────────────────────────────────────────────┘
    │
    ▼
LLM Response Composer  (formats all tool results into natural language)
```

## 3.5 Evaluation

Eval is how we validate that the design works. Each layer of the architecture has a corresponding eval signal:

| Layer | Eval signal |
|-------|-------------|
| Intent routing | Did the router select the correct access pattern and skill? |
| MCP server routing | Was the request correctly sent to FnO MCP vs BPA MCP? |
| Skill execution | Did the skill produce correct entity names, field selections, OData options, or BPA parameters? |
| End-to-end | Did the final response correctly answer the business question? |

If end-to-end scores are low, the layer-by-layer signals tell us exactly where the breakdown is — routing, skill execution, or response composition. Without the Skill layer, all failures look the same from the outside.
