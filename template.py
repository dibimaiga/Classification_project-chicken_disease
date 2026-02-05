import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "Chicken_disease_classification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

    ]

for file_path in list_of_files:
    filepath = Path(file_path) #to make it a windows path (windows works with backward slash)
    #to separate folder from files so we can store one by one
    filedir,filename = os.path.split(filepath) #(my file directory or my folder, my file inside it)

    if filedir != "": # if it's not empty, I had to create it
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0): #si le chemin n'existe pzs ou qu'il est vide
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file {file_path}")
    
    else:
        logging.info(f"{filename} already exists")
        

