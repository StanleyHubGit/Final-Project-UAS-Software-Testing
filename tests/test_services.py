import pytest
from app import create_app, db
from app.services import add_task, get_tasks, complete_task, delete_task, update_task

@pytest.fixture
def app_context():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


def test_add_task_success(app_context):
    task = add_task("Belajar")
    assert task["title"] == "Belajar"


def test_get_tasks_returns_list(app_context):
    add_task("A")
    tasks = get_tasks()
    assert isinstance(tasks, list)


def test_complete_task_success(app_context):
    task = add_task("Complete Me")
    updated = complete_task(task["id"])
    assert updated["completed"] is True


def test_complete_task_not_found(app_context):
    with pytest.raises(ValueError):
        complete_task(9999)


def test_delete_task_success(app_context):
    task = add_task("Delete Me")
    result = delete_task(task["id"])
    assert result["id"] == task["id"]


def test_delete_task_not_found(app_context):
    with pytest.raises(ValueError):
        delete_task(9999)


def test_multiple_tasks(app_context):
    add_task("Task 1")
    add_task("Task 2")
    tasks = get_tasks()
    assert len(tasks) == 2


def test_task_id_increment(app_context):
    t1 = add_task("A")
    t2 = add_task("B")
    assert t2["id"] > t1["id"]


# =====================
# UPDATE TASK TEST
# =====================

def test_update_task_success(app_context):
    task = add_task("Old")
    updated = update_task(task["id"], "New")
    assert updated["title"] == "New"


def test_update_task_not_found(app_context):
    with pytest.raises(ValueError):
        update_task(999, "New")


def test_update_task_empty_title(app_context):
    task = add_task("Task")
    with pytest.raises(ValueError):
        update_task(task["id"], "")