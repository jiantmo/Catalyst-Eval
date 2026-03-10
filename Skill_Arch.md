# Modern Modular AI / Agent Architecture

---

# 0. The Problem This Document Is Responding To

## 0.1 Observed Eval Results

Multiple evaluation runs against the FnO Declarative Agent (DA) using the SEVAL framework have produced consistently poor results. The most recent run as of March 2026:

| Eval job                                     | Queries | Control pass rate | Treatment pass rate |
| -------------------------------------------- | ------- | ----------------- | ------------------- |
| 200TrialBalance-FnODA_Accuracy_Only_20260303 | 206     | **11/206 (5.3%)** | **2/206 (1.0%)**    |

All failing queries are Trial Balance analytical questions — date-range aggregations, period comparisons, percentage calculations — run against a live FnO synthetic tenant with real data.

## 0.2 What the Failures Look Like

**Query**: *"What percent of YTD expense is represented by the single largest invoice?"*

**Expected**: Largest invoice $4,200.00 ÷ YTD total $64,495.00 = **6.5%**

**Actual Copilot response**:
> "I'm missing the required data (the largest invoice amount and the total YTD expense). Here is the formula you can use once the data is available: Percentage = (Largest Invoice / Total YTD Expense) × 100"

Copilot knows the formula. It does not retrieve the data. Score: **0**.

The eval judge's rationale confirms the root cause:
> *"The response does not perform any calculation... no relevant finance or expense data is available."*

This pattern repeats across virtually all 206 queries.

## 0.3 Root Cause: The Execution Gap

The FnO DA has access to MCP tools that can retrieve the underlying data. The problem is not missing tools — it is that the LLM **cannot translate an analytical business question into the sequence of OData calls needed to retrieve and aggregate the answer**.

To answer "What percent of YTD expense is the largest invoice?", the correct execution chain is:

```
1. data_find_entities
     odataPath:   GeneralJournalAccountEntry (or equivalent)
     filter:      TransDate ge 2026-01-01, account = expense accounts
     → returns:   list of transaction lines with amounts and invoice refs

2. Client-side aggregation:
     - sum all lines → YTD total ($64,495.00)
     - group by invoice number → find max ($4,200.00)

3. Calculate: 4200 / 64495 = 6.5%
```

The LLM must independently know:
- Which OData entity holds GL transaction data in FnO
- How to filter by date range in FnO OData format (`TransDate ge ...`)
- That FnO OData does not support server-side `$aggregate` — aggregation must be done client-side
- Which accounts classify as "expense"

Without this knowledge, the LLM gives up and returns a formula instead of an answer. This is the **execution gap**.

## 0.4 Why This Document Exists

This document analyzes the execution gap and examines how a **Skill layer** between the LLM and the MCP tools can close it — and where the limits of that approach are for a system as large as FnO.

---

## 1. Overview

Modern AI systems are evolving from simple **LLM + tools** setups to a more structured **modular architecture**.

The emerging pattern can be summarized as:

```
LLM
 + 
Agent Runtime
 +
Skill Graph
 +
Tool Ecosystem
 +
Memory & Evaluation
```

This architecture improves:

- modularity
- composability
- reliability
- evaluation
- scalability

---

# 2. High-Level Architecture

```
User
  │
  ▼
Agent Runtime
  │
  ├── Planner
  ├── Router
  └── Execution Engine
  │
  ▼
Skill Graph
  │
  ├── Skill A
  ├── Skill B
  ├── Skill C
  │
  ▼
Tool Layer
  │
  ├── Tool 1
  ├── Tool 2
  ├── Tool 3
  │
  ▼
External Systems
(API / Database / Services)
```

---

# 3. Key Architectural Layers

## 3.1 Agent Runtime

The **Agent Runtime** orchestrates the overall task execution.

Responsibilities:

- task planning
- routing requests
- coordinating skills
- managing execution flow

Typical components:

```
Agent Runtime
 ├── Planner
 ├── Router
 ├── Context Manager
 ├── Execution Engine
 └── Safety / Guardrails
```

Example workflow:

