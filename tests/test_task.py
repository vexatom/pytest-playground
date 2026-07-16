import pytest

from src.task_manager import Task


def test_task_returns_correct_name():
    name = "<NAME>"
    description = "This is a test task"

    task = Task(name, description)

    assert task.name == name

def test_task_returns_correct_description():
    name = "<NAME>"
    description = "This is a test task"

    task = Task(name, description)

    assert task.description == description

def test_task_returns_correct_status():
    name = "<NAME>"
    description = "This is a test task"
    status = False

    task = Task(name, description, status=status)

    assert task.status == status
