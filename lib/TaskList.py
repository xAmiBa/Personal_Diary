'''
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
'''
from datetime import datetime
from lib.TaskUnit import TaskUnit

class TaskList():
    def __init__(self) -> None:
        