```
User request
   ↓
Planner determines task structure
   ↓
Router selects appropriate skill(s)
   ↓
Execution engine runs the workflow
```

---

# 3.2 Skill Graph

The **Skill Graph** represents reusable capabilities of the system.

Unlike simple tool lists, skills can **compose multiple tools and other skills**.

```
Skill Graph
 ├── Data Retrieval Skill
 ├── Data Analysis Skill
 ├── Report Generation Skill
 └── Decision Support Skill
```

Example:

```
Sales Analysis Skill
 ├── Retrieve sales data
 ├── Perform aggregation
 ├── Detect trends
 └── Generate explanation
```

Skills can depend on other skills:

```
Order Insight Skill
     │
     ├── Product Lookup Skill
     ├── Pricing Analysis Skill
     └── Promotion Detection Skill
```

This creates a **graph of capabilities** rather than a flat tool list.

---

# 3.3 Tool Layer

Tools represent **atomic executable functions**.

Examples:

```
Tools
 ├── search_database
 ├── run_sql_query
 ├── calculate_price
 ├── get_inventory
 └── call_external_api
```

Each tool typically provides:

```
Tool Definition
 ├── name
 ├── description
 ├── input schema
 ├── output schema
```

Tools are often exposed through protocols such as:

- Model Context Protocol (MCP)
- Function Calling APIs

---

# 3.4 Tool Ecosystem / Integration Layer

The tool layer connects the AI system with real-world systems.

Examples:

```
External Systems
 ├── Databases
 ├── Enterprise APIs
 ├── Search Engines
 ├── ERP / CRM Systems
 └── Knowledge Bases
```

Example integration:

```
getProduct → Product Service
getInventory → Inventory API
calculatePrice → Pricing Engine
```

---

# 3.5 Memory Layer

The **Memory Layer** enables persistent context and knowledge reuse.

Types of memory:

```
Memory
 ├── Short-term context
 ├── Conversation history
 ├── Long-term knowledge
 ├── Vector databases
 └── User preferences
```

Common implementations:

- vector search
- retrieval augmented generation (RAG)

---

# 3.6 Evaluation Layer

Modern AI systems increasingly include **built-in evaluation frameworks**.

```
Evaluation
 ├── Response quality
 ├── Groundedness
 ├── Reasoning correctness
 ├── Tool usage accuracy
 └── Safety compliance
```

Evaluation can operate at multiple levels:

```
LLM output evaluation
Skill-level evaluation
Tool-level evaluation
End-to-end task evaluation
```

---

# 4. Execution Flow Example

Example task:

```
User: "Analyze why sales dropped this quarter"
```

Execution pipeline:

```
User request
     ↓
Planner creates execution plan
     ↓
Router selects Sales Analysis Skill
     ↓
Skill executes sub-steps

  retrieve_sales_data
        ↓
  analyze_trend
        ↓
  detect_root_cause
        ↓
  generate_report

     ↓
Final response returned to user
```

---

# 5. Relationship with MCP

Model Context Protocol (MCP) operates primarily at the **Tool Layer**.

```
Agent Runtime
     ↓
Skill Graph
     ↓
Tools (MCP Servers)
     ↓
External APIs
```

MCP standardizes:

```
tool discovery
tool schema
tool invocation
```

However, MCP does **not define**:

- skill composition
- workflow orchestration
- agent planning

These are handled by the **Agent Runtime and Skill Graph** layers.

---

# 6. Why This Architecture Matters

Compared to simple **LLM + tools**, this modular architecture provides:

### Better Modularity

```
Capabilities are reusable
Skills can be composed
Tools remain atomic
```

### Improved Reliability

Structured workflows reduce unpredictable LLM behavior.

### Easier Evaluation

Each layer can be evaluated independently.

```
Tool correctness
Skill performance
Agent decision quality
```

### Better Scalability

The system can scale to hundreds of tools by grouping them into skills.

---

# 7. Future Direction

Emerging AI system architectures are moving toward something similar to an **AI operating system**.

Potential components:

