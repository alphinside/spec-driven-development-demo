# Tasks: Local Expense Organizer

**Input**: Design documents from `/specs/001-build-a-local/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as required by the constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- Web app: `backend/src/`, `frontend/src/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure (`backend`, `frontend` directories).
- [x] T002 [P] Initialize `uv` project in `backend` and `frontend` directories.
- [x] T003 [P] Create `pyproject.toml` for `backend` with dependencies: `fastapi`, `uvicorn`, `sqlalchemy`, `pytest`.
- [x] T004 [P] Create `pyproject.toml` for `frontend` with dependencies: `dash`, `requests`.
- [x] T005 [P] Configure `ruff` for linting and formatting in both `backend` and `frontend`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 [US1, US2, US3] Implement database setup in `backend/src/database.py` to connect to the SQLite database.
- [x] T007 [US1, US2, US3] Create base SQLAlchemy models for `Transaction`, `Category`, and `Account` in `backend/src/models.py`.
- [x] T008 [US1, US2, US3] Create a script to initialize the database and populate initial data for `Category` and `Account` tables.
- [x] T009 [US1, US2, US3] Set up the basic FastAPI application in `backend/src/main.py`.
- [x] T010 [US1, US2, US3] Set up the basic Dash application in `frontend/src/app.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Record an Expense (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to record a new expense so that I can track my spending.

**Independent Test**: Can be fully tested by adding an expense and verifying it is saved correctly.

### Tests for User Story 1

- [x] T011 [P] [US1] Create unit test for the transaction creation service in `backend/tests/unit/test_transactions.py`.
- [x] T012 [P] [US1] Create integration test for the `POST /transactions` endpoint in `backend/tests/integration/test_api.py`.

### Implementation for User Story 1

- [x] T013 [US1] Create a Pydantic schema for transaction creation in `backend/src/schemas.py`.
- [x] T014 [US1] Implement the service logic for creating an expense in `backend/src/services/transactions.py`.
- [x] T015 [US1] Implement the `POST /transactions` endpoint in `backend/src/api/transactions.py`.
- [x] T016 [P] [US1] Create the "Add Expense" form component in `frontend/src/components/expense_form.py`.
- [x] T017 [US1] Create the main application layout in `frontend/src/app.py` to include the expense form.
- [x] T018 [US1] Implement the callback logic in `frontend/src/app.py` to handle form submission and call the backend API.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Record an Income (Priority: P1)

**Goal**: As a user, I want to record a new income so that I can track my earnings.

**Independent Test**: Can be fully tested by adding an income and verifying it is saved correctly.

### Tests for User Story 2

- [x] T019 [P] [US2] Update integration test for `POST /transactions` to cover income creation in `backend/tests/integration/test_api.py`.

### Implementation for User Story 2

- [x] T020 [US2] Update the service logic in `backend/src/services/transactions.py` to handle income creation (if different from expense).
- [x] T021 [P] [US2] Create the "Add Income" form component in `frontend/src/components/income_form.py`.
- [x] T022 [US2] Add the income form to the main application layout in `frontend/src/app.py`.
- [x] T023 [US2] Implement the callback logic in `frontend/src/app.py` for the income form.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - View Monthly Summary (Priority: P2)

**Goal**: As a user, I want to see a summary of my income and expenses for a selected month so that I can understand my financial activity.

**Independent Test**: Can be tested by navigating to the monthly summary page and verifying that the correct totals for income and spending are displayed for the selected month.

### Tests for User Story 3

- [x] T024 [P] [US3] Create unit test for the summary service in `backend/tests/unit/test_summary.py`.
- [x] T025 [P] [US3] Create integration test for the `GET /summary/{year}/{month}` endpoint in `backend/tests/integration/test_api.py`.

### Implementation for User Story 3

- [x] T026 [US3] Implement the service logic for calculating the monthly summary in `backend/src/services/summary.py`.
- [x] T027 [US3] Implement the `GET /summary/{year}/{month}` endpoint in `backend/src/api/summary.py`.
- [x] T028 [P] [US3] Create a component to display the summary and transaction list in `frontend/src/components/summary_display.py`.
- [x] T029 [US3] Add the summary display to the main application layout in `frontend/src/app.py`.
- [x] T030 [US3] Implement the callback logic in `frontend/src/app.py` to fetch and display the summary data, including pagination.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T031 [P] Add clear error messages and user feedback for API and UI interactions.
- [x] T032 [P] Apply consistent styling to all frontend components.
- [x] T033 [P] Review and add logging for important events.
- [x] T034 Create a performance test script to verify that the monthly summary for 1000 transactions loads in under 3 seconds.
- [x] T035 Run `quickstart.md` validation to ensure setup and execution steps are correct.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion.
- **User Stories (Phase 3-5)**: Depend on Foundational phase completion.
- **Polish (Phase 6)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2).
- **User Story 2 (P1)**: Can start after Foundational (Phase 2).
- **User Story 3 (P2)**: Can start after Foundational (Phase 2).

### Parallel Opportunities

- Once the Foundational phase is complete, work on all user stories can begin in parallel.
- Within each story, tasks marked with `[P]` can be worked on in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. **STOP and VALIDATE**: Test recording income and expenses independently.

### Incremental Delivery

1. Complete Setup + Foundational.
2. Add User Story 1 & 2.
3. Add User Story 3.
4. Each story adds value without breaking previous stories.