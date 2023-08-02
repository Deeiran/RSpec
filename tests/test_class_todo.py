from lib.class_todo import *
import pytest 

"""
initally, there is no todo task
return empty list 
"""
def test_intially_no_task():
    todo = Todo()
    assert todo.incomplted_task() == []

"""
When we add a task 
that task added to the todo list. 
"""
def test_add_a_task():
    todo = Todo()
    todo.add("go to class")
    assert todo.incomplted_task() == ["go to class"]



"""
When we add mulitble task 
all task added to the todo list. 
"""
def test_multible_task():
    todo = Todo()
    todo.add("go to class")
    todo.add("go to shop")
    todo.add("go to park")
    assert todo.incomplted_task() == ["go to class", "go to shop","go to park"]

"""
When we mark task as complete
markone as completed and disappear from the todo list. 
"""

def test_remove_task():
    todo = Todo()
    todo.add("go to class")
    todo.add("go to shop")
    todo.add("go to park")
    todo.mark_completed_task(1)
    assert todo.incomplted_task() == ["go to class","go to park"]
"""
When we mark task as complete, task is not in the list(lower),raise an error "there is no such a task is in the list" 
"""
def test_remove_task_lower():
    todo = Todo()
    todo.add("go to class")
    with pytest.raises(Exception) as err:
        todo.mark_completed_task(-1)
    assert str(err.value) == "there is no such a task is in the list" 
"""
When we mark task as complete, task is not in the list(upper),raise an error "there is no such a task is in the list" 
"""
def test_remove_task():
    todo = Todo()
    todo.add("go to class")
    with pytest.raises(Exception) as err:
        todo.mark_completed_task(1)
    assert str(err.value) == "there is no such a task is in the list" 
    