```
AI Runtime Platform
 ├── Skill Registry
 ├── Skill Graph Engine
 ├── Tool Registry
 ├── Memory Systems
 ├── Evaluation Framework
 └── Safety Guardrails
```

This enables large-scale **multi-agent ecosystems** and enterprise AI platforms.

---

# 8. Applying This Architecture to FnO MCP — The Execution Gap Problem

## 8.1 The Problem: Generic Tools vs. Business Intent

The FnO MCP server exposes two families of tools:

**`data_*` tools** — generic OData CRUD primitives:
```
data_find_entities(odataPath, odataQueryOptions)
data_create_entities(odataPath, entityDefinitionsJson)
data_update_entities(updatedOdataPathAndFieldValuesJson)
data_delete_entities(odataPaths)
data_find_entity_type(tableSearchFilter)
data_get_entity_metadata(entitySetName, ...)
```

**`form_*` tools** — UI-level interaction primitives:
```
form_open_menu_item, form_click_control, form_set_control_values, ...
```

When a user asks: *"Find the 5 most recent sales orders"*, the LLM must independently infer:

- The OData entity name is `SalesOrderHeadersV2` (not `SalesOrders`)
- The query must include `cross-company=true`
- The correct `$select` fields: `SalesOrderNumber`, `OrderingCustomerAccountNumber`, `SalesOrderStatus`, etc.
- Enum fields require a namespace prefix (e.g., `Microsoft.Dynamics.DataEntities.Status'Active'`)
- Multi-step operations must be sequenced correctly (e.g., create PR header → add lines → submit)

Every step in this inference chain is a potential failure point. This is the **execution gap**: the distance between a business-level question and the technical knowledge needed to invoke the right MCP tool correctly.

---

## 8.2 The LLM → Skill → MCP Pattern

The solution is to insert a **Skill layer** between the LLM and the MCP tools. The Skill layer encodes FnO domain knowledge so the LLM does not have to rediscover it on every request.

```
User: "Find recent 5 sales orders"
         ↓
LLM  (intent classification + parameter extraction)
         ↓
Skill Router  →  selects: QuerySalesOrders skill
         ↓
Skill Execution  (pre-defined workflow with hardcoded FnO knowledge)
  - entity:  SalesOrderHeadersV2
  - fields:  SalesOrderNumber, Status, CurrencyCode, ...
  - rules:   always add cross-company=true
  - maps:    company param → dataAreaId eq '{company}'
         ↓
MCP Tool Call
  data_find_entities(
    odataPath = "SalesOrderHeadersV2",
    odataQueryOptions = "cross-company=true&$top=5&$select=SalesOrderNumber,..."
  )
         ↓
FnO OData API
```

A Skill is **not** an LLM prompt. It is a structured definition that:

- Maps business concepts to OData entity names
- Defines the minimal correct `$select` fields for each use case
- Encodes multi-step sequencing for write operations
- Translates LLM-extracted parameters (company, date range, count) into OData syntax

---

## 8.3 Skill Definition Example

```yaml
skill: query_sales_orders
intent_patterns:
  - "find sales order"
  - "show sales orders"
  - "recent sales"
steps:
  - tool: data_find_entities
    odataPath: SalesOrderHeadersV2
    defaultOptions: "cross-company=true&$select=SalesOrderNumber,OrderingCustomerAccountNumber,SalesOrderStatus,CurrencyCode&$top=5"
    paramMap:
      company: "dataAreaId eq '{company}'"
      top: "$top={top}"
```

For multi-step write operations:

```yaml
skill: create_purchase_requisition
steps:
  - tool: data_create_entities
    odataPath: PurchaseRequisitionHeaders
    fields: [RequisitionName, RequestedDate, CompanyDataAreaId]
  - tool: data_create_entities
    odataPath: PurchaseRequisitionLines
    fields: [RequisitionId, ItemNumber, PurchaseQuantity, PurchaseUnitSymbol]
    dependsOn: step[0].RequisitionId
  - tool: data_update_entities   # submit for approval
    odataPath: PurchaseRequisitionHeaders(...)
    action: submit
```

---

## 8.4 Three-Tier Bridging Strategy

