from src.task_manager import Task


class TaskNotFoundError(Exception):
    pass


class TaskManager:

    @staticmethod
    def _validate_task(task: Task) -> None:
        if not isinstance(task, Task):
            raise TypeError('Task must be of type Task')

    @staticmethod
    def _validate_task_id(task_id: int) -> None:
        if type(task_id) is not int:
            raise TypeError('Task ID must be of type int')

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self._validate_task(task)
        self.tasks.append(task)

    def get_task(self, task_id: int) -> Task:
        self._validate_task_id(task_id)
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError
