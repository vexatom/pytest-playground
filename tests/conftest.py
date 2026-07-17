import pytest

from src.task_manager import Task, TaskManager


@pytest.fixture
def task():
    return Task('<NAME>', 'This is a test task')

@pytest.fixture
def inactive_task():
    return Task('<NAME>', 'This is a test task', status=False)

@pytest.fixture
def important_task():
    return Task('Important task', 'This is a very important task', status=True, priority=3)

@pytest.fixture
def task_manager():
    return TaskManager()
