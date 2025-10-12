# Using Ruff for Linting and Formatting

Ruff is a fast and powerful tool for linting and formatting Python code. It can replace multiple tools like Flake8, isort, and Black, providing a unified and efficient experience.

## Ruff Linter

The Ruff linter checks your code for errors, style issues, and other problems. It's incredibly fast and can be used as a drop-in replacement for many other linters.

### Key Features

*   **Speed:** Extremely fast, written in Rust.
*   **Compatibility:** Drop-in replacement for Flake8, isort, pydocstyle, and more.
*   **Auto-fixing:** Can automatically fix many common issues.
*   **Configurability:** Highly configurable through `pyproject.toml` or `ruff.toml`.

### Basic Usage

To run the linter on your project, use the following command:

```bash
ruff check .
```

To automatically fix issues, use:

```bash
ruff check . --fix
```

## Ruff Formatter

The Ruff formatter automatically formats your code to ensure a consistent style. It's designed to be a drop-in replacement for Black.

### Key Features

*   **Speed:** Blazing fast, as it's part of the same Ruff toolchain.
*   **Black Compatibility:** Aims for near-identical output to Black.
*   **Configuration:** Offers some configuration options for line width, quote style, etc.

### Basic Usage

To format your entire project, run:

```bash
ruff format .
```

## Combined Usage

You can use both the linter and formatter together to ensure your code is both correct and consistently styled. A common workflow is to first format the code and then run the linter.

```bash
ruff format . && ruff check . --fix
```
