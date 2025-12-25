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
