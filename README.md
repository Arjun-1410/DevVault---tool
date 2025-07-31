# DevVault - Automated Python Project Setup Tool

DevVault is a simple Command Line Interface (CLI) tool written in Python to automate the setup of new Python project directories. 
It quickly creates a standard folder structure, sets up a virtual environment, generates essential files (like `README.md`, `requirements.txt`, `.gitignore`), 
and can optionally install common development dependencies.

## Features

-   **Project Structure:** Creates `src`, `tests`, `docs`, `data`, `notebooks`, `models`, `scripts` directories.
-   **Virtual Environment:** Sets up a Python `venv` for isolated dependencies.
-   **Essential Files:** Generates `README.md`, `requirements.txt`, `.gitignore`, and `src/main.py` with boilerplate.
-   **Dependency Installation:** Optionally installs common AI/ML libraries (NumPy, Pandas, Scikit-learn, Requests, Matplotlib).
-   **Cleanup:** Can remove common temporary Python files (`__pycache__`, `.pyc`).

## How to Use

1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/Arjun-1410/DevVault---tool.git](https://github.com/Arjun-1410/DevVault---tool.git)
    cd DevVault---tool
    ```
    *(Note: Replace `Arjun-1410` with your actual GitHub username if it's different.)*

    *(Note: The actual output may vary slightly based on your system and Python version.)*

2.  **Run the tool:**
    ```bash
    python devvault.py
    ```
    Follow the prompts to enter your new project name, install dependencies, and optionally run cleanup.

## Example Output

--- DevVault Project Setup ---
Enter the new project name: my_new_ai_project
Preparing to create project: 'my_new_ai_project' at 'C:\Users...\my_new_ai_project'

Successfully created main project directory: C:\Users...\my_new_ai_project

Creating standard subdirectories:

Created: my_new_ai_project\src

Created: my_new_ai_project\tests

Created: my_new_ai_project\docs

Created: my_new_ai_project\data

Created: my_new_ai_project\notebooks

Created: my_new_ai_project\models

Created: my_new_ai_project\scripts

Creating essential project files:

Created file: my_new_ai_project\README.md

Created file: my_new_ai_project\requirements.txt

Created file: my_new_ai_project.gitignore

Created file: my_new_ai_project\src\main.py

Setting up virtual environment...
Virtual environment created successfully.
Activate with: .\my_new_ai_project\venv\Scripts\activate.bat (Command Prompt)
Or: .\my_new_ai_project\venv\Scripts\Activate.ps1 (PowerShell)

Do you want to install common AI/ML dependencies (...)? (y/n): y
Installing common dependencies: numpy, pandas, scikit-learn, requests, matplotlib...
... (pip installation output) ...
Common dependencies installed successfully.

--- DevVault Operations Complete ---
Do you want to run cleanup (...)? (y/n): n
Skipping cleanup.

DevVault setup for 'my_new_ai_project' is complete. Happy coding!


*(Note: The actual output may vary slightly based on your system and Python version.)*

## Development

This tool is a single Python script. Contributions are welcome!

## License

This project is open-source under the MIT License.
