# spec-driven-development Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-12

## Active Technologies
- Python 3.12 + FastAPI, uvicorn (001-build-an-application)

## Project Structure
```
src/
tests/
```

## Commands
cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style
Python 3.12: Follow standard conventions

## Recent Changes
- 001-build-an-application: Added Python 3.12 + FastAPI, uvicorn

<!-- MANUAL ADDITIONS START -->
## `uv` guidelines

`uv` is a fast, all-in-one tool for managing Python projects, offering features from installing Python to managing dependencies and running scripts.

### Python Version Management

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

### Project and Environment Management

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

### Dependency Management (Projects)

-   **Add a dependency**:
    ```bash
    uv add <dependency>  # e.g., fastapi
    ```
-   **Remove a dependency**:
    ```bash
    uv remove <dependency>
    ```

### Dependency Management (Pip Interface)

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

### Running Scripts

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

### Utility Commands

-   **Clean `uv` cache entries**:
    ```bash
    uv cache clean
    ```
-   **Update `uv` to the latest version**:
    ```bash
    uv self update
    ```

## `ruff` guidelines

Ruff is a fast and powerful tool for linting and formatting Python code. It can replace multiple tools like Flake8, isort, and Black, providing a unified and efficient experience.

### Ruff Linter

The Ruff linter checks your code for errors, style issues, and other problems. It's incredibly fast and can be used as a drop-in replacement for many other linters.

#### Key Features

*   **Speed:** Extremely fast, written in Rust.
*   **Compatibility:** Drop-in replacement for Flake8, isort, pydocstyle, and more.
*   **Auto-fixing:** Can automatically fix many common issues.
*   **Configurability:** Highly configurable through `pyproject.toml` or `ruff.toml`.

#### Basic Usage

To run the linter on your project, use the following command:

```bash
ruff check .
```

To automatically fix issues, use:

```bash
ruff check . --fix
```

### Ruff Formatter

The Ruff formatter automatically formats your code to ensure a consistent style. It's designed to be a drop-in replacement for Black.

#### Key Features

*   **Speed:** Blazing fast, as it's part of the same Ruff toolchain.
*   **Black Compatibility:** Aims for near-identical output to Black.
*   **Configuration:** Offers some configuration options for line width, quote style, etc.

#### Basic Usage

To format your entire project, run:

```bash
ruff format .
```

### Combined Usage

You can use both the linter and formatter together to ensure your code is both correct and consistently styled. A common workflow is to first format the code and then run the linter.

```bash
ruff format . && ruff check . --fix
```

<!-- MANUAL ADDITIONS END -->