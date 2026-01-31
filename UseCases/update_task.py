from Interfaces.task_repository import TaskRepository
from Task.task_attributes import TaskStatus, TaskPriority, TaskCategory


class UpdateTaskCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(
        self,
        task_id: str,
        *,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        category: TaskCategory | None = None,
    ) -> None:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")

        if status:
            task.change_status(status)
        if priority:
            task.change_priority(priority)
        if category:
            task.change_category(category)

        self.repository.add(task)
