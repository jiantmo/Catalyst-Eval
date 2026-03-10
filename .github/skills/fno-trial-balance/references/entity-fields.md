# VendInvoiceJournalLine Entity — Field Reference

Source: `AxDataEntityView/VendInvoiceJournalLineEntity.xml`

OData path: `VendInvoiceJournalLines`
Header entity OData path: `VendInvoiceJournalHeaders`

## Key fields for expense queries

| OData Field Name | Underlying Table Field | Type | Notes |
|-----------------|----------------------|------|-------|
| `Company` | DataAreaId | string | Company filter. Always use `Company eq 'USMF'` |
| `InvoiceDate` | DocumentDate | date | Invoice document date. **Preferred for date filtering.** |
| `Date` | TransDate | date | Transaction/posting date. |
| `Debit` | AmountCurDebit | decimal | Debit amount in transaction currency. Expense invoices post here. |
| `Credit` | AmountCurCredit | decimal | Credit amount in transaction currency. |
| `Invoice` | Invoice | string | Invoice identifier. Group by this to find distinct invoices. |
| `AccountDisplayValue` | — (computed) | string | GL account display value (e.g. "602200"). Use for account filtering. |
| `OffsetAccountDisplayValue` | — (computed) | string | Offset account display value. |
| `JournalBatchNumber` | JournalNum | string | Journal batch number. Links to header. |
| `Currency` | CurrencyCode | string | Transaction currency code (e.g. "USD"). |
| `Description` | Txt | string | Line description / memo. |
| `Voucher` | Voucher | string | Voucher number. |
| `LineNumber` | LineNum | decimal | Line sequence number within journal. |
| `DueDate` | Due | date | Payment due date. |
| `PostingProfile` | PostingProfile | string | Vendor posting profile. |
| `DefaultDimensionDisplayValue` | — (computed) | string | Financial dimension values. |

## Header-level fields (VendInvoiceJournalHeaders)

| OData Field Name | Underlying Field | Notes |
|-----------------|-----------------|-------|
| `JournalBatchNumber` | JournalNum | Key. Links to lines. |
| `JournalName` | JournalName | Journal name/type. |
| `Description` | Name | Journal description. |
| `IsPosted` | Posted | Whether the journal is posted. |
| `JournalTotalDebit` | JournalTotalDebit | Total debit across all lines. |
| `JournalTotalCredit` | JournalTotalCredit | Total credit across all lines. |

## OData query notes

- **No server-side `$aggregate`**: FnO OData does not support `$apply=aggregate(...)`.
  Always retrieve lines and aggregate client-side.
- **Company filter is required**: Without it you may get data from all legal entities.
  Use `Company eq 'USMF'`.
- **Date field choice**: Use `InvoiceDate` (DocumentDate) for invoice-level date filtering.
  Use `Date` (TransDate) if you need the GL posting date.
- **Amount sign**: For vendor expense invoices, the expense amount is in `Debit`.
  Net = `Debit - Credit`.

## Example OData calls

**All YTD expense lines for USMF:**
```
VendInvoiceJournalLines?$filter=InvoiceDate ge 2026-01-01 and Company eq 'USMF'
  &$select=Invoice,InvoiceDate,Debit,Credit,AccountDisplayValue,Description
```

**Lines for a specific date range:**
```
VendInvoiceJournalLines?$filter=InvoiceDate ge 2026-01-01 and InvoiceDate le 2026-01-15
  and Company eq 'USMF'
  &$select=Invoice,Debit,Credit
```
