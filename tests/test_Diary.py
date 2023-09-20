from lib.Diary import *
from lib.DiaryEntry import *
from lib.TaskUnit import *
import pytest

### TEST CLASS DiaryEntry
# test basic modules in DairyEntry class:
#       self.format()
#       self.count_words()
#       self.reading_time(wpm)

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
