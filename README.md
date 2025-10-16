# Specification Driven Development Demo

This repository demonstrates the use of [`spec-kit`](https://github.com/github/spec-kit) with [Gemini CLI](https://github.com/google-gemini/gemini-cli) by building a simple expense tracker application.

## Workshop Challenges

Do the following prompt to test development in this repo to demonstrate using spec-kit and Gemini CLI in brownfield project

Specification: Show balance of each accounts below total expenses in summary page. Sorted alphabetically.

Technical Plan: Add "balance" field to the account domain, all transaction must be a database transaction to this balance field. Use current database implementation for this

## Project Structure

The project is organized into two main parts: a backend and a frontend.

```
/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   ├── services/
│   │   ├── database.py
│   │   ├── main.py
│   │   └── models.py
│   └── tests/
└── frontend/
    └── src/
        ├── callbacks/
        ├── components/
        ├── pages/
        ├── utils/
        └── app.py
```

### Backend

The `backend` directory contains a FastAPI application responsible for the business logic and data persistence.

- **`src/main.py`**: The main entry point for the FastAPI application.
- **`src/database.py`**: Manages the database connection and session.
- **`src/models.py`**: Defines the data models using SQLModel.
- **`src/api/`**: Contains the API endpoints for different resources:
    - `lookups.py`: Endpoints for retrieving categories and accounts.
    - `summary.py`: Endpoint for generating monthly summaries.
    - `transactions.py`: Endpoint for creating transactions.
- **`src/services/`**: Implements the business logic for each resource.
- **`tests/`**: Contains unit and integration tests for the backend.

### Frontend

The `frontend` directory contains a Dash application that provides the user interface for the expense tracker.

- **`src/app.py`**: The main entry point for the Dash application.
- **`src/pages/`**: Defines the layout for different pages of the application:
    - `transaction.py`: A page for adding new transactions.
    - `summary.py`: A page for viewing monthly summaries.
- **`src/components/`**: Contains reusable UI components.
- **`src/callbacks/`**: Manages the application's interactivity through callbacks.
- **`src/utils/`**: Includes utility functions, such as for making API requests to the backend.

## Technical Specifications

### Backend

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [SQLModel](https://sqlmodel.tiangolo.com/) for ORM and data validation, with SQLite as the database.
- **Testing**: [Pytest](https://docs.pytest.org/)
- **Linting/Formatting**: [Ruff](https://github.com/astral-sh/ruff)

### Frontend

- **Framework**: [Dash](https://dash.plotly.com/)
- **Component Library**: Dash Core Components and Dash HTML Components.

### Dependency Management

- **Package Manager**: [uv](https://github.com/astral-sh/uv) is used for dependency management and as a virtual environment manager.

## How to Run

Install the dependencies first

```bash
uv sync
```

### Backend

Run the development server:

```bash
uv run backend/src/main.py
```

### Frontend

Run the application:

```bash
uv run frontend/src/app.py
```
