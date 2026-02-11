# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a dataset repository for Dynamics 365 Finance & Operations (F&O) Catalyst AI assistant training data. The dataset contains conversation scenarios covering various business processes and functional areas within D365 F&O.

## Data Structure

### CSV Schema (`OrigData/Catalyst_FnO.csv`)

The dataset is structured with the following columns:

1. **Scenario Name**: The business process or workflow (e.g., "Requisition to Reciept", "Trial Balance")
2. **Product Area**: Functional module in D365 F&O (e.g., "Procurement & Sourcing", "Record to report")
3. **Type**: Operation category - Create, Read, Update, Delete, Act
4. **User Question**: Natural language query from the user
5. **Expected Response (in demo data)**: Detailed AI assistant response with structured formatting
6. **Multi-Turn Conversation Pattern**: Description of conversation flow across multiple interactions
7. **Contact alias**: Internal contact reference
8. **User Role**: User persona for the scenario
9. **Ready for Review**: Quality gate indicator (Yes/No)

### Data Characteristics

- Total records: 276 rows (including header)
- Covers multiple D365 F&O modules including:
  - Procurement & Sourcing (Purchase Requisitions)
  - Record to Report (Trial Balance, GL Account operations)
  - Other financial and operational processes

- Question types span CRUD operations plus workflow actions (approve, submit, recall)
- Responses include formatted data structures, status updates, and action confirmations
- Scenarios demonstrate both single-turn and multi-turn conversation patterns

## Working with the Dataset

### Reading the CSV

The CSV uses standard comma separation with quoted fields for multi-line content. Expected responses contain rich formatting including:
- Bullet points (• character)
- Status indicators (✓ checkmark)
- Structured sections with headers
- Embedded line breaks within cells

### Legal Entity Context

Most scenarios use "USMF" as the demo legal entity. This is a standard Dynamics 365 F&O demo company identifier.

### Key Business Objects

Common entities referenced in the dataset:
- Purchase Requisitions (identified by numeric IDs like 000081, 000082)
- Items/Products (identified by codes like C0001, C0002)
- GL Accounts (numeric account codes like 1650, 6110)
- Vouchers (numeric IDs like 000123)
- Vendors (alphanumeric codes like US-111)

## Data Quality Considerations

When analyzing or extending this dataset:

1. **Consistency**: Maintain the established response format patterns
2. **Entity References**: Ensure cross-reference integrity between questions and responses
3. **Status Workflows**: Follow D365 F&O standard status progressions (Draft → In Review → Approved)
4. **Date Formats**: Uses M/D/YYYY format (e.g., 1/27/2026)
5. **Currency**: Amounts shown with $ symbol and USD designation
