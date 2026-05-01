import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

    return app.test_client()

def test_home_page(client):
    client.post('/register', json={
        "username": "user_test",
        "password": "Password1!"
    })

    client.post('/login', json={
        "username": "user_test",
        "password": "Password1!"
    })

    res = client.get('/')
    assert res.status_code == 200

def test_create_task_success(client):
    res = client.post('/tasks', json={"title": "API Task"})
    assert res.status_code == 201
    assert res.json["title"] == "API Task"

def test_create_task_invalid(client):
    res = client.post('/tasks', json={"title": ""})
    assert res.status_code == 400

def test_get_tasks(client):
    res = client.get('/tasks')
    assert res.status_code == 200

def test_complete_task_success(client):
    create = client.post('/tasks', json={"title": "To Complete"})
    task_id = create.json["id"]

    res = client.put(f'/tasks/{task_id}')
    assert res.status_code == 200
    assert res.json["completed"] == True

def test_complete_task_not_found(client):
    res = client.put('/tasks/9999')
    assert res.status_code == 404

def test_delete_task_success(client):
    create = client.post('/tasks', json={"title": "To Delete"})
    task_id = create.json["id"]

    res = client.delete(f'/tasks/{task_id}')
    assert res.status_code == 200

def test_delete_task_not_found(client):
    res = client.delete('/tasks/9999')
    assert res.status_code == 404