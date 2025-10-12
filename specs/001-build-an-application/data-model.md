# Data Model for Expense Tracker Application

This document defines the data entities for the application, based on the feature specification. The data will be stored in a SQLite database.

## Transaction

Represents an income or expense transaction.

- **id**: `string` (UUID) - Unique identifier for the transaction.
- **date**: `string` (ISO 8601) - The date of the transaction.
- **amount**: `number` - The amount of the transaction.
- **type**: `string` - The type of transaction, either "income" or "expense".
- **category_id**: `string` (UUID) - The ID of the category this transaction belongs to.
- **account_id**: `string` (UUID) - The ID of the account this transaction is associated with.

## Category

Represents a category for transactions.

- **id**: `string` (UUID) - Unique identifier for the category.
- **name**: `string` - The name of the category (e.g., "Food & Groceries", "Salary").
- **type**: `string` - The type of category, either "income" or "expense".

## Account

Represents a financial account.

- **id**: `string` (UUID) - Unique identifier for the account.
- **name**: `string` - The name of the account (e.g., "Cash", "Bank").
- **type**: `string` - The type of account, either "cash" or "bank".
