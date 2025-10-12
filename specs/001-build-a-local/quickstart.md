# Quickstart Guide: Local Expense Organizer

This guide provides instructions on how to set up and run the application.

## Prerequisites

- Python 3.12
- `uv`

## Setup

1.  **Install Python 3.12**:
    ```bash
    uv python install 3.12
    ```

2.  **Create a virtual environment**:
    ```bash
    uv venv
    ```

3.  **Install dependencies for backend and frontend**:
    ```bash
    uv pip install -r backend/requirements.txt
    uv pip install -r frontend/requirements.txt
    ```
    *(Note: `requirements.txt` will be generated in the implementation phase)*

## Running the Application

1.  **Start the backend server**:
    ```bash
    uv run backend.main:app --reload
    ```

2.  **Start the frontend application**:
    In a separate terminal:
    ```bash
    uv run frontend/src/app.py
    ```

3.  **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8050`.