from .models import Task
from . import db

def add_task(title):
    if not title or title.strip() == "":
        raise ValueError("Title is required")

    task = Task(title=title)
    db.session.add(task)
    db.session.commit()

    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }

def get_tasks():
    tasks = Task.query.all()
    return [
        {"id": t.id, "title": t.title, "completed": t.completed}
        for t in tasks
    ]

def complete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        raise ValueError("Task not found")

    task.completed = True
    db.session.commit()

    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }

def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        raise ValueError("Task not found")

    db.session.delete(task)
    db.session.commit()

    return {"id": task.id}