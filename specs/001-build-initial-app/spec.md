# Feature Specification: Local Expense Organizer

**Feature Branch**: `001-build-a-local`
**Created**: 2025-10-12
**Status**: Draft
**Input**: User description: "Build a local web application that can help me organize my daily expense. I want to be able to input expenses and have options to categorize my expense, this should also work in similar way for income. for this MVP categories are initially provided and no way to modify them. Also, both expense and income must be linked into a specific account, enable 2 types of base account: cash & bank accounts, user will not be able to create new accounts for now. Use IDR as the currency. Also include a page where I can display the expenses per month ( each month started at date 1 ) and display total income and spending for the month across accounts."

## Clarifications

### Session 2025-10-12
- Q: What should happen if a user enters a zero or negative amount for an income or expense? → A: Block the entry and show an error message: "Amount must be greater than zero."
- Q: What should happen if the list of transactions for a month is very long? → A: Paginate the list, showing a fixed number of transactions per page (e.g., 50).
- Q: What should happen if a user enters a non-numeric value (e.g., "abc") in the amount field? → A: Prevent submission and display an error message like "Amount must be a valid number."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Record an Expense (Priority: P1)

As a user, I want to record a new expense so that I can track my spending.

**Why this priority**: This is the core functionality of the application. Without it, no other features have value.

**Independent Test**: Can be fully tested by adding an expense and verifying it is saved correctly. This delivers the primary value of tracking expenses.

**Acceptance Scenarios**:

1. **Given** I am on the "Add Expense" page, **When** I enter an amount, select a category, choose an account, and save, **Then** the expense is recorded and visible in my transaction history.
2. **Given** I am on the "Add Expense" page, **When** I try to save without entering an amount, **Then** I see an error message and the expense is not saved.

---

### User Story 2 - Record an Income (Priority: P1)

As a user, I want to record a new income so that I can track my earnings.

**Why this priority**: This is the counterpart to tracking expenses and is essential for a complete financial overview.

**Independent Test**: Can be fully tested by adding an income and verifying it is saved correctly. This delivers the primary value of tracking income.

**Acceptance Scenarios**:

1. **Given** I am on the "Add Income" page, **When** I enter an amount, select a category, choose an account, and save, **Then** the income is recorded and visible in my transaction history.
2. **Given** I am on the "Add Income" page, **When** I try to save without entering an amount, **Then** I see an error message and the income is not saved.

---

### User Story 3 - View Monthly Summary (Priority: P2)

As a user, I want to see a summary of my income and expenses for a selected month so that I can understand my financial activity.

**Why this priority**: This feature provides the main analytical value, allowing users to review their financial habits.

**Independent Test**: Can be tested by navigating to the monthly summary page and verifying that the correct totals for income and spending are displayed for the selected month.

**Acceptance Scenarios**:

1. **Given** I have recorded several incomes and expenses in the current month, **When** I navigate to the "Monthly Summary" page, **Then** I see the total income, total spending, and a list of transactions for that month.
2. **Given** there are no transactions for a specific month, **When** I view the summary for that month, **Then** the total income and spending are both displayed as zero.


### Edge Cases


- How does the system handle transactions on the last day of the month?


## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST allow users to record a new expense with an amount, category, and account.
- **FR-002**: The system MUST allow users to record a new income with an amount, category, and account.
- **FR-003**: The system MUST provide a pre-defined, non-modifiable list of categories for both income and expenses.
- **FR-004**: The system MUST provide two pre-defined, non-modifiable accounts: "Cash" and "Bank".
- **FR-005**: All transactions (income and expenses) MUST be recorded in IDR currency.
- **FR-006**: The system MUST display a monthly summary page showing total income, total spending, and a list of transactions for the selected month.
- **FR-007**: The monthly summary calculation MUST start from the 1st of each month.
- **FR-008**: The system MUST prevent users from recording transactions with a zero or negative amount and display an error message.
- **FR-009**: The system MUST paginate the list of transactions in the monthly summary, showing a maximum of 50 transactions per page.
- **FR-010**: The system MUST validate that the amount field for a transaction is a numeric value and display an error message if it is not.


### Key Entities *(include if feature involves data)*

- **Transaction**: Represents a single financial event. Attributes include: amount, date, type (income/expense), category, and account.
- **Category**: A label for a transaction. Pre-defined and cannot be changed by the user.
- **Account**: The source or destination of funds. Pre-defined as "Cash" or "Bank".

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can record a new expense or income in under 30 seconds.
- **SC-002**: The monthly summary page for a month with up to 1000 transactions loads in under 3 seconds.
- **SC-003**: 100% of recorded transactions are correctly reflected in the monthly summary.
- **SC-004**: The application can be used entirely offline in a local web browser.

## Assumptions

- **A-001**: No user authentication is required for this MVP. The application is for a single user on a local machine.
- **A-002**: The initial set of categories for expenses will be: Food, Transportation, Housing, Utilities, Entertainment.
- **A-003**: The initial set of categories for income will be: Salary, Gifts, Other.
- **A-004**: Data will be stored in a local SQLite database, managed by the Python backend. This ensures data persistence between sessions.