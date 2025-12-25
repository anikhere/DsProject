import os 
import urllib.request as request
from src.ds import logger
import zipfile
from src.ds.entity.config_entity import (DataTrans)
from src.ds.config.configuration import ConfigManager
from src.ds.components.dt1 import actual_code 
from pathlib import Path

stage_name = "Data_transformation"

class DataTrans:
    def __init__(self):
        pass
    def _initiate_transformation(self):
       try:
           with open(Path('artifacts/data_validate/status.txt'),'r') as file:
                status= file.read().split(' ')[-1]
           if status==True:
              config= ConfigManager()
              datatc = config.get_data_transform()
              trans = actual_code(config=datatc)
              trans.Train_test()
           else:
               raise Exception("your scheme is not valid ")
       except Exception as e:
           raise e