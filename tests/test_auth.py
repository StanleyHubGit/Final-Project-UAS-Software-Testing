import pytest
import uuid
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


def test_register_success(client):
    res = client.post('/register', json={
        "username": str(uuid.uuid4()),
        "password": "Password1!"
    })
    assert res.status_code == 201


def test_register_duplicate(client):
    username = str(uuid.uuid4())

    client.post('/register', json={
        "username": username,
        "password": "Password1!"
    })

    res = client.post('/register', json={
        "username": username,
        "password": "Password1!"
    })

    assert res.status_code == 400


def test_login_success(client):
    username = str(uuid.uuid4())

    client.post('/register', json={
        "username": username,
        "password": "Password1!"
    })

    res = client.post('/login', json={
        "username": username,
        "password": "Password1!"
    })

    assert res.status_code == 200


def test_login_fail(client):
    res = client.post('/login', json={
        "username": "wrong_user",
        "password": "WrongPass1!"
    })
    assert res.status_code == 401