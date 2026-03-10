# Expense Account Discovery Guide

Each D365 F&O company has its own chart of accounts. Never assume specific account numbers.
Use the patterns below to discover the relevant accounts at runtime.

## Typical account range conventions

Most standard D365 charts of accounts follow this pattern (but verify per company):

| Range | Type |
|-------|------|
| 1xxxxx | Assets |
| 2xxxxx | Liabilities |
| 3xxxxx | Equity |
| 4xxxxx | Revenue |
| 5xxxxx | Cost of goods / direct costs |
| 6xxxxx | Operating expenses |

> This is a common convention — not guaranteed. If the company uses a non-standard chart of
> accounts, ask the user which account range covers operating expenses.

## How to discover expense accounts

### Option 1: Read all rows from the Trial Balance results

After running `LedgerTrialBalanceListPage` for the period:
- Read all rows from the grid
- Identify rows where the Description contains keywords like "Expense", "Training",
  "Insurance", "Promotional", etc.
- Note the account number from those rows

### Option 2: Filter by account range in OData

When querying `GeneralJournalAccountEntryEntity` or `VendInvoiceJournalLines`,
filter by account range if the user says expenses are in the 6xxxxx range:
```
startswith(LedgerAccount,'6')
```

For a specific account once discovered:
```
startswith(AccountDisplayValue,'{account_number}')
```

### Option 3: Ask the user

If the query requires a specific account (e.g. "Training expense") and the account
number is not visible in the Trial Balance results, ask:
> "What is the GL account number for Training Expense in your chart of accounts?"

## When the user mentions an account by description

Map description → account number by:
1. Running the Trial Balance for any recent period
2. Scanning the Description column for the matching account name
3. Using that account number for the actual query

Do not hardcode account numbers between sessions or across companies.
