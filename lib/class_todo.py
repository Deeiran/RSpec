class Todo():
    def __init__(self):
        self._task_list = []
    def add(self,task): 
        self._task_list.append(task)

    def incomplted_task(self):
        return self._task_list
    
    def mark_completed_task(self,index):
        if index < 0 or index >= 1:
            raise Exception("there is no such a task is in the list" )
        self._task_list.pop(index)


