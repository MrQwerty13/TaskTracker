from abc import ABC, abstractmethod
from Task.task import Task
from Task.task_attributes import TaskStatus, TaskPriority, TaskCategory


class TaskRepository(ABC):

    @abstractmethod
    def add(self, task: Task) -> None:
        pass

    @abstractmethod
    def get_by_id(self, task_id: str) -> Task | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Task]:
        pass

    @abstractmethod
    def remove(self, task_id: str) -> None:
        pass

    @abstractmethod
    def filter(
        self, *,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        category: TaskCategory | None = None,
    ) -> list[Task]:
        pass
