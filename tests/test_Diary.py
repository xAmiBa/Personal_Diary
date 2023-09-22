from lib.Diary import *
from lib.DiaryEntry import *
from lib.TaskUnit import *
import pytest

### TEST CLASS DiaryEntry
# test basic modules in DairyEntry class:
#       self.format()
#       self.count_words()
#       self.reading_time(wpm)

def test_format_entry():
    test_DiaryEntry = DiaryEntry("Good day", "I learned a lot of Python today hehe")
    assert test_DiaryEntry.format() == "Good day: I learned a lot of Python today hehe"

def test_if_count_is_10_readingtime_2():
    test_DiaryEntry = DiaryEntry("Good day", "I learned a lot of Python today hehe")
    assert test_DiaryEntry.count_words() == 10
    assert test_DiaryEntry.reading_time(5) == 2

def test_error_reading_time_wpm_0():
    test_DiaryEntry = DiaryEntry("Good day", "I learned a lot of Python today hehe")
    with pytest.raises(Exception) as e:
        test_DiaryEntry.reading_time(0)
    assert str(e.value) == "Words per minute must be more than 0!"

def test_error_reading_time_wpm_no_int():
    test_DiaryEntry = DiaryEntry("Good day", "I learned a lot of Python today hehe")
    with pytest.raises(Exception) as e:
        test_DiaryEntry.reading_time("hey")
    assert str(e.value) == "Words per minute must be a number!"


### TEST CLASS Diary

# checking if Dairy class calls TaskList Class and creates empty task list
def test_init_calls_TaskList():
    test_Diary = Diary()
    assert test_Diary.Task_List.all_tasks == []

# testing integration
# Diary()
#   modules:
#       .add_entry())
#       .view_diary()
# DiaryEntry()
#   modules: 
#       .formatted())

def test_add_diary_3_entries_view_3_formatted_entries_integration():
    test_DiaryEntry1 = DiaryEntry("First day", "I learned a lot of Python today")
    test_DiaryEntry2 = DiaryEntry("Second day", "I ate lunch")
    test_DiaryEntry3 = DiaryEntry("Third day", "I debugged a program")

    test_Diary = Diary()
    test_Diary.add_entry(test_DiaryEntry1)
    test_Diary.add_entry(test_DiaryEntry2)
    test_Diary.add_entry(test_DiaryEntry3)

    assert test_Diary.view_diary() == "First day: I learned a lot of Python today\nSecond day: I ate lunch\nThird day: I debugged a program\n"

def test_view_entry_to_read_returns_9_word_string():
    test_DiaryEntry1 = DiaryEntry("First day", "I learned a lot of Python today") #9
    test_DiaryEntry2 = DiaryEntry("Second day", "I ate lunch") #5
    test_DiaryEntry3 = DiaryEntry("Third day", "I debugged a program") #6
    
    test_Diary = Diary()
    test_Diary.add_entry(test_DiaryEntry1)
    test_Diary.add_entry(test_DiaryEntry2)
    test_Diary.add_entry(test_DiaryEntry3)
    
    #5wpm in 2min = 10min
    assert test_Diary.view_entry_to_read(5, 2) == "First day: I learned a lot of Python today"


def test_view_contacts_if_2_numbers_extracted():
    test_DiaryEntry1 = DiaryEntry("First day", "I met Amina 07899662854") #number
    test_DiaryEntry2 = DiaryEntry("Second day", "I ate lunch")
    test_DiaryEntry3 = DiaryEntry("Third day", "I met Sam 5577862538067") #number
    
    test_Diary = Diary()
    test_Diary.add_entry(test_DiaryEntry1)
    test_Diary.add_entry(test_DiaryEntry2)
    test_Diary.add_entry(test_DiaryEntry3)
    
    assert test_Diary.view_contacts() == "\"First day: I met Amina 07899662854\" -> Contact: 07899662854\n\"Third day: I met Sam 5577862538067\" -> Contact: 5577862538067\n"



# # TESTING FOR ERRORS:

def test_if_wpm_time_are_integer_error_no_dairy_entries_error():
    
    test_Diary = Diary()
    with pytest.raises(Exception) as e1:
        test_Diary.view_entry_to_read(10, 3)
    assert str(e1.value) == "The diary is empty!"

    # adding an entry
    test_DiaryEntry1 = DiaryEntry("First day", "I learned a lot of Python today") #9
    test_Diary.add_entry(test_DiaryEntry1)

    with pytest.raises(Exception) as e:
        test_Diary.view_entry_to_read("j", "h")
    assert str(e.value) == "Words per minute and reading time shlould be a number!"