import os

def print_tree(directory, prefix="", ignored_dirs=None):
    """Recursively prints the hierarchy of files and folders, ignoring specified directories."""
    if ignored_dirs is None:
        ignored_dirs = []
    
    entries = sorted(os.listdir(directory))
    entries = [e for e in entries if e not in ignored_dirs]
    
    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        connector = "└── " if index == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "    " if index == len(entries) - 1 else "│   "
            print_tree(path, prefix + extension, ignored_dirs)

if __name__ == "__main__":
    ignored = ["__pycache__", ".git", ".idea", ".venv", "env", ".vscode", ".gitignore"]
    print("Структура проєкту:")
    print_tree(os.getcwd(), ignored_dirs=ignored)