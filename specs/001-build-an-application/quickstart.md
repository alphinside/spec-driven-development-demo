# Quickstart Guide for Expense Tracker Application

This guide provides instructions on how to set up the development environment and run the application.

## Prerequisites

- Python 3.12
- `uv` (can be installed with `pip install uv`)

## Setup

1.  **Create a virtual environment:**

    ```bash
    uv venv
    ```

2.  **Activate the virtual environment:**

    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    uv pip install -r requirements.txt
    ```

    *(Note: The `requirements.txt` file will be created in a later step. For now, it will contain `fastapi`, `uvicorn`, `pytest`, and `sqlalchemy`)*

4.  **Initialize the database:**

    A script will be provided to initialize the SQLite database and create the necessary tables.

    ```bash
    python backend/src/init_db.py
    ```

## Running the Application

1.  **Start the backend server:**

    ```bash
    uvicorn backend.src.main:app --reload
    ```

2.  **Open the application in your browser:**

    Navigate to `http://127.0.0.1:8000`

## Running Tests

To run the unit and integration tests, use `pytest`:

```bash
pytest
```
