# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Evaluation dataset repository for two distinct AI assistant evaluation tracks:

1. **D365 F&O Catalyst MCP eval** — Purchase requisition and trial balance scenarios tested against a live MCP server
2. **AI-Gen / LMC financial analysis eval** — Public company financial analysis queries (419 queries across topics like financial performance, geographic insights, peer comparisons)

## Repository Structure

```
OrigData/               # Raw source files
  Catalyst_FnO.csv      # 275-record CSV with full metadata (main editable source)
  aigen_419.tsv         # 419 financial analysis utterances + segments
  aigen_419_lmc_20260126.yaml  # LMChecklist YAML for the aigen queries
  lmc_ar_evals_tenant_1_26_rubric.yaml  # AR eval rubric (metric tag definitions)
  Sample Query-DA.tsv   # DA extensibility test queries (multi-DA, CIQ annotation)
  Sample Query-MultiTurn.tsv / Sample Query-SingleTurn.tsv

Dataset/
  From Abhinav/
    catalyst_seval_poc_39_examplesTSV 1.tsv  # 39 FnO seval examples (Utterance+Segment)
  LMChecklist/
    lmc_mcp_server_evals.yaml  # MCP server eval (groundedness/task_completion/tool_selection rubric)
    lmc_ar_evals_tenant_1_26_rubric.yaml     # AR eval rubric copy
  Mahsa-200/
    mahsa-200.tsv        # 200 FnO eval examples (seval TSV)
    mahsa-200.yaml       # 200 FnO eval examples (LMChecklist YAML with accuracy assertions)
    convert_examples.py  # Script to regenerate TSV+YAML from raw export

fno_mcp_singleone.tsv   # Minimal single-query test file
```

## Data Formats

### TSV (seval format)
Used for utterance routing tests. Two columns: `Utterance` (user query) and `Segment` (scenario/product area label).

### LMChecklist YAML
Used for rubric-based evaluation. Structure:
1. **Metric tag definitions** (top of file) — each `tag` entry has `metric: true` and a list of `assertions` with `level: critical`
2. **Query entries** — each query has `tags` (which metric definitions apply) and optionally inline `assertions` (expected response content)

```yaml
- tag: accuracy
  metric: true
  assertions:
  - text: '...'
    level: critical

- query: 'user question here'
  tags:
  - accuracy
  - groundness
  assertions:
  - text: 'expected response content'
    level: critical
```

### CSV (OrigData/Catalyst_FnO.csv)
Nine columns: Scenario Name, Product Area, Type (Create/Read/Update/Delete/Act), User Question, Expected Response, Multi-Turn Conversation Pattern, Contact alias, User Role, Ready for Review.

## Regenerating Eval Files

To regenerate `mahsa-200.tsv` and `mahsa-200.yaml` from the raw source:

```bash
cd Dataset/Mahsa-200
python convert_examples.py
```

The script reads `mahsa's200example` (tab-separated export), writes a seval TSV and a LMChecklist YAML with accuracy/groundness/structure/depth metric tags.

## Evaluation Tracks

### FnO MCP Server Eval (`Dataset/LMChecklist/lmc_mcp_server_evals.yaml`)
Metrics: **groundedness**, **task_completion**, **tool_selection**, **error_handling**
Covers the full purchase requisition lifecycle in USMF legal entity.

### FnO Trial Balance / AR Eval (`OrigData/lmc_ar_evals_tenant_1_26_rubric.yaml`)
Metrics: **structure**, **depth**, **recency**, **citation**
Covers GL account queries, voucher tracing, and financial reporting scenarios.

### Financial Analysis Eval (`OrigData/aigen_419_lmc_20260126.yaml`)
Metrics: **structure**, **recency**, topic-specific depth tags (e.g., `financialperformance&financialhealth_depth`, `geographic&governmentalinsights_depth`)
Covers public company queries across 419 utterances.

## Key Business Objects

- Purchase Requisitions: 6-digit IDs (000081, 000082, 000083)
- Purchase Orders: 8-digit IDs (00000200, 00000205)
- Items: C0001–C0004; Vendor: US-111 (Contoso office supply)
- Product Receipt numbers: `PR-YYMMDD-XX` format; Invoice numbers: `INV-XXXXX`
- GL Accounts: 4-digit (1110, 1300, 1650, 6110); Vouchers: 6-digit (000123)
- Snapshot IDs: `TB_YYYY_MM` format
- Legal entity: USMF; Date format: M/D/YYYY; Currency: USD ($)

## Status Workflows

Purchase Requisition: `Draft → In Review → Approved → (Cancelled)` (can recall back to Draft)
Purchase Order: `Open order → Confirmed → Received → Invoiced`
