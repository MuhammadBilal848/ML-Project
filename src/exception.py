# handles all the exceptions that arise on runtime
# whenever we get an exeption , the code will take it to logger.py and make directories on the exceptions 
# using logging.info


import sys
import logging

# we want to show our own custom message when an error is raised.
# error_detail:sys means error should in sys library.
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # exc_tb tells on which file and on which line number the exception occured 
    error_message = f'Error occured in python script name {file_name} line number {exc_tb.tb_lineno} error message {str(error)}'

    return error_message

class CustomException(Exception):
    def __init__(self,error,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
