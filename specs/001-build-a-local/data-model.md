# Data Model for Local Expense Organizer

This document defines the data entities for the application, based on the feature specification.

## Entity: Transaction

Represents a single financial event.

| Field | Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary key | Not Null, Unique |
| `amount` | Float | The transaction amount | Not Null, > 0 |
| `description` | String | A brief description of the transaction | |
| `date` | Date | The date of the transaction | Not Null |
| `type` | String | "income" or "expense" | Not Null |
| `category_id` | Integer | Foreign key to the Category entity | Not Null |
| `account_id` | Integer | Foreign key to the Account entity | Not Null |

## Entity: Category

A label for a transaction.

| Field | Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary key | Not Null, Unique |
| `name` | String | The name of the category | Not Null, Unique |
| `type` | String | "income" or "expense" | Not Null |

**Initial Data:**
- **Expense Categories**: Food, Transportation, Housing, Utilities, Entertainment
- **Income Categories**: Salary, Gifts, Other

## Entity: Account

The source or destination of funds.

| Field | Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Primary key | Not Null, Unique |
| `name` | String | The name of the account | Not Null, Unique |

**Initial Data:**
- Cash
- Bank