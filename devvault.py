# devvault.py
# An automated tool for setting up new Python project directories and virtual environments.
# Created by [Your Name/Alias]
# Date: [Current Date]

import sys
from pathlib import Path
import subprocess
import os
import shutil

# Helper function to create a file with specified content
def create_file(file_path, content=""):
    """Creates a file at the given path with optional content."""
    file_path.write_text(content)
    print(f"  - Created file: {file_path}")

# Helper function for cleaning up temporary files and directories
def run_cleanup(project_path):
    """Removes common temporary files and directories from a project."""
    print(f"\nStarting cleanup for project: {project_path.resolve()}...")

    # Directories to remove recursively
    cleanup_dirs = ['__pycache__', '.pytest_cache', '.mypy_cache', 'build', 'dist']
    # File extensions to remove
    cleanup_file_extensions = ['.pyc', '.bak', '.tmp']

    cleaned_items_count = 0

    for root, dirs, files in os.walk(project_path, topdown=True):
        for d in list(dirs):
            if d in cleanup_dirs:
                dir_to_remove = Path(root) / d
                try:
                    shutil.rmtree(dir_to_remove)
                    print(f"  Removed directory: {dir_to_remove}")
                    dirs.remove(d)
                    cleaned_items_count += 1
                except OSError as e:
                    print(f"  Error removing directory {dir_to_remove}: {e}")

        for f in files:
            if any(f.endswith(ext) for ext in cleanup_file_extensions):
                file_to_remove = Path(root) / f
                try:
                    os.remove(file_to_remove)
                    print(f"  Removed file: {file_to_remove}")
                    cleaned_items_count += 1
                except OSError as e:
                    print(f"  Error removing file {file_to_remove}: {e}")

    if cleaned_items_count == 0:
        print("No common temporary files or directories found for cleanup.")
    else:
        print(f"Cleanup complete. Removed {cleaned_items_count} items.")


