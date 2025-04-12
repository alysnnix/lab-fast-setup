# A simple setup for fastAPI application 🐍 

### Management Tools 🛠️

*   **pyenv**: Our trusty assistant for managing multiple Python versions on the same system. Allows easy installation and switching between different versions, like disguises for different cases.
*   **pipx**: Installs and runs Python command-line tools in isolated environments, keeping our crime scene clean of dependency conflicts.
*   **poetry**: The mastermind of the operation, managing project dependencies and virtual environments. Simplifies declaring, installing, and updating packages, organizing our clues.
*   **ignr (optional)**: A tool for generating `.gitignore` files, ensuring we don't accidentally include sensitive or unnecessary files in our version control. It's like a bouncer at the door, checking IDs and keeping unwanted guests out.

### Project Tools 🔍

*   **ruff**: An extremely fast Python linter and code formatter, written in Rust. Helps maintain code quality and consistency, like a magnifying glass over every line.
*   **pytest**: A robust and easy-to-use testing framework for Python, essential for verifying our code alibis.
*   **pytest-cov**: A pytest plugin that measures code coverage of tests, ensuring no clues are left behind.
*   **taskipy**: A task runner that allows defining and running custom scripts defined in the `pyproject.toml` file, our notebook for frequent commands.

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
    Poetry will read the [`pyproject.toml`](pyproject.toml) file and install the necessary dependencies in a virtual environment managed by it. It's elementary!
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