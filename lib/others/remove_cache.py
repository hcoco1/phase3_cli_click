import os
import shutil

def remove_pycache(directory="."):
    """
    Remove all __pycache__ directories recursively starting from the given directory.
    """
    for root, dirs, _ in os.walk(directory):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"Removed: {pycache_path}")
            except Exception as e:
                print(f"Error removing {pycache_path}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path (default is current directory): ").strip()
    directory = directory if directory else "."
    remove_pycache(directory)
