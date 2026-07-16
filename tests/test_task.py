import pytest

from src.task_manager import Task


@pytest.fixture
def task():
    return Task('<NAME>', 'This is a test task')

@pytest.fixture
def inactive_task():
    return Task('<NAME>', 'This is a test task', status=False)

def test_task_returns_correct_name(task):
    assert task.name == '<NAME>'

def test_task_returns_correct_description(task):
    assert task.description == 'This is a test task'

def test_task_returns_correct_status_when_status_is_false(inactive_task):
    assert inactive_task.status is False

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

@pytest.mark.parametrize('priority', [True, 'high', (1, 2), None, {1: 2}, [1, 2]])
def test_task_raises_type_error_when_priority_is_not_int(priority):
    name = "<NAME>"
    description = "This is a test task"

    with pytest.raises(TypeError):
        Task(name, description, priority=priority)

@pytest.mark.parametrize('priority', [-1, 4])
def test_task_raises_value_error_when_priority_not_between_0_and_3(priority):
    name = "<NAME>"
    description = "This is a test task"

    with pytest.raises(ValueError):
        Task(name, description, priority=priority)

def test_task_returns_correct_priority():
    name = "<NAME>"
    description = "This is a test task"
    priority = 3

    task = Task(name, description, priority=priority)

    assert task.priority == priority

def test_tasks_have_unique_ids(task, inactive_task):
    assert task.id != inactive_task.id

@pytest.mark.parametrize('name', ['', ' '])
def test_set_name_raises_value_error_for_empty_name(name):
    task = Task('<NAME>', 'This is a test task')
    with pytest.raises(ValueError):
        task.set_name(name)

@pytest.mark.parametrize('description', [None, [1, 2], (1, 2), {1: 2}, False, 123])
def test_set_description_raises_type_error_when_description_is_not_str(description):
    task = Task('<NAME>', 'This is a test task')

    with pytest.raises(TypeError):
        task.set_description(description)


def test_set_description_raises_value_error_when_description_greater_than_400():
    task = Task('<NAME>', 'This is a test task')

    with pytest.raises(ValueError):
        task.set_description('A' * 401)

@pytest.mark.parametrize('status', ['active', 1, [1, 2], {1: 2}, (1, 2)])
def test_task_raises_type_error_for_not_boolean_status(status):
    with pytest.raises(TypeError):
        Task('<NAME>', 'This is a test task', status=status)

def test_change_status_returns_reverse_value():
    status = False
    task = Task('<NAME>', 'This is a test task', status=status)

    task.change_status()

    assert task.status is not status

