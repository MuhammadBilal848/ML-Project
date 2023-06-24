# # This has all the common functionalities that we can use in the entire project can use

import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    ''' Function is responsible for saving file as pkl'''
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)


def evaluate_model(xtrain,ytrain,xtest,ytest,models,params):
    try: 
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            prm = params[list(models.keys())[i]]
            gsc = GridSearchCV(model,prm,cv = 3)

            gsc.fit(xtrain,ytrain)
            
            model.set_params(**gsc.best_params_)
            
            model.fit(xtrain,ytrain)

            y_train_pred = model.predict(xtrain)

            y_test_pred = model.predict(xtest)

            train_model_score = r2_score(ytrain,y_train_pred)

            test_model_score = r2_score(ytest,y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report

    except Exception as e:
        raise CustomException(e,sys)
