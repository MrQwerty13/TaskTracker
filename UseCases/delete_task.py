from Interfaces.task_repository import TaskRepository


class DeleteTaskCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self, task_id: str) -> None:
        self.repository.remove(task_id)
