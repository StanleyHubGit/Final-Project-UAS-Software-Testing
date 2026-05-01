import pytest
from app.services import add_task, get_tasks, complete_task, delete_task

def test_add_task_success():
    task = add_task("Belajar")
    assert task["title"] == "Belajar"
    assert task["completed"] == False

def test_add_task_empty():
    with pytest.raises(ValueError):
        add_task("")

def test_add_task_whitespace():
    with pytest.raises(ValueError):
        add_task("   ")

def test_get_tasks_returns_list():
    tasks = get_tasks()
    assert isinstance(tasks, list)

def test_complete_task_success():
    task = add_task("Complete Me")
    updated = complete_task(task["id"])
    assert updated["completed"] == True

def test_complete_task_not_found():
    with pytest.raises(ValueError):
        complete_task(9999)

def test_delete_task_success():
    task = add_task("Delete Me")
    deleted = delete_task(task["id"])
    assert deleted["id"] == task["id"]

def test_delete_task_not_found():
    with pytest.raises(ValueError):
        delete_task(9999)

def test_multiple_tasks():
    add_task("Task 1")
    add_task("Task 2")
    tasks = get_tasks()
    assert len(tasks) >= 2

def test_task_id_increment():
    t1 = add_task("A")
    t2 = add_task("B")
    assert t2["id"] > t1["id"]