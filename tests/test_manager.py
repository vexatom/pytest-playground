import pytest

from src.task_manager.manager import TaskNotFoundError


def test_manager_add_task_correctly_add_task(task, task_manager):
    task_manager.add_task(task)

    assert task in task_manager.tasks

@pytest.mark.parametrize('obj', [None, 'task', 123, True, ('task', 2), ['task'], {'task': 2}])
def test_manager_add_task_receives_only_task_objects(obj, task_manager):
    with pytest.raises(TypeError):
        task_manager.add_task(obj)

def test_manager_get_task_returns_correct_task(task, task_manager):
    task_manager.add_task(task)

    result = task_manager.get_task(task.id)

    assert task == result

@pytest.mark.parametrize('task_id', [-1, 999])
def test_manager_get_task_raises_task_not_found_error_when_task_not_found(task_id, task_manager):
    with pytest.raises(TaskNotFoundError):
        task_manager.get_task(task_id)

@pytest.mark.parametrize('task_id', [None, True, 'id', 12.34, (1, 2), [1, 2], {1: 2}])
def test_manager_get_task_raises_type_error_when_task_id_is_not_int(task_id, task_manager):
    with pytest.raises(TypeError):
        task_manager.get_task(task_id)

