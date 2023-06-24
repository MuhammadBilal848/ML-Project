import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    # path is needed if we want to save model
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        ''' This function is responsible for creating data pipelines'''
        try: 
            numerical_col = ['writing_score','reading_score']
            categorical_col = [
                    'gender',
                    'race_ethnicity',
                    'parental_level_of_education',
                    'lunch',
                    'test_preparation_course'
                              ] 

            num_pipeline = Pipeline(
            steps = [
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                    ])

            cat_pipeline = Pipeline(
                steps= [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ohe',OneHotEncoder(handle_unknown="ignore")),
                    ("scaler",StandardScaler(with_mean=False))  
                ])

            logging.info('Numericals columns imputing and standard scaling done!')

            logging.info('Categorical columns imputing and one hot encoding and standard scaling done!')

            proprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_col),
                ('cat_pipeline',cat_pipeline,categorical_col), 
            ])

            return proprocessor

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try: 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('Readind train and test completed')

            logging.info('Obtaining preprocessing object')

            preprocessor_ob = self.get_data_transformer_object() 

            target_column_name = 'math_score'
            numerical_col = ['writing_score','reading_score']

            input_feature_train_df = train_df.drop(target_column_name,axis = 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(target_column_name,axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info('Applying preprocesing object on training and testing dataframes')

            input_feature_train_arr = preprocessor_ob.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_ob.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr , np.array(target_feature_train_df)] # works as concatenation on axis 1
            test_arr = np.c_[input_feature_test_arr , np.array(target_feature_test_df)] # works as concatenation on axis 1

            logging.info('Saved Preprocessing object')

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path, 
                obj = preprocessor_ob
            )

            return (train_arr, test_arr , self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e:
            raise CustomException(e,sys)
