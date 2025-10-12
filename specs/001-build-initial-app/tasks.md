# Tasks for Local Expense Organizer

**Feature**: `001-build-initial-app`

This document outlines the tasks required to implement the Local Expense Organizer feature.

## Phase 1: Setup

These tasks initialize the project structure and must be completed before any other phase.

- **T001**: [Setup] Initialize the `backend` FastAPI application structure in `backend/`.
- **T002**: [Setup] Initialize the `frontend` Dash application structure in `frontend/`.
- **T003**: [Setup] Configure `uv` for both `backend` and `frontend` projects.
- **T004**: [Setup] Configure `ruff` for the entire project.

## Phase 2: Foundational Tasks

These are blocking prerequisites that must be completed before any user story can be implemented.

- **T005**: [Backend] [Database] Create the database connection and session management in `backend/src/database.py`.
- **T006**: [Backend] [Models] Define the `Transaction`, `Category`, and `Account` models in `backend/src/models.py` using SQLAlchemy.
- **T007**: [Backend] [Database] Create a script `backend/src/initial_data.py` to populate the database with initial categories and accounts.
- **T008**: [Backend] [Main] Modify `backend/src/main.py` to create the database and tables on startup and run the initial data script.
- **T009**: [Backend] [Service] Create a `lookups` service in `backend/src/services/lookups.py` with functions to get categories and accounts.
- **T010**: [Backend] [API] Implement the `GET /categories/{type}` and `GET /accounts` endpoints in `backend/src/api/lookups.py`.
- **T011**: [Backend] [Main] Modify `backend/src/main.py` to include the lookups router.
- **T012**: [Frontend] [API] Create an API service module in `frontend/src/utils/api.py` to fetch data from the backend, including categories by type and accounts.

## Phase 3: User Story 1 - Record an Expense (P1)

**Goal**: As a user, I want to record a new expense so that I can track my spending.
**Independent Test**: Can be fully tested by adding an expense and verifying it is saved correctly.

- **T013**: [US1] [Backend] [Service] Create a `transactions` service in `backend/src/services/transactions.py` with a function to create a transaction.
- **T014**: [US1] [Backend] [API] Implement the `POST /transactions` endpoint in `backend/src/api/transactions.py` to record a new expense.
- **T015**: [US1] [Frontend] [Page] Create the "Add Expense" page layout in `frontend/src/pages/transaction.py`.
- **T016**: [US1] [Frontend] [Page] Implement the transaction form UI within the "Add Expense" page in `frontend/src/pages/transaction.py`.
- **T017**: [US1] [Frontend] [Callback] Implement callbacks in `frontend/src/callbacks/transaction_callbacks.py` to dynamically populate category and account dropdowns.
- **T018**: [US1] [Frontend] [Callback] Implement the callback in `frontend/src/callbacks/transaction_callbacks.py` to handle the form submission and call the backend API.

---
**CHECKPOINT**: User Story 1 (Record Expense) is complete and independently testable.
---

## Phase 4: User Story 2 - Record an Income (P1)

**Goal**: As a user, I want to record a new income so that I can track my earnings.
**Independent Test**: Can be fully tested by adding an income and verifying it is saved correctly.

- **T019**: [US2] [Backend] The backend implementation from US1 already supports creating income transactions. No new backend tasks are required.
- **T020**: [US2] [Frontend] [Page] Create the "Add Income" page in `frontend/src/pages/transaction.py` (or reuse the existing page with a parameter).
- **T021**: [US2] [Frontend] [Component] Reuse the form component from US1 for entering income details.
- **T022**: [US2] [Frontend] [Callback] Implement the callback in `frontend/src/callbacks/transaction_callbacks.py` to handle the form submission for income.

---
**CHECKPOINT**: User Story 2 (Record Income) is complete and independently testable.
---

## Phase 5: User Story 3 - View Monthly Summary (P2)

**Goal**: As a user, I want to see a summary of my income and expenses for a selected month.
**Independent Test**: Can be tested by navigating to the monthly summary page and verifying the correct totals.

- **T023**: [US3] [Backend] [Service] Create a `summary` service in `backend/src/services/summary.py` to calculate the monthly summary.
- **T024**: [US3] [Backend] [API] Implement the `GET /summary/{year}/{month}` endpoint in `backend/src/api/summary.py`.
- **T025**: [US3] [Frontend] [Page] Create the "Monthly Summary" page in `frontend/src/pages/summary.py`.
- **T026**: [US3] [Frontend] [Callback] Implement the callback in `frontend/src/callbacks/summary_callbacks.py` to fetch and display the monthly summary.

---
**CHECKPOINT**: User Story 3 (View Monthly Summary) is complete and independently testable.
---

## Phase 6: Polish & Integration

- **T027**: [Frontend] Create a navigation bar in `frontend/src/components/navbar.py` to switch between pages.
- **T028**: [Frontend] Integrate the navbar into the main app layout in `frontend/src/app.py`.
- **T029**: [Docs] Update `README.md` files for both `backend` and `frontend` with setup and run instructions.

## Dependencies

```
      +----------------+
      |     Setup      |
      | (T001 - T004)  |
      +----------------+
              |
              v
+---------------------------+
|   Foundational Tasks      |
|   (T005 - T012)           |
+---------------------------+
              |
+-------------v-------------+
| US1: Record Expense (P1)  |
| (T013 - T018)             |
+---------------------------+
              |
+-------------v-------------+
|  US2: Record Income (P1)  |
|  (T019 - T022)            |
+---------------------------+
              |
+-------------v-------------+
| US3: View Summary (P2)    |
| (T023 - T026)             |
+---------------------------+
              |
              v
  +-----------------------+
  |  Polish & Integration |
  |  (T027 - T029)        |
  +-----------------------+
```

## Parallel Execution Examples

- **Foundational**: T010 can be done in parallel.
- **US1**: T013, T015 can be started in parallel. T014 depends on T013. T016 depends on T015. T017 and T018 depend on T014 and T016.
- **US3**: T023 and T025 can be started in parallel. T024 depends on T023. T026 depends on T024 and T025.

## Implementation Strategy

The implementation will follow an MVP-first approach. We will deliver the user stories in priority order, ensuring that each user story is independently testable.

- **MVP**: User Story 1 (Record Expense).
- **Post-MVP**: User Story 2 (Record Income) and User Story 3 (View Monthly Summary).
