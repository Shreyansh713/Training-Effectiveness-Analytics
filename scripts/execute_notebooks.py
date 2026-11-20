import nbformat
from nbclient import NotebookClient
import os

notebooks = [
    "notebooks/01_cleaning.ipynb",
    "notebooks/02_eda.ipynb",
    "notebooks/03_insights.ipynb"
]

for nb_path in notebooks:
    print(f"Executing {nb_path}...")
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    client = NotebookClient(nb, timeout=600, kernel_name="python3")
    client.execute()
    
    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Successfully executed and saved: {nb_path}")

print("All notebooks executed with full cell outputs!")
