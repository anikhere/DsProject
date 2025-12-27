from dataclasses import dataclass
from pathlib import Path
import os 

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_dir: Path
    all_schema:dict

@dataclass
class DataTrans:
    root_dir: Path
    data_path: Path

@dataclass
class main_Train:
   root_dir:Path
   train_data_path:Path
   test_data_path:Path
   model_name:str
   alpha:float
   l1_ratio: float
   target:str

