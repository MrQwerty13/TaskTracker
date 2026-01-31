from Interfaces.task_repository import TaskRepository
from Task.task_attributes import TaskStatus, TaskPriority, TaskCategory


class GetTasksCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def filter(
        self,
        *,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        category: TaskCategory | None = None,
    ):
        return self.repository.filter(
            status=status,
            priority=priority,
            category=category,
        )
