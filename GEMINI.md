# spec-driven-development Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-12

## Active Technologies
- Python 3.12 + FastAPI (backend), Dash (frontend), SQLModel (database) (001-build-initial-app)

## Project Structure
```
backend/
├── src/
│   ├── database.py
│   ├── initial_data.py
│   ├── main.py
│   ├── models.py
│   ├── api/
│   │   ├── lookups.py
│   │   ├── summary.py
│   │   └── transactions.py
│   └── services/
│       ├── lookups.py
│       ├── summary.py
│       └── transactions.py
└── tests/
    ├── integration/
    │   └── test_api.py
    └── unit/
        ├── test_summary.py
        └── test_transactions.py
frontend/
└── src/
    ├── app.py
    ├── styles.py
    ├── callbacks/
    │   ├── summary_callbacks.py
    │   └── transaction_callbacks.py
    ├── components/
    │   └── navbar.py
    ├── pages/
    │   ├── summary.py
    │   └── transaction.py
    └── utils/
        └── api.py
```

## Commands

to run the backend:

```
uv run backend/src/main.py
```

to run the frontend:

```
uv run frontend/src/app.py
```

to run the tests:

```
uv run pytest
```

## Code Style
Python 3.12: Follow standard conventions

## Recent Changes
- 001-build-initial-app: Added Python 3.12 + FastAPI (backend), Dash (frontend), SQLModel (database)

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->