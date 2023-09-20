from datetime import datetime

class TaskUnit():
    def __init__(self, task, d=1, m=1, y=2100) -> None:
        # Parameters:
        #   task: string
        # Side effects:
        #   Initiates self.task
        
        #Catch error for no input for task
        
        
        self.task = task
        if self.task == "":
            raise Exception("No input for task")
        if type(d) != int or type(m) != int or type(y) != int:
            raise Exception("Date should be integer.")
        
        self.complete = False
        self.due_date = datetime(y, m, d)
        # datetime object will sort by this attribute
        self.due_date_formatted = self.due_date.strftime("%d/%m/%Y")
        # this is a string for displaying later
        if self.due_date == datetime(2100, 1, 1):
            self.due_date_formatted = None

    def mark_complete(self):
        # Parameters: none
        # Side effects:
        #   Changes self.complete to True
        #  returns: none
        self.complete = True

    def mark_incomplete(self):
        # Parameters: none
        # Side effects:
        #   Changes self.complete to False
        #  returns: none
        self.complete = False
