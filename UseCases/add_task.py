from Interfaces.task_repository import TaskRepository
from Task.task import Task


class AddTaskCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self, task: Task) -> None:
        if self.repository.get_by_id(task.task_id):
            raise ValueError("Task with this ID already exists")

        self.repository.add(task)
