from enum import Enum

class Status(Enum):
    TODO = 1
    BLOCKED = 2
    INPROGRESS = 3
    COMPLETED = 4

class Task:
    def __init__(self, name: str, description: str, priority: int, status: Status):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status

    def updateDescription(self, description: str):
        self.description = description

    def updatePriority(self, priority: int):
        self.priority = priority

    def updateStatus(self, status: Status):
        self.status = status