| Tier                         | What it does                                                                                                                                                       | Timeframe   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| **System prompt enrichment** | Add FnO entity mapping inline: `"sales order" → SalesOrderHeadersV2`, common field lists, OData rules (`cross-company=true`). Fast to implement, brittle at scale. | Short-term  |
| **Skill library**            | Structured YAML/JSON skill definitions per business scenario. LLM selects a skill; skill drives tool calls. Reliable, maintainable.                                | Medium-term |
| **RAG over FnO metadata**    | Pre-index all entity metadata; retrieve relevant context at query time. Handles long-tail entities not covered by static skills.                                   | Long-term   |

---

## 8.5 Impact on Evaluation

The existing eval metrics (`groundedness`, `task_completion`, `tool_selection`, `error_handling`) remain valid but need to be extended once a Skill layer exists:

```
Current eval (flat):
  LLM + system prompt → MCP tools → response
  Metrics: tool_selection, task_completion, groundedness, error_handling

With Skill layer (layered eval):
  ├── Skill routing accuracy   Did the router select the correct skill for the intent?
  ├── Parameter extraction     Did the LLM correctly extract company, date, count, etc.?
  ├── Tool invocation          Did the skill generate correct OData paths and query options?
  └── End-to-end task          Did the final response correctly answer the business question?
```

Each layer can fail independently and should be evaluated independently. This is one of the key advantages of the modular architecture: **failures become attributable**.

---

# 9. How Skills Actually Work — Three Implementation Patterns

"Skill" is a concept, not a protocol. How it is implemented determines how reliable it is.

## Pattern 1: Skill as system prompt text (simplest, most fragile)

The skill definition is written as natural language instructions injected into the system prompt. The LLM reads the description and generates tool calls itself.

```
System Prompt:
  When the user asks about sales orders, call data_find_entities with
  odataPath=SalesOrderHeadersV2, always include cross-company=true,
  $select=SalesOrderNumber,Status,CurrencyCode...
```

The LLM still owns execution. It can mis-spell entity names, forget `cross-company=true`, or hallucinate field names. This pattern **narrows the gap but does not close it**.

---

## Pattern 2: Skill as a higher-level tool definition (recommended)

The skill is exposed as a structured tool with a business-level signature. The LLM only sees the high-level interface; deterministic code handles the translation to OData.

```
LLM sees:
  query_sales_orders(company: string, top: int)

LLM does NOT see:
  odataPath, $select, cross-company=true, field names, enum namespaces

Code does:
  def query_sales_orders(company, top=5):
      odata = f"cross-company=true&$select=...&$top={top}&$filter=dataAreaId eq '{company}'"
      return mcp_client.call("data_find_entities", "SalesOrderHeadersV2", odata)
```

The LLM's job is reduced to:
1. **Intent classification** — which skill to invoke
2. **Parameter extraction** — company, date range, count, etc.

All OData knowledge lives in code. Execution is deterministic.

---

## Pattern 3: Pure code routing (most reliable, least flexible)

An embedding-based classifier (not an LLM) matches the user query to a skill. The LLM is only invoked at the end to compose a natural language response from tool results.

```
User query → intent classifier (embeddings) → skill selected → code executes → LLM formats response
```

No LLM reasoning in the execution path. Maximum reliability for known, high-frequency operations. Cannot handle novel queries outside the classifier's training distribution.

---

## Summary

| Pattern                    | LLM sees                | Execution | Reliability | Flexibility |
| -------------------------- | ----------------------- | --------- | ----------- | ----------- |
| System prompt text         | All OData details       | LLM       | Low         | High        |
| High-level tool definition | Business interface only | Code      | Medium-high | Medium      |
| Pure code routing          | Nothing (result only)   | Code      | Highest     | Low         |

**Recommended**: Pattern 2 for most operations. Pattern 3 for the small set of highest-risk irreversible actions (post invoice, delete, cancel).

---

# 10. The Skill Protocol Landscape — No Standard Exists Yet

## Current state

The industry has a standard for the **Tool layer** (MCP), but no equivalent standard for the **Skill layer**.

