from task_attributes import TaskCategory, TaskPriority, TaskStatus


class Task:
    def __init__(
        self,
        task_id: str,
        name: str,
        category: TaskCategory,
        priority: TaskPriority,
        status: TaskStatus = TaskStatus.PENDING,
        description: str | None = None,
    ):
        if not name:
            raise ValueError("Task name cannot be empty")

        self.task_id = task_id
        self.name = name
        self.category = category
        self.priority = priority
        self.status = status
        self.description = description

    def change_status(self, status: TaskStatus) -> None:
        self.status = status

    def change_priority(self, priority: TaskPriority) -> None:
        self.priority = priority

    def change_category(self, category: TaskCategory) -> None:
        self.category = category
