from lib.TaskList import *

"""
As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
"""

class Diary():
    
    def __init__():
        # Arguments: None
        # Return: None
        # Side effects: self.diary list of DiaryEntry objects
        pass

    def view_diary():
        # Arguments: none
        # Return: string view of all entries
        # Side effects: none
        pass

    def view_tasks():
        choice_tasks = input("[ALL] - all tasks\n[C] - completed tasks\n[I] - incompleted tasks")
        match choice_tasks:
            case "ALL":
                TaskList.view_all()
                pass

            case "C":
                TaskList.view_completed()
                pass

            case "I":
                TaskList.view_incompleted()
                pass

        # Arguments:
        # Return:
        # Side effects:
        pass

    def view_contacts():
        # Arguments:
        # Return:
        # Side effects:
        pass




#TODO: Command line interface