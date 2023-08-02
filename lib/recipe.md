#Todo list.

## 1.Discribe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list. 

we may want to look through multible task to do list
remove the completed task

## 2.Disign the Method Signature

class Todo()
   
    def add(self,task):
        #Parameter:
        #task = human readable text
    passs
 
    def uncomplted_task(self),
        #Return:
            list of tasks
    def mark_completed_task(self,index)
        #Parameter:
            Index - an int representing the completed task
        #side effects: index represented task will be removed from the list. 
    pass



## 3.Create Example as Tests. 

"""
initally, there is no todo task
return empty list 
"""
def test_intially_no_task():
todo = Todo()
todo.list_tasks() = []

# => []

"""
When we add a task 
that task added to the todo list. 
"""
def test_add_a_task()
todo = Todo()
todo.add("go to class")
todo.list_tasks() = ["go to class"]

# => ["go to class"]

"""
When we add mulitble task 
all task added to the todo list. 
"""
def test_multible_task()
todo = Todo()
todo.add("go to class")
todo.add("go to shop")
todo.add("go to park")
todo.list_tasks() = ["go to class", "go to shop","go to park"]

# => ["go to class", "go to shop", "go to park"]

When we mark task as complete
markone as completed and disappear from the todo list. 
"""
def test_remove_task()
todo = Todo()
todo.add("go to class")
todo.add("go to shop")
todo.add("go to park")
todo.mark_completed_task(1)
todo.list_tasks() = ["go to class","go to park"]

# => ["go to class", "go to park"]

When we mark task as complete
mark one not in the list as completed ,raise an error "there is no such a task is in the list" 
"""
"""
def test_remove_task()
todo = Todo()
todo.add("go to class")
todo.mark_completed_task(-1)
raise an error message "there is no such a task is in the list" 




#music_tracker

## 1.Discribe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

we may want to look through multible tracks to be added. 

## 2.Disign the Method Signature

class Tracker()
   
    def add(self,track):
        #Parameter:
        #string:human readable text-song name
    passs
 
    def tracker_list(self),
        #Return:
            list of tasks



## 3.Create Example as Tests. 

"""
initally, there is no tracks
return empty list 
"""
def test_intially_no_track():
tracker = Tracker()
tracker.tracker_list() = []

# => []

"""
When we add a track
that tracker added to the tracker list. 
"""
def test_add_a_track()
tracker = Tracker()
tracker.add("beliver")
tracker.tracker_list() = ["beliver"]

# => ["beliver"]

"""
When we add mulitble tracks 
all tracks added to the tracker list. 
"""
def test_add_a_track()
tracker = Tracker()
tracker.add("beliver")
tracker.add("don't give up")
tracker.add("love me like you do")
tracker.tracker_list() = ["beliver","don't give up" "love me like you do"]

# => ["beliver","don't give up" "love me like you do"]

 

When we 
mark one not in the list as completed ,raise an error "there is no such a task is in the list" 
"""
"""
def test_remove_task()
todo = Todo()
todo.add("go to class")
todo.mark_completed_task(-1)
raise an error message "there is no such a task is in the list" 


## 4.Implement the Behaviour. 