import pytest
# from lib.TaskList import *
from TaskList import TaskList

"""
As a user
So that I can record my experiences
I want to keep a regular diary
"""

class DiaryEntry:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.contents_available = self.contents.split(" ")
        pass

    def format(self):
        # formatted string of title and contents
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # number of words in entry
        count = len((self.format()).split(" "))
        return count

    def reading_time(self, wpm):
        # catch non int error
        if type(wpm) != int:
            raise Exception("Words per minute must be a number!")
        # catch 0 error
        if wpm <= 0:
            raise Exception("Words per minute must be more than 0!")
        # how much time it will take to read this entry
        count = self.count_words()
        return count/wpm