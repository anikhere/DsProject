import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

proj_name="ds"
list_files= [
    '.github/workflows/.gitkeep',
    f'src/{proj_name}/__init__.py',
    f'src/{proj_name}/components/__init__.py',
    f'src/{proj_name}/utils/__init__.py',
    f'src/{proj_name}/utlis/common.py',
    f'src/{proj_name}/config/__init__.py',
    f'src/{proj_name}/config/configuration.py',
    f'src/{proj_name}/pipeline/__init__.py',
    f'src/{proj_name}/entity/__init__.py',
    f'src/{proj_name}/entity/config_entity.py',
    f'src/{proj_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"

]
for files in list_files:
    file_path= Path(files)
    filedir,filename=os.path.split(file_path)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating a directory for {filedir}')
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as file:
            pass
            logging.info(f'creating empty file: {file_path}')
        
    else:
        logging.info(f'already exists{file_path}')