```
Tool layer  ←  MCP is the de facto standard (Anthropic, adopted by OpenAI / Microsoft / Google)
Skill layer ←  fragmented; each team builds their own
```

## What exists

### MCP Composition (most pragmatic current approach)

An orchestrator MCP server exposes high-level business tools to the LLM while internally calling the atomic MCP server. The Skill layer *is* an MCP server.

```python
# Orchestrator MCP server
server = MCPServer("fno-skill-layer")
fno_client = MCPClient("https://fno-env.operations.dynamics.com/mcp")

@server.call_tool()
async def query_sales_orders(company: str, top: int = 5):
    return await fno_client.call_tool("data_find_entities", {
        "odataPath": "SalesOrderHeadersV2",
        "odataQueryOptions": f"cross-company=true&$select=...&$top={top}&$filter=dataAreaId eq '{company}'"
    })
```

The LLM interacts only with the orchestrator MCP. The atomic FnO MCP is invisible to it. This reuses existing MCP infrastructure without introducing a new protocol.

### Google Agent2Agent Protocol (A2A, released April 2025)

A protocol specifically for agent-to-agent communication. Each agent publishes an **Agent Card** (JSON) describing its skills and how to invoke them.

```json
{
  "name": "FnO Sales Agent",
  "skills": [
    { "id": "query_sales_orders", "description": "Find sales orders by company, date range, status" },
    { "id": "create_purchase_req", "description": "Create a purchase requisition in USMF" }
  ]
}
```

A2A is protocol-level (not framework-level) and is designed to complement MCP: MCP for tool invocation, A2A for agent/skill discovery and delegation.

### Framework-internal abstractions (not interoperable)

| Framework                             | Skill concept                      | Protocol?                |
| ------------------------------------- | ---------------------------------- | ------------------------ |
| Microsoft Semantic Kernel             | Plugin / KernelFunction            | No — framework internal  |
| LangChain                             | Tool / Chain                       | No — framework internal  |
| AutoGen                               | Tool                               | No — framework internal  |
| M365 Copilot (your FNO_MCP_TOOL.json) | Declarative Agent Plugin (OpenAPI) | Partially — OpenAPI spec |

## Likely convergence

```
MCP  — Tool layer standard (already established)
A2A  — Skill/Agent layer standard (emerging)
```

These two protocols are complementary and both are open. The pragmatic bet is to design Skill layer interfaces that can be exposed as either an MCP tool or an A2A skill without re-implementation.

---

# 11. The Scale Problem — Why Static Skill Enumeration Fails for FnO

## The real scope of FnO

FnO spans dozens of modules, each with multiple business objects and multiple operations per object:

```
Procurement & Sourcing   Sales & Marketing        Inventory Management
Warehouse Management     Production Control       Master Planning
General Ledger           Accounts Payable/Recv.   Fixed Assets
Budgeting                Project Management       HR & Payroll
Cost Accounting          Transportation           Quality Management
...
```

Each module × each business object × (Create / Read / Update / Delete / workflow actions) = **thousands of operations**.

Writing and maintaining a static Skill for every operation is not feasible. This is precisely why the FnO MCP tools are generic OData primitives — the surface area of FnO is too large for any fixed enumeration to cover.

## Why the explosion is asymmetric

On closer examination, the scale problem is not uniform:

| Operation type           | Scale                              | Pattern                                                    |
| ------------------------ | ---------------------------------- | ---------------------------------------------------------- |
| **Read queries**         | Unbounded — any entity, any filter | Uniform: always `data_find_entities` + OData               |
| **Simple CRUD**          | Large                              | Uniform: same OData tools, different entity paths          |
| **Multi-step workflows** | ~20–50 important ones              | Heterogeneous: sequence and dependencies vary per workflow |

The explosion is worst for reads. But reads follow a **completely uniform pattern** — the only variable is which entity and which fields. This is actually an opportunity, not just a problem.

---

# 12. Solutions That Actually Scale

## Solution A: Fine-tuning (knowledge in model weights)

