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

def test_task_returns_correct_status_when_status_is_false():
    name = "<NAME>"
    description = "This is a test task"
    status = False

    task = Task(name, description, status=status)

    assert task.status == status

def test_task_raises_value_error_when_name_is_empty():
    name = ""
    description = "This is a test task"

    with pytest.raises(ValueError):
        Task(name, description)

def test_task_raises_value_error_when_name_is_whitespaces():
    name = "   "
    description = "This is a test task"

    with pytest.raises(ValueError):
        Task(name, description)

def test_task_raises_type_error_when_name_is_none():
    name = None
    description = "This is a test task"

    with pytest.raises(TypeError):
        Task(name, description)

def test_task_raises_value_error_when_name_len_greater_than_50():
    name = "A" * 51
    description = "This is a test task"

    with pytest.raises(ValueError):
        Task(name, description)

def test_task_name_is_string():
    name = "<NAME>"
    description = "This is a test task"

    task = Task(name, description)

    assert isinstance(task.name, str)

def test_task_allows_when_name_len_is_50():
    name = "A" * 50
    description = "This is a test task"

    task = Task(name, description)

    assert task.name == name

def test_task_allows_when_description_is_empty():
    name = "<NAME>"
    description = ""

    task = Task(name, description)

    assert task.description == description

def test_task_raises_type_error_when_description_is_not_str():
    name = "<NAME>"
    description = None

    with pytest.raises(TypeError):
        Task(name, description)

def test_task_raises_value_error_when_description_len_greater_than_400():
    name = "<NAME>"
    description = 'A' * 401

    with pytest.raises(ValueError):
        Task(name, description)

def test_task_allows_when_description_len_is_400():
    name = "<NAME>"
    description = 'A' * 400

    task = Task(name, description)

    assert task.description == description
