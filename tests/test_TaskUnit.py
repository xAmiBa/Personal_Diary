from lib.TaskUnit import TaskUnit
import pytest
from datetime import datetime


def test_init_default():
    task = TaskUnit(task="123")
    assert task.task == "123" 
    assert task.complete == False
    assert task.due_date == datetime(2100, 1, 1)
    assert task.due_date_formatted == None


def test_mark_complete():
    task = TaskUnit(task="123")
    task.mark_complete()
    assert task.complete == True


def test_mark_incomplete():
    task = TaskUnit(task="123")
    task.mark_complete()
    task.mark_incomplete()
    assert task.complete == False


def test_init_due_date():
    task= TaskUnit(task="123", d=20, m=9, y=2023)
    assert task.due_date == datetime(2023, 9, 20)
    assert task.due_date_formatted == "20/09/2023"




#ERRORS:
def test_no_task_error():
    with pytest.raises(Exception) as e:
        task1 = TaskUnit("")
    error = str(e.value)
    assert error == "No input for task"

def test_date_noninteger():
    with pytest.raises(Exception) as e:
        task1 = TaskUnit("task", "j", 9, "j")
    error = str(e.value)
    assert error == "Date should be integer."