from Infrastructure.repositories.in_memory_task_repository import InMemoryTaskRepository

from UseCases.add_task import AddTaskCase
from UseCases.update_task import UpdateTaskCase
from UseCases.delete_task import DeleteTaskCase
from UseCases.get_tasks import GetTasksCase

from Entities.task import Task
from Entities.task_attributes import TaskCategory, TaskPriority, TaskStatus


def main():
    # Repository
    repository = InMemoryTaskRepository()

    # Use Cases
    add_task = AddTaskCase(repository)
    update_task = UpdateTaskCase(repository)
    delete_task = DeleteTaskCase(repository)
    get_tasks = GetTasksCase(repository)

    # Create tasks
    task1 = Task(
        task_id="1",
        name="Learn Clean Architecture",
        category=TaskCategory.WORK,
        priority=TaskPriority.HIGH,
    )

    task2 = Task(
        task_id="2",
        name="Watch anime",
        category=TaskCategory.HOBBY,
        priority=TaskPriority.LOW,
    )

    # Add tasks
    add_task.execute(task1)
    add_task.execute(task2)

    print("=== All tasks ===")
    for task in get_tasks.get_all():
        print(task.task_id, task.name, task.status)

    # Update task
    update_task.execute(
        task_id="1",
        status=TaskStatus.DONE,
    )

    print("\n=== After update ===")
    for task in get_tasks.get_all():
        print(task.task_id, task.name, task.status)

    # Filter tasks
    print("\n=== Filter: DONE ===")
    done_tasks = get_tasks.filter(status=TaskStatus.DONE)
    for task in done_tasks:
        print(task.task_id, task.name)

    # Delete task
    delete_task.execute("2")

    print("\n=== After delete ===")
    for task in get_tasks.get_all():
        print(task.task_id, task.name)


if __name__ == "__main__":
    main()

