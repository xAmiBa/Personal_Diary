'''
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
'''

from datetime import datetime
from TaskUnit import TaskUnit


class TaskList():
    def __init__(self) -> None:
        self.all_tasks = []  # all TaksUnit objects
    
    def add(self, task):
        self.task = task  # TaskUnit object
        self.all_tasks.append(task)
        pass

    def view_all(self):
        # catches empty task list error
        if self.all_tasks == []:
            raise Exception("Task list empty!")
        
        # task view list contains task, "due on" string and date formatted
        tasks_view = [f"{item.task} due on {str(item.due_date_formatted)}\n" for item in self.all_tasks]
        return "".join(tasks_view)  # task_view list presented as string

    def view_completed(self):
        completed = []   # completed TaksUnit objects
        for item in self.all_tasks:
            if item.complete == True:
                completed.append(item.task)

        # catches empty task list error
        if completed == []:
            raise Exception("No completed tasks!")
        
        return completed

    def view_incompleted(self):
        incompleted = []   # incompleted TaksUnit objects
        for item in self.all_tasks:
            if item.complete == False:
                incompleted.append(item.task)
                
        # catches empty task list error
        if incompleted == []:
            raise Exception("No incompleted tasks!")
        
        return incompleted
