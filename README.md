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

2.  **Run the tool:**
    ```bash
    python devvault.py
    ```
    Follow the prompts to enter your new project name, install dependencies, and optionally run cleanup.
