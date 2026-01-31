from enum import Enum


class TaskStatus(str, Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskCategory(str, Enum):
    WORK = "work"
    PERSONAL = "personal"
    HOME = "home"
    HOBBY = "hobby"
