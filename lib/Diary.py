# from lib.TaskList import *
# from lib.TaskUnit import *

from TaskList import TaskList
from TaskUnit import TaskUnit
from DiaryEntry import DiaryEntry

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
    
    def __init__(self):
        # Side effects: self.diary list of DiaryEntry objects
        # Calls TaskList Class
        self.diary = []
        self.Task_List = TaskList() #TaskList integration/initiation
    
    def add_entry(self, entry):
        # Side effects: add DiaryEntry Objcet to the task list
        self.diary.append(entry)

    def view_diary(self):
        # Return: string view of all entries
        return "".join([ f"{entry.format()}\n" for entry in self.diary])
    
    def view_entry_to_read(self, wpm, time):
        # Return: string of entry which user can read based on how much time they have and their reading speed
        # Exception: in not integer, if diary empty
        if type(wpm) is not int or type(time) is not int:
            raise Exception("Words per minute and reading time shlould be a number!")
        
        if self.diary == []:
            raise Exception("The diary is empty!")
        
        total_words = wpm * time
        word_counts = [entry.count_words() for entry in self.diary]
        # lambda: fro number in word_counts choose the lowest defference between
        # total_words and word_counts
        closest = min(word_counts, key=lambda num: abs(num - total_words))
        for entry in self.diary:
            if entry.count_words() == closest:
                return entry.format()

    def add_task(self):
        # Return: string view of all entries
        choice_new_task = input("New task: ")
        # assign input as function argument
        new_task = TaskUnit(choice_new_task)
        self.Task_List.add(new_task)

    def view_tasks(self):
        self.Task_List.view_all()

    def view_contacts(self):
        # Return: string of quoted diary entry followed by -> Contact: [number] \n
        self.contact_list = ""
        for entry in self.diary:
            single_entry = entry.format().split()
            for word in single_entry:
                if len(word) > 9 and word.isnumeric() == True:
                    self.contact_list += (f"\"{' '.join(single_entry)}\" -> Contact: {word}\n")
        return self.contact_list