"""A tiny in-memory task manager used to demo PR-Agent reviews."""

from dataclasses import dataclass, field
from datetime import datetime

PRIORITY_LOW = 1
PRIORITY_MEDIUM = 2
PRIORITY_HIGH = 3


@dataclass
class Task:
    title: str
    priority: int = PRIORITY_LOW
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)


class TaskBoard:
    """Manages a list of tasks in memory."""

    def __init__(self):
        self._tasks: list[Task] = []

    def add(self, title: str, priority: int = PRIORITY_LOW) -> Task:
        if not title or not title.strip():
            raise ValueError("title must not be empty")
        task = Task(title=title.strip(), priority=priority)
        self._tasks.append(task)
        return task

    def complete(self, title: str) -> bool:
        for task in self._tasks:
            if task.title == title and not task.completed:
                task.completed = True
                return True
        return False

    def pending(self) -> list[Task]:
        return [t for t in self._tasks if not t.completed]

    def stats(self) -> dict:
        done = sum(1 for t in self._tasks if t.completed)
        return {"total": len(self._tasks), "done": done, "pending": len(self._tasks) - done}
