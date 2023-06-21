# This file is for the purpose of logging any events happening in the project, such as execution, errors, and exceptions, etc.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE) # add name 'logs' in the start of every log file
os.makedirs(logs_path,exist_ok=True) # exist_ok = True is making sure, even if there is file or folders keep  appending the files or folders
# line 8 is making directories based on logs_path


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) # joining the log path and current time(the time at which log files are creating)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
   # wherever we write logging.INFO, it is going to use this configuration. 
    )
    
