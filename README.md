# A simple setup for fastAPI application 🐍 

### Management Tools 🛠️

*   **pyenv**: Our trusty assistant for managing multiple Python versions on the same system. Allows easy installation and switching between different versions.
*   **pipx**: Installs and runs Python command-line tools in isolated environments.
*   **poetry**: The mastermind of the operation, managing project dependencies and virtual environments. Simplifies declaring, installing, and updating packages.

### Project Tools 🔍

*   **ruff**: An extremely fast Python linter and code formatter, written in Rust. Helps maintain code quality and consistency.
*   **pytest**: A robust and easy-to-use testing framework for Python.
*   **pytest-cov**: A pytest plugin that measures code coverage of tests.
*   **taskipy**: A task runner that allows defining and running custom scripts defined in the `pyproject.toml` file.

### Setup Steps 👣

1.  **Install the correct Python version using pyenv:**
    ```bash
    pyenv install 3.12
    pyenv local 3.12
    ```

2.  **Install poetry using pipx:**
    ```bash
    pipx install poetry
    ```

3.  **Install project dependencies using poetry:**
    ```bash
    poetry install --with dev
    ```
    Poetry automatically creates and manages the virtual environment. To activate it manually (if necessary):
    ```bash
    poetry shell
    ```

4. **Dont forget to set your name and email**
    Set your name and email in the `pyproject.toml` file. This is important for commit history and package metadata.

5.  **Verify the installation and run tasks:**
    Use `taskipy` to run the tasks defined in [`pyproject.toml`](pyproject.toml):
    *   Run the application: `task run` ▶️
    *   Run the tests: `task test` ✅
    *   Check formatting and linting: `task lint` ✨
    *   Format the code: `task format` 🎨