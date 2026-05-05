import pytest
from app import create_app, db
from app.services import add_task, get_tasks, complete_task, delete_task, update_task

# =====================
# SETUP APP CONTEXT
# =====================
@pytest.fixture
def app_context():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # DB sementara

    with app.app_context():
        db.create_all()  # buat tabel
        yield  # jalankan test
        db.session.remove()
        db.drop_all()  # reset DB


# =====================
# CREATE TEST
# =====================
def test_add_task_success(app_context):
    task = add_task("Belajar")
    assert task["title"] == "Belajar"  # cek title sesuai


# =====================
# READ TEST
# =====================
def test_get_tasks_returns_list(app_context):
    add_task("A")
    tasks = get_tasks()
    assert isinstance(tasks, list)  # harus list


# =====================
# COMPLETE TEST
# =====================
def test_complete_task_success(app_context):
    task = add_task("Complete Me")
    updated = complete_task(task["id"])
    assert updated["completed"] is True  # harus true


def test_complete_task_not_found(app_context):
    with pytest.raises(ValueError):
        complete_task(9999)  # task tidak ada → error


# =====================
# DELETE TEST
# =====================
def test_delete_task_success(app_context):
    task = add_task("Delete Me")
    result = delete_task(task["id"])
    assert result["id"] == task["id"]  # id cocok


def test_delete_task_not_found(app_context):
    with pytest.raises(ValueError):
        delete_task(9999)  # tidak ada → error


# =====================
# MULTI TASK TEST
# =====================
def test_multiple_tasks(app_context):
    add_task("Task 1")
    add_task("Task 2")
    tasks = get_tasks()
    assert len(tasks) == 2  # jumlah sesuai


def test_task_id_increment(app_context):
    t1 = add_task("A")
    t2 = add_task("B")
    assert t2["id"] > t1["id"]  # id harus naik


# =====================
# UPDATE TEST
# =====================
def test_update_task_success(app_context):
    task = add_task("Old")
    updated = update_task(task["id"], "New")
    assert updated["title"] == "New"  # berhasil update


def test_update_task_not_found(app_context):
    with pytest.raises(ValueError):
        update_task(999, "New")  # task tidak ada


def test_update_task_empty_title(app_context):
    task = add_task("Task")
    with pytest.raises(ValueError):
        update_task(task["id"], "")  # title kosong


# =====================
# ADD TASK EDGE CASE
# =====================
def test_add_task_empty_title(app_context):
    with pytest.raises(ValueError):
        add_task("")  # title kosong


def test_add_task_whitespace_title(app_context):
    with pytest.raises(ValueError):
        add_task("   ")  # hanya 


# =====================
# GET TASKS EDGE CASE
# =====================
def test_get_tasks_empty(app_context):
    tasks = get_tasks()
    assert tasks == []  # harus kosong kalau belum ada data


# =====================
# COMPLETE TASK IDEMPOTENT
# =====================
def test_complete_task_already_completed(app_context):
    task = add_task("Done Task")
    complete_task(task["id"])  # pertama

    updated = complete_task(task["id"])  # kedua
    assert updated["completed"] is True  # tetap true