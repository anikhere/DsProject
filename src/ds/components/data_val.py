import os 
import pandas as pd
from src.ds import logger
import zipfile
from src.ds.entity.config_entity import (DataValidationConfig)

class DataVal:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    
    def val_all_col(self)-> bool:
        try:
            val_status = None
            
            data = pd.read_csv(self.config.unzip_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    val_status = False
                    with open(self.config.STATUS_FILE,'w') as file:
                        file.write(f"Validation Status{val_status}")
                else:
                    val_status= True
                    with open(self.config.STATUS_FILE,'w') as file:
                        file.write(f"Validation Status{val_status}")
            return val_status
        except Exception as e :
            raise e 