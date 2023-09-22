from lib.TaskList import *
from lib.TaskUnit import *
import pytest
from datetime import datetime

# TaskList TESTS

def test_add_two_new_tasks():
    test_TaskList = TaskList()
    task1 = TaskUnit("My test task", 20, 9, 2023)
    task2 = TaskUnit("My test task1", 10, 1, 2023)

    test_TaskList.add(task1)
    test_TaskList.add(task2)

    assert test_TaskList.all_tasks == [task1, task2]
    
# @pytest.mark.skip
def test_view_task_list():
    test_TaskList = TaskList()
    task1 = TaskUnit("My test task") # date should be none
    task2 = TaskUnit("My test task1", 20, 9, 2023) # date should appear

    test_TaskList.add(task1)
    test_TaskList.add(task2)

    assert test_TaskList.view_all() == "My test task due on None\nMy test task1 due on 20/09/2023\n"

def test_view_completed_list():
    task1 = TaskUnit("test task")
    test_list = TaskList()
    task1.mark_complete()
    test_list.add(task1)
    assert test_list.view_completed() == ["test task"]

# @pytest.mark.skip
def test_view_incompleted_list():
    task1 = TaskUnit("test task")
    test_list = TaskList()
    test_list.add(task1)
    assert test_list.view_incompleted() == ["test task"]

# ERRORS:
def test_view_error_no_tasks():
    with pytest.raises(Exception) as e:
        test_TaskList = TaskList()
        test_TaskList.view_all()
    assert str(e.value) == "Task list empty!"

def test_no_task_completed_error():
    task1 = TaskUnit("test task")
    test_list = TaskList()
    test_list.add(task1)
    with pytest.raises(Exception) as e:
        test_list.view_completed()
    error = str(e.value)
    assert error == "No completed tasks!"

def test_no_task_incompleted_error():
    task1 = TaskUnit("test task")
    task1.mark_complete()
    test_list = TaskList()
    test_list.add(task1)
    with pytest.raises(Exception) as e:
        test_list.view_incompleted()
    error = str(e.value)
    assert error == "No incompleted tasks!"


# Taskunit TESTS:
# From each unit call specific variables:
#       self.task
#       self.due_date -> for sorting
#       self.due_date_formatted

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