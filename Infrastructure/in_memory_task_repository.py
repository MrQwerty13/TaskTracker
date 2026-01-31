from Interfaces.task_repository import TaskRepository
from Task.task import Task
from Task.task_attributes import TaskStatus, TaskPriority, TaskCategory


class InMemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def add(self, task: Task) -> None:
        """
        Adds a new task or updates an existing one.
        """
        self._tasks[task.task_id] = task

    def get_by_id(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())

    def remove(self, task_id: str) -> None:
        if task_id not in self._tasks:
            raise ValueError("Task not found")

        del self._tasks[task_id]

    def filter(
        self,
        *,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        category: TaskCategory | None = None,
    ) -> list[Task]:
        tasks = self._tasks.values()

        if status is not None:
            tasks = filter(lambda t: t.status == status, tasks)

        if priority is not None:
            tasks = filter(lambda t: t.priority == priority, tasks)

        if category is not None:
            tasks = filter(lambda t: t.category == category, tasks)

        return list(tasks)

