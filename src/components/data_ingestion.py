    # This is used for loading data and performing traintestsplit.

import sys
import os
import src
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformationConfig,DataTransformation
from src.components.model_trainer import ModelTrainerConfig,ModelTrainer

# dataclass decorator is used to define variables
@dataclass 
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_congif = DataIngestionConfig()

    def initiate_data_ingestion(self):
        ''' This function is responsible for reading data and performing train_test_split'''
        logging.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_path),exist_ok = True)
        # creates a folder name artifacts and create a file named train.csv, if it exist it should just overwrite it.

            df.to_csv(self.ingestion_congif.raw_data_path,index = False , header = True)

            logging.info('Train Test Split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state = 42)

            train_set.to_csv(self.ingestion_congif.train_data_path,index = False , header = True)
            # save the (xtrain,ytrain) as train.csv 

            test_set.to_csv(self.ingestion_congif.test_data_path,index = False , header = True)
            # save the (xtest,ytest) as test.csv

            logging.info('Data Ingestion is completed')

            return (self.ingestion_congif.train_data_path,
                    self.ingestion_congif.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == '__main__':
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr , test_arr , _ = data_transformation.initiate_data_transformation(train_data,test_data)


    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
