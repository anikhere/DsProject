from box import ConfigBox
import os 
import yaml
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from src.ds import logger
from box.exceptions import BoxValueError

@ensure_annotations
def Load_yaml(path_yaml: Path) -> ConfigBox:
    try:
        with open (path_yaml) as file:
            content=yaml.safe_load(file)
            logger.info('safely opened yaml',path_yaml)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
@ensure_annotations        
def create_dir(path_dirs:list,verbose=True):
    for path in path_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'created directory at: {path}')
@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path,'w') as file:
        json.dump(data,file,indent=4)

    logger.info(f'json file dumped success{path}')

@ensure_annotations
def Save(data:Any,path:Path):
    joblib.dump(value=data, filename=path)
    logger.info(f'binary file saved{path}')