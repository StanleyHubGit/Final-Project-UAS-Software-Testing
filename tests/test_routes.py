import pytest
from app import create_app, db
from app.models import User

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


def test_login_page(client):
    res = client.get('/login-page')
    assert res.status_code == 200


def test_login_sets_session(client):
    username = "user_session"
    client.post('/register', json={
        "username": username,
        "password": "Password1!"
    })
    res = client.post('/login', json={
        "username": username,
        "password": "Password1!"
    })
    assert res.status_code == 200


def test_register_null_json(client):
    res = client.post('/register', json=None)
    assert res.status_code == 400


def test_register_page(client):
    res = client.get('/register-page')
    assert res.status_code == 200


def test_home_requires_login(client):
    res = client.get('/')
    assert res.status_code in [302, 401]


def test_home_page_logged_in(client):
    with client.application.app_context():
        user = User(username="testuser", password="Password1!")
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    with client.session_transaction() as sess:
        sess['user_id'] = user_id

    res = client.get('/')
    assert res.status_code == 200


def test_home_user_not_found(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 999  # user tidak ada

    res = client.get('/')
    assert res.status_code == 302


def test_home_redirect_if_not_logged_in(client):
    res = client.get('/')
    assert res.status_code == 302


def test_create_task_success(client):
    res = client.post('/tasks', json={"title": "Task 1"})
    assert res.status_code == 201


def test_create_task_no_title(client):
    res = client.post('/tasks', json={})
    assert res.status_code == 400


def test_create_task_empty_title(client):
    res = client.post('/tasks', json={"title": ""})
    assert res.status_code == 400


def test_create_task_null_json(client):
    res = client.post('/tasks', json=None)
    assert res.status_code == 400


def test_get_tasks_empty(client):
    res = client.get('/tasks')
    assert res.status_code == 200


def test_get_tasks_with_data(client):
    client.post('/tasks', json={"title": "Task A"})
    res = client.get('/tasks')
    assert res.status_code == 200
    assert isinstance(res.json, list)


def test_complete_task_success(client):
    res = client.post('/tasks', json={"title": "Complete Me"})
    task_id = res.json["id"]

    res2 = client.put(f'/tasks/{task_id}')
    assert res2.status_code == 200


def test_complete_task_not_found(client):
    res = client.put('/tasks/999')
    assert res.status_code == 404


def test_complete_task_invalid_id(client):
    res = client.put('/tasks/0')
    assert res.status_code == 404


def test_delete_task_success(client):
    res = client.post('/tasks', json={"title": "Delete Me"})
    task_id = res.json["id"]

    res2 = client.delete(f'/tasks/{task_id}')
    assert res2.status_code == 200


def test_delete_task_not_found(client):
    res = client.delete('/tasks/999')
    assert res.status_code == 404


def test_delete_task_invalid_id(client):
    res = client.delete('/tasks/0')
    assert res.status_code == 404


def test_update_task_success(client):
    res = client.post('/tasks', json={"title": "Old Task"})
    task_id = res.json["id"]

    res2 = client.patch(f'/tasks/{task_id}', json={"title": "New Task"})
    assert res2.status_code == 200
    assert res2.json["title"] == "New Task"


def test_update_task_not_found(client):
    res = client.patch('/tasks/999', json={"title": "New"})
    assert res.status_code == 400


def test_update_task_empty_title(client):
    res = client.post('/tasks', json={"title": "Task"})
    task_id = res.json["id"]

    res2 = client.patch(f'/tasks/{task_id}', json={"title": ""})
    assert res2.status_code == 400


def test_update_task_null_json(client):
    res = client.post('/tasks', json={"title": "Task"})
    task_id = res.json["id"]

    res2 = client.patch(f'/tasks/{task_id}', json=None)
    assert res2.status_code == 400


def test_logout(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    res = client.get('/logout')
    assert res.status_code == 302