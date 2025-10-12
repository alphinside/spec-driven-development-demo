# `uv` Usage Guidelines

`uv` is a fast, all-in-one tool for managing Python projects, offering features from installing Python to managing dependencies and running scripts.

## Python Version Management

`uv` can install and manage Python versions directly.

-   **Install a Python version**:
    ```bash
    uv python install <version>  # e.g., 3.12
    ```
-   **View installed Python versions**:
    ```bash
    uv python list
    ```
-   **Pin the current project to a specific Python version**:
    ```bash
    uv python pin
    ```
-   **Uninstall a Python version**:
    ```bash
    uv python uninstall
    ```

## Project and Environment Management

`uv` simplifies working with Python projects, typically those with a `pyproject.toml` file.

-   **Initialize a new project**:
    ```bash
    uv init
    ```
-   **Create a virtual environment**:
    ```bash
    uv venv
    ```
-   **Sync project dependencies**:
    ```bash
    uv sync
    ```
-   **Create a lockfile for dependencies**:
    ```bash
    uv lock
    ```
-   **Run a command within the project environment**:
    ```bash
    uv run <command>
    ```
-   **View the dependency tree**:
    ```bash
    uv tree
    ```

## Dependency Management (Projects)

-   **Add a dependency**:
    ```bash
    uv add <dependency>  # e.g., fastapi
    ```
-   **Remove a dependency**:
    ```bash
    uv remove <dependency>
    ```

## Dependency Management (Pip Interface)

For more granular control or legacy workflows, `uv` provides a `pip`-like interface.

-   **Install packages into the current environment**:
    ```bash
    uv pip install <package>
    ```
-   **Show details about an installed package**:
    ```bash
    uv pip show <package>
    ```
-   **List installed packages**:
    ```bash
    uv pip list
    ```
-   **Uninstall packages**:
    ```bash
    uv pip uninstall <package>
    ```
-   **Compile requirements into a lockfile**:
    ```bash
    uv pip compile
    ```
-   **Sync an environment with a lockfile**:
    ```bash
    uv pip sync
    ```

## Running Scripts

-   **Execute a standalone Python script**:
    ```bash
    uv run <script_name>.py
    ```
-   **Add a dependency to a script**:
    ```bash
    uv add --script <dependency>
    ```
-   **Remove a dependency from a script**:
    ```bash
    uv remove --script <dependency>
    ```

## Utility Commands

-   **Clean `uv` cache entries**:
    ```bash
    uv cache clean
    ```
-   **Update `uv` to the latest version**:
    ```bash
    uv self update
    ```
