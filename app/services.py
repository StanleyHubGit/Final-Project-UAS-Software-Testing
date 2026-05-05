from .models import Task  # import model Task (database)
from . import db  # import database instance

# =====================
# CREATE TASK
# =====================
def add_task(title):
    if not title or title.strip() == "":
        raise ValueError("Title is required")  # validasi input

    task = Task(title=title)  # buat object task
    db.session.add(task)  # simpan ke database
    db.session.commit()  # commit perubahan

    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }  # return dalam bentuk dictionary


# =====================
# READ TASK
# =====================
def get_tasks():
    tasks = Task.query.all()  # ambil semua data dari database

    return [
        {"id": t.id, "title": t.title, "completed": t.completed}
        for t in tasks
    ]  # convert ke list of dict (JSON friendly)


# =====================
# UPDATE STATUS (COMPLETE)
# =====================
def complete_task(task_id):
    task = Task.query.get(task_id)  # cari task berdasarkan id

    if not task:
        raise ValueError("Task not found")  # jika tidak ada

    task.completed = True  # ubah status jadi selesai
    db.session.commit()  # simpan perubahan

    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }


# =====================
# DELETE TASK
# =====================
def delete_task(task_id):
    task = Task.query.get(task_id)  # cari task

    if not task:
        raise ValueError("Task not found")  # jika tidak ada

    db.session.delete(task)  # hapus dari database
    db.session.commit()  # commit perubahan

    return {"id": task.id}  # return id task yang dihapus


# =====================
# UPDATE TASK (EDIT TITLE)
# =====================
def update_task(task_id, new_title):
    if not new_title or not new_title.strip():
        raise ValueError("Title cannot be empty")  # validasi input

    task = Task.query.get(task_id)  # cari task

    if not task:
        raise ValueError("Task not found")  # jika tidak ada

    task.title = new_title  # update title
    db.session.commit()  # simpan perubahan

    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }