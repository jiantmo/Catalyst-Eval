---
name: fno-trial-balance
description: >
  Answer financial analysis questions about D365 F&O Trial Balance and expense data.
  Use when the user asks about: period expense totals, account balances,
  week-over-week or month-over-month variance, YTD expense percentages,
  largest invoice, account-level breakdowns, or any question involving
  GL expense accounts by date range.
compatibility: Requires D365 F&O MCP server
metadata:
  author: catalyst-eval
  version: "1.1"
---

# D365 F&O Trial Balance Skill

## Step 0: Resolve company before doing anything

**Always determine the company (legal entity) before querying.**

Priority order:
1. User explicitly states a company name or ID (e.g. "in USMF", "for Contoso", "company GBSI")
2. Extract from context (e.g. previous messages, document being discussed)
3. If still unknown — **ask the user**: "Which company (legal entity) should I use?"

Do not assume a default company. The company ID is required for all queries.

---

## Step 1: Choose data source

**Use Data Entity** when the question is about individual vendor invoices:
- "largest invoice", "total invoices", "exclude an invoice", "invoice count"
- Entity: `VendInvoiceJournalLines`

**Use Trial Balance form** when the question is about GL account balances by period:
- "expense total for a date range", "account balance", "variance between periods",
  "week-over-week change", "which account increased the most", "account breakdown"
- Form: `LedgerTrialBalanceListPage`

When in doubt: prefer the Trial Balance form for any question involving
a specific date range + dollar amount on an expense account.

---

## Path A: Data Entity — Vendor Invoice Queries

Use `data_find_entities` with:

```
odataPath: VendInvoiceJournalLines
filter:    Company eq '{company}'   ← use the resolved company ID
```

### Key fields

| OData Field | Maps to | Description |
|-------------|---------|-------------|
| `InvoiceDate` | DocumentDate | Invoice document date — use for date range filters |
| `Date` | TransDate | Transaction/posting date |
| `Debit` | AmountCurDebit | Debit amount (expense invoices post here) |
| `Credit` | AmountCurCredit | Credit amount |
| `Invoice` | Invoice | Invoice ID — group by this to identify distinct invoices |
| `AccountDisplayValue` | — | GL account display string |
| `Company` | DataAreaId | Company / legal entity ID |
| `Currency` | CurrencyCode | Transaction currency |
| `Description` | Txt | Line description |

See [entity-fields.md](references/entity-fields.md) for the full field list.

### Common patterns

**YTD total expense:**
```
filter: InvoiceDate ge {fiscal_year_start} and Company eq '{company}'
select: Invoice, InvoiceDate, Debit, Credit
→ client-side: SUM(Debit) - SUM(Credit) = net expense total
```

**Largest single invoice:**
```
filter: InvoiceDate ge {fiscal_year_start} and Company eq '{company}'
select: Invoice, Debit
→ client-side: GROUP BY Invoice, SUM(Debit) per group, then MAX
```

**Date range total:**
```
filter: InvoiceDate ge {date_from} and InvoiceDate le {date_to} and Company eq '{company}'
select: Debit, Credit
→ client-side: SUM(Debit) - SUM(Credit)
```

**Exclude largest invoice:**
```
1. Query all lines for the period, GROUP BY Invoice, SUM(Debit) per group
2. Identify the Invoice with the highest total
3. Period total - largest invoice amount = result
```

### Aggregation note
FnO OData does **not** support server-side `$aggregate`.
Always retrieve the full result set and aggregate client-side.
Use `$top=100` (or higher if needed) to avoid pagination issues.

---

## Path B: Trial Balance Form — GL Account Balance Queries

Use `form_open_menu_item` to open `LedgerTrialBalanceListPage` for the resolved company.

### Navigation steps

1. Open the Trial Balance list page:
   ```
   form_open_menu_item("LedgerTrialBalanceListPage", company="{company}")
   ```

2. Set the date range (From date / To date). Format: M/D/YYYY
   ```
   form_set_control_values({fromDate: "{date_from}", toDate: "{date_to}"})
   ```

3. Click **Calculate balances**:
   ```
   form_click_control("Calculate balances")
   ```

4. Read the results grid — one row per main account:
   - Account number, Description, Opening balance, Debit, Credit, Closing balance (net)

5. Filter by account number if needed (e.g. apply column filter for a specific account code).

### Expense account conventions

Expense accounts typically start with 6 (e.g. 6xxxxx range).
Account descriptions and numbers vary by company chart of accounts.
If account numbers are unknown, read all rows from the Trial Balance results
and identify expense accounts by their description or by asking the user.

---

## Multi-step patterns

### Variance between two periods

Run the Trial Balance **twice**, then subtract:
```
Step 1: dates {period1_start} to {period1_end} → Calculate → note balance = A
Step 2: dates {period2_start} to {period2_end} → Calculate → note balance = B
Variance = B - A
```

For **cumulative** balances: start both runs from the fiscal year start date.
For **period-only** activity: use that period's exact start and end date.

### Week-over-week comparison

```
Week 1: {week1_start} to {week1_end} → record each account balance
Week 2: {week2_start} to {week2_end} → record each account balance
Difference per account = Week 2 balance - Week 1 balance
Largest increase = account with highest positive difference
```

### Account breakdown as percentage

```
Step 1: Run Trial Balance for the period → get each account's closing balance
Step 2: SUM all expense account balances = period total
Step 3: Each account % = account balance / period total × 100
```

---

## Important rules

- **Company is required** — always resolve before querying (see Step 0).
- **Fiscal year start** — ask the user or infer from context if not obvious.
  Common default: January 1 of the current year.
- FnO OData does not support `$aggregate` — all aggregation is client-side.
- All date filters use ISO format for OData: `YYYY-MM-DD`.
  Trial Balance form dates use M/D/YYYY format.
