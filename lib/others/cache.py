import os
import shutil

def remove_pycache(directory="."):
    for root, dirs, _ in os.walk(directory):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"))

remove_pycache()  # Call the function
