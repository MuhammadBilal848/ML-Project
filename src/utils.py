# # This has all the common functionalities that we can use in the entire project can use

import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException

def save_object(file_path,obj):
    ''' Function is responsible for saving file as pkl'''
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
