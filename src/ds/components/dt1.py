import os
from pathlib import Path
import sys
from sklearn.model_selection import train_test_split
import pandas as pd
from src.ds import logger
from src.ds.entity.config_entity import DataTrans
from dataclasses import dataclass

class actual_code:
    def __init__(self,config: DataTrans):
        self.config = config
    
    def Train_test(self):
        data = pd.read_csv(self.config.data_path)
        train,test= train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info('splitted data')
        logger.info(train.shape)
        logger.info(test.shape)
        