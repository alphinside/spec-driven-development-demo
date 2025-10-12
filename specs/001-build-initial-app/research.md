# Research for Local Expense Organizer

This document outlines the decisions and best practices for the chosen technology stack.

## Decisions

- **Backend Framework**: FastAPI was chosen for its high performance, ease of use, and automatic OpenAPI documentation generation.
- **Frontend Framework**: Dash was chosen as it is a Python-based framework for building analytical web applications, which fits the requirements of this project. It allows for a full-stack Python application.
- **Database**: SQLite is used for its simplicity and serverless nature, making it ideal for a local, single-user application.
- **ORM**: SQLAlchemy will be used as the Object-Relational Mapper to interact with the SQLite database. It provides a robust and flexible way to manage the data model.
- **Project Management**: `uv` is used for its speed and all-in-one capabilities for managing Python projects.

## Best Practices

### FastAPI and Dash Integration

- **Serving Dash through FastAPI**: The Dash application will be served as a sub-application within FastAPI. This allows for a single server process to run both the backend API and the frontend application.
- **API Communication**: The Dash frontend will communicate with the FastAPI backend via HTTP requests to the API endpoints.

### Project Structure with `uv`

- A monorepo structure with `backend` and `frontend` directories will be used.
- Each directory will have its own `pyproject.toml` file to manage its dependencies using `uv`.
- A top-level `pyproject.toml` can be used to manage the overall project and run scripts.

### Data Modeling with SQLAlchemy

- The data model will be defined in `backend/src/models/` using SQLAlchemy's declarative base.
- Alembic can be used for database migrations if the schema evolves in the future, but for the MVP, we will create the tables directly from the models.