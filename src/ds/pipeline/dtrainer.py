import os 
import urllib.request as request
from src.ds import logger
import zipfile
from src.ds.entity.config_entity import (main_Train)
from src.ds.config.configuration import ConfigManager
from src.ds.components.trainer import Model_trainer,main_Train 
from pathlib import Path

stage_name= "Training stage"

class Model_trainer:
    def __init__(self):
        pass
    def ini_train(self):
        config = ConfigManager()
        mct = config.get_trainer()
        mt = Model_trainer(config=mct)
        mt.train()
        print("✅ Training completed successfully!")