Train a domain-specific model on FnO entity names, OData patterns, business workflows, and field semantics. The model natively knows that "sales order" maps to `SalesOrderHeadersV2`, that `cross-company=true` is always required, and that enum fields require namespace prefixes.

- **Advantage**: no runtime overhead, no context consumed, works for any entity
- **Disadvantage**: requires large training dataset, significant compute, expensive to maintain as FnO schema evolves
- **Who does this**: Microsoft internally for Copilot for Finance & Operations

## Solution B: RAG over FnO entity metadata (knowledge retrieved at runtime)

Pre-build an offline index of all FnO entity names, descriptions, and key field lists. At query time, semantically retrieve the 2–3 most relevant entities and inject only that metadata into context.

```
User: "show vendor invoices pending approval"
         ↓
Semantic search over entity index
         ↓
Retrieved: VendorInvoiceJournal — fields: InvoiceNumber, VendorAccountNumber, ApprovalStatus, ...
           hint: filter ApprovalStatus eq 'Pending', use cross-company=true
         ↓
Injected into LLM context (small, targeted)
         ↓
LLM generates correct OData call
```

FnO already exposes `data_find_entity_type` and `data_get_entity_metadata` — the raw material for this index already exists. The improvement is doing this **offline and indexed**, not dynamically at runtime on every query.

- **Advantage**: covers the full long tail of entities; no fine-tuning required
- **Disadvantage**: retrieval quality determines correctness; index must stay in sync with FnO schema

## Solution C: Asymmetric treatment — static for workflows, dynamic for reads

Accept that the two problem types need different solutions:

```
Read queries (unbounded)
  → RAG over entity metadata  (Solution B)
  → or: one parameterized meta-skill read_fno_entity(entity_type, filters)
        backed by a code-maintained entity mapping table

Multi-step workflows (finite, high-risk)
  → explicit hardcoded Skills (~20–50 key workflows)
  → deterministic execution, not LLM-driven
```

This is the most pragmatic near-term architecture: **finite explicit skills for what matters most, dynamic retrieval for everything else.**

---

# 13. Recommended Architecture for FnO at Scale

```
User query
    │
    ▼
Intent Router
    ├── Matches known workflow skill?
    │       │ Yes
    │       ▼
    │   Skill Executor (deterministic code)
    │   e.g. CreatePurchaseRequisition:
    │     step 1: data_create_entities → PurchaseRequisitionHeaders
    │     step 2: data_create_entities → PurchaseRequisitionLines
    │     step 3: data_update_entities → submit action
    │       │
    │       ▼
    │   FnO MCP (atomic tools)
    │
    └── No match (read query / long-tail CRUD)
            │
            ▼
        Entity Retriever
        (semantic search over pre-built FnO entity index)
            │
            ▼
        LLM + retrieved entity metadata
        (knows correct entity name, fields, OData rules)
            │
            ▼
        data_find_entities / data_create_entities / data_update_entities
            │
            ▼
        FnO MCP (atomic tools)
    │
    ▼
LLM response generation (formats tool results into natural language)
```

## Design principles this architecture follows

1. **LLM does reasoning, code does execution.** The LLM classifies intent and extracts parameters. Deterministic code or retrieved metadata handles the FnO-specific translation. The LLM never guesses OData entity names.

2. **Static skills only where it matters.** Explicit skills cover multi-step workflows and irreversible actions — the operations where reliability is non-negotiable. Everything else is handled dynamically.

3. **Domain knowledge has a home.** Entity knowledge lives in the retrieval index (not in the system prompt, not in model weights for most deployments). It can be updated when FnO schema changes without retraining or rewriting prompts.

4. **Evaluation is layered.** Each component can be measured independently:

```
Intent routing accuracy     → did the router pick the right path?
Parameter extraction        → did the LLM correctly extract company, date, ID?
Entity retrieval precision  → did the retriever return the right entity?
Tool invocation correctness → was the OData path and query options valid?
End-to-end task completion  → did the response correctly answer the business question?
```

5. **The FnO MCP stays generic by design.** The atomic OData tools are correct as-is. The intelligence gap is filled above them, not by replacing them.