import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    return app.test_client()

def test_register_success(client):
    res = client.post('/register', json={
        "username": "user1",
        "password": "123"
    })
    assert res.status_code == 201

def test_register_duplicate(client):
    client.post('/register', json={"username": "user2", "password": "123"})
    res = client.post('/register', json={"username": "user2", "password": "123"})
    assert res.status_code == 400

def test_login_success(client):
    client.post('/register', json={"username": "user3", "password": "123"})
    res = client.post('/login', json={"username": "user3", "password": "123"})
    assert res.status_code == 200

def test_login_fail(client):
    res = client.post('/login', json={"username": "wrong", "password": "wrong"})
    assert res.status_code == 401