def main():
    """Main function to orchestrate the project setup."""
    print("\n--- DevVault Project Setup ---")
    project_name = input("Enter the new project name: ").strip()

    if not project_name:
        print("Error: Project name cannot be empty. Exiting.")
        sys.exit(1)

    project_path = Path(project_name)

    print(f"Preparing to create project: '{project_name}' at '{project_path.resolve()}'")

    # --- Code for creating main directory and subdirectories ---
    try:
        project_path.mkdir(parents=True, exist_ok=False)
        print(f"\nSuccessfully created main project directory: {project_path.resolve()}")
    except FileExistsError:
        print(f"\nError: Directory '{project_name}' already exists at '{project_path.resolve()}'.")
        print("Please choose a different name or manually delete the existing one if you wish to proceed.")
        sys.exit(1)

    subdirs = ['src', 'tests', 'docs', 'data', 'notebooks', 'models', 'scripts']

    print("\nCreating standard subdirectories:")
    for subdir in subdirs:
        (project_path / subdir).mkdir(exist_ok=True)
        print(f"  - Created: {project_path / subdir}")

    # --- Code for creating essential files ---
    print("\nCreating essential project files:")

    # 1. Create README.md
    readme_content = f"""
# {project_name.replace('_', ' ').title()}

## Project Description

This is a new project created using DevVault, your automated project setup tool.

## Setup

1.  **Create and activate virtual environment:**
    ```bash
    python -m venv venv
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows (Command Prompt):
    .\\venv\\Scripts\\activate.bat
    # On Windows (PowerShell):
    .\\venv\\Scripts\\Activate.ps1
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

(Add your project's usage instructions here)

## Development

(Add notes for development, e.g., running tests, building docs)

## License

(Specify your project's license here)

"""
    create_file(project_path / 'README.md', readme_content.strip())

    # 2. Create requirements.txt (initially empty)
    create_file(project_path / 'requirements.txt')

    # 3. Create .gitignore
    gitignore_content = """
# Virtual environment
venv/
.venv/

# Python artifacts
__pycache__/
*.pyc
*.egg-info/
*.egg/
*.so
*.pyd
*.dist-info/

# IDE specific files
.idea/
.vscode/
*.iml

# Operating System files
.DS_Store
Thumbs.db

# Data files (often large or sensitive, should not be versioned)
data/
*.csv
*.json
*.parquet
*.pkl
*.sqlite
*.db

# Notebook outputs
*.ipynb_checkpoints/
.ipynb

# Logs
*.log
logs/

# Models (often large, should not be versioned directly)
models/

# Environment variables
.env
*.env

# Build artifacts
build/
dist/
"""
    create_file(project_path / '.gitignore', gitignore_content.strip())

    # 4. Create main entry point file (e.g., src/main.py)
    main_py_content = """
# src/main.py
# Main entry point for your project.

def run_project():
    print("Hello from your new DevVault project!")
    print("Start building your AI application here.")

if __name__ == "__main__":
    run_project()
"""
    create_file(project_path / 'src' / 'main.py', main_py_content.strip())

    # --- Code for virtual environment setup ---
    print("\nSetting up virtual environment...")
    venv_path = project_path / 'venv'

    try:
        subprocess.run([sys.executable, '-m', 'venv', str(venv_path)], check=True)
        print("Virtual environment created successfully.")

        if sys.platform.startswith('win'):
            print(f"  Activate with: .\\{project_name}\\venv\\Scripts\\activate.bat (Command Prompt)")
            print(f"  Or: .\\{project_name}\\venv\\Scripts\\Activate.ps1 (PowerShell)")
        else:
            print(f"  Activate with: source {project_name}/venv/bin/activate")

    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        print("Please ensure Python is correctly installed and accessible in your PATH.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'python' command not found. Ensure Python is installed and added to your system PATH.")
        sys.exit(1)

    # --- Code for installing initial dependencies ---
    install_deps_choice = input("\nDo you want to install common AI/ML dependencies (numpy, pandas, scikit-learn, requests, matplotlib)? (y/n): ").lower().strip()

    if install_deps_choice == 'y':
        # Removed 'jupyter' for testing. We can add it back later if other installs work.
        common_packages = ['numpy', 'pandas', 'scikit-learn', 'requests', 'matplotlib']
        print(f"Installing common dependencies: {', '.join(common_packages)}...")

        if sys.platform.startswith('win'):
            pip_executable = venv_path / 'Scripts' / 'pip.exe'
        else:
            pip_executable = venv_path / 'bin' / 'pip'

        try:
            # Added '-v' for verbose pip output, and stderr=subprocess.STDOUT to capture all messages
            subprocess.run([str(pip_executable), 'install', '-v', *common_packages], check=True, stderr=subprocess.STDOUT)
            print("Common dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing dependencies: {e}")
            if e.output:
                print(f"Subprocess Output (stderr/stdout combined):\n{e.output.decode('utf-8')}")
            print("Please activate the virtual environment manually and install dependencies.")
        except FileNotFoundError:
            print(f"Error: pip executable not found at {pip_executable}.")
            print("Please activate the virtual environment manually and install dependencies.")
    else:
        print("Skipping common dependency installation.")

    # --- Code for cleanup functionality ---
    print("\n--- DevVault Operations Complete ---")
    cleanup_choice = input("Do you want to run cleanup (remove common temporary files/folders like __pycache__)? (y/n): ").lower().strip()

    if cleanup_choice == 'y':
        final_confirm = input(f"Are you sure you want to clean up '{project_name}'? This will delete temporary files. (y/n): ").lower().strip()
        if final_confirm == 'y':
            run_cleanup(project_path)
        else:
            print("Cleanup cancelled.")
    else:
        print("Skipping cleanup.")

    print(f"\nDevVault setup for '{project_name}' is complete. Happy coding!")


if __name__ == "__main__":
    main()