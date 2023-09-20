'''
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
'''

from datetime import datetime
from lib.TaskUnit import *

class TaskList():
    def __init__(self) -> None:
        self.all_tasks = []  # all TaksUnit objects
        self.completed = []  # completed TaksUnit objects
        self.incompleted = []  # incompleted TaksUnit objects
    
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
        for item in self.all_tasks:
            if item.complete == True:
                self.completed.append(item.task)

        # catches empty task list error
        if self.completed == []:
            raise Exception("No completed tasks!")
        
        return self.completed

    def view_incompleted(self):
        for item in self.all_tasks:
            if item.complete == False:
                self.incompleted.append(item.task)
                
        # catches empty task list error
        if self.incompleted == []:
            raise Exception("No incompleted tasks!")
        
        return self.incompleted

#TODO: List view by due date