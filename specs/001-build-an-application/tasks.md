---
description: "Task list for implementing the Expense Tracker Application"
---

# Tasks: Expense Tracker Application

**Input**: Design documents from `/specs/001-build-an-application/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/openapi.yaml

**Tests**: Test tasks are included following a TDD approach, as testing is a stated priority in the project documentation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- **Backend**: `backend/src/`, `backend/tests/`
- **Frontend**: Served from `backend/src/static/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [ ] T001 Initialize project with `uv init` command and create project structure: `backend/src` and `backend/tests`.
- [ ] T002 add dependencies for `fastapi[standard]`, `SQLAlchemy`, `pytest`, and `ruff` using `uv add` command.
- [ ] T003 [P] Create a basic FastAPI app in `backend/src/main.py` that serves a placeholder "Hello World" at the root.
- [ ] T004 [P] Configure `ruff` by configuring `pyproject.toml` file with basic rules.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T006 [P] Define Pydantic schemas for all API entities (`Transaction`, `Category`, `Account`, `MonthlyReport`) in `backend/src/models/schemas.py` based on `openapi.yaml`.
- [ ] T007 [P] Define SQLAlchemy models for `Transaction`, `Category`, and `Account` in `backend/src/models/database.py` based on `data-model.md`.
- [ ] T008 Implement a database session utility in `backend/src/database.py` to handle SQLite connection and sessions.
- [ ] T009 Create a database initialization script `backend/src/init_db.py` that:
    - Creates the SQLite database and all tables from the SQLAlchemy models.
    - Seeds the two required `Account` records ("Cash", "Bank").
    - Seeds the default `Category` records listed in `spec.md`.
- [ ] T010 Run the `init_db.py` script to create the initial database `expense_tracker.db`.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Transaction Management (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to be able to record my income and expenses, so I can track my financial activities.

**Independent Test**: Add an expense and an income transaction via the UI and verify they are saved correctly by calling the API.

### Tests for User Story 1 ⚠️
**NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Write an integration test in `backend/tests/test_transactions.py` for `POST /transactions` to create a new transaction.
- [ ] T012 [P] [US1] Write an integration test in `backend/tests/test_transactions.py` for `GET /transactions/{year}/{month}`.
- [ ] T013 [P] [US1] Write an integration test in `backend/tests/test_accounts.py` for `GET /accounts`.

### Implementation for User Story 1

- [ ] T014 [P] [US1] Implement the service logic for accounts in `backend/src/services/account_service.py` to list all accounts.
- [ ] T015 [P] [US1] Implement the API endpoint `GET /accounts` in `backend/src/api/accounts.py`.
- [ ] T016 [US1] Implement the service logic for transactions in `backend/src/services/transaction_service.py` to create and list transactions. (Depends on T014)
- [ ] T017 [US1] Implement the API endpoints `POST /transactions` and `GET /transactions/{year}/{month}` in `backend/src/api/transactions.py`. (Depends on T016)
- [ ] T018 [US1] Create the main frontend page `backend/src/static/index.html`.
- [ ] T019 [US1] Add CSS to `backend/src/static/styles.css` for basic styling of the main page.
- [ ] T020 [US1] Add JavaScript to `index.html` to:
    - Fetch and display accounts and categories for the transaction form.
    - Handle form submission to `POST /transactions`.
    - Fetch and display a list of recent transactions.
- [ ] T021 [US1] Update `backend/src/main.py` to mount the `static` directory and include the API routers.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Category Management (Priority: P2)

**Goal**: As a user, I want to be able to create new categories for my income and expenses.

**Independent Test**: Create a new category via the UI, then navigate to the main page and verify it appears as an option in the transaction form.

### Tests for User Story 2 ⚠️

- [ ] T022 [P] [US2] Write an integration test in `backend/tests/test_categories.py` for `POST /categories`.
- [ ] T023 [P] [US2] Write an integration test in `backend/tests/test_categories.py` for `GET /categories`.

### Implementation for User Story 2

- [ ] T024 [US2] Implement the service logic in `backend/src/services/category_service.py` to create and list categories.
- [ ] T025 [US2] Implement the API endpoints `POST /categories` and `GET /categories` in `backend/src/api/categories.py`. (Depends on T024)
- [ ] T026 [P] [US2] Create the category management page `backend/src/static/categories.html`.
- [ ] T027 [P] [US2] Add a navigation link from `index.html` to `categories.html`.
- [ ] T028 [US2] Add JavaScript to `categories.html` to handle the form for creating new categories and display a list of existing ones.
- [ ] T029 [US2] Update the JavaScript in `index.html` to ensure the category dropdown is populated from the `GET /categories` endpoint.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Monthly Reporting (Priority: P2)

**Goal**: As a user, I want to see a summary of my income and expenses for each month.

**Independent Test**: Add several transactions for a specific month, navigate to the report page, and verify the total income and expense match the transactions.

### Tests for User Story 3 ⚠️

- [ ] T030 [US3] Write an integration test in `backend/tests/test_reports.py` for `GET /reports/monthly`.

### Implementation for User Story 3

- [ ] T031 [US3] Implement the service logic in `backend/src/services/report_service.py` to calculate total income and expenses for a given month and year.
- [ ] T032 [US3] Implement the API endpoint `GET /reports/monthly` in `backend/src/api/reports.py`. (Depends on T031)
- [ ] T033 [P] [US3] Create the monthly report page `backend/src/static/report.html`.
- [ ] T034 [P] [US3] Add a navigation link from `index.html` to `report.html`.
- [ ] T035 [US3] Add JavaScript to `report.html` to allow the user to select a month/year, fetch the data from the API, and display the report.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T036 [P] Enhance and unify CSS in `backend/src/static/styles.css` for all pages.
- [ ] T037 Add comprehensive error handling and user feedback on all forms.
- [ ] T038 [P] Manually perform end-to-end testing of all user stories.
- [ ] T039 [P] Update the main `README.md` with final setup and run instructions.
- [ ] T040 Code cleanup and refactoring based on `ruff` feedback and peer review.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** -> **Foundational (Phase 2)** -> **User Stories (Phases 3-5)** -> **Polish (Phase 6)**

### User Story Dependencies

- **US1, US2, US3**: All depend on Foundational (Phase 2) completion. They can be developed in parallel after Phase 2 is done.

### Within Each User Story

- **TDD Flow**: Tests first, then services, then API endpoints, then frontend.
- **Parallel Tasks**: Tasks marked `[P]` within a phase can be executed in parallel.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: The application can now record and display transactions. This is a deployable MVP.

### Incremental Delivery

1. Deliver MVP (US1).
2. Add User Story 2 (Category Management).
3. Add User Story 3 (Monthly Reporting).
4. Each story adds value without breaking previous stories.
