from datetime import datetime

class TaskUnit():
    def __init__(self, task, d=1, m=1, y=2100):
        # Parameters:
        #   task: string
        # Side effects:
        #   Initiates self.task
        self.task = task
        self.complete = False
        self.due_date = datetime(y, m, d)
        # datetime object will sort by this attribute
        self.due_date_formatted = self.due_date.strftime("%d/%m/%Y")
        # this is a string for displaying later
        if self.due_date == datetime(2100, 1, 1):
            self.due_date_formatted == None

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





    

