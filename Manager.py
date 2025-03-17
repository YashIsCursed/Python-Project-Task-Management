from Task import Task, Status

class Manager:
    def __init__(self):
        self.Tasks = []

    def create_Task(self, name: str, description: str, priority: int, status: Status):
        new_task = Task(name, description, priority, status)
        self.Tasks.append(new_task)
