import pandas as pd 
import os 
import joblib
from sklearn.linear_model import ElasticNet
from src.ds.entity.config_entity import main_Train




class Model_trainer:
    def __init__(self,config:main_Train):
        self.config= config

    def train(self):
        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)

        X_train= train.drop([self.config.target],axis=1)
        X_test = test.drop([self.config.target],axis=1)
        y_train = train[self.config.target]
        y_test= test[self.config.target]

        lr= ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio,random_state=42)
        lr.fit(X_train,y_train)
        prediction= lr.predict(X_test)
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))
        return prediction
    
        
