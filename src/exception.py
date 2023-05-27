import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tab=error_detail.exc_info()
    file_name=exc_tab.tb_frame.f_code.co_filename
    error_message=f"Error message occured in python script name : {file_name} line number : {exc_tab.tb_lineno} error message : {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,erroe_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=erroe_detail)
    def __str__(self) :
        return self.error_message
