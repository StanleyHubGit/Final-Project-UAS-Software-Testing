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


def test_register_invalid_password(client):
    res = client.post('/register', json={
        "username": "user_invalid",
        "password": "123"
    })
    assert res.status_code == 400


def test_register_no_username(client):
    res = client.post('/register', json={
        "password": "Password1!"
    })
    assert res.status_code == 400


def test_register_no_password(client):
    res = client.post('/register', json={
        "username": "user_no_pass"
    })
    assert res.status_code == 400


def test_register_no_letter(client):
    res = client.post('/register', json={
        "username": "user_no_letter",
        "password": "12345678!"
    })
    assert res.status_code == 400


def test_register_no_number(client):
    res = client.post('/register', json={
        "username": "user_no_number",
        "password": "Password!"
    })
    assert res.status_code == 400


def test_register_no_symbol(client):
    res = client.post('/register', json={
        "username": "user_no_symbol",
        "password": "Password1"
    })
    assert res.status_code == 400


def test_register_whitespace_username(client):
    res = client.post('/register', json={
        "username": "   ",
        "password": "Password1!"
    })
    assert res.status_code == 400


def test_register_whitespace_password(client):
    res = client.post('/register', json={
        "username": "user_space",
        "password": "   "
    })
    assert res.status_code == 400


def test_register_null_json(client):
    res = client.post('/register', json=None)
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


def test_login_wrong_password(client):
    client.post('/register', json={
        "username": "userx",
        "password": "Password1!"
    })

    res = client.post('/login', json={
        "username": "userx",
        "password": "WrongPass1!"
    })

    assert res.status_code == 401


def test_login_user_not_found(client):
    res = client.post('/login', json={
        "username": "wrong_user",
        "password": "Password1!"
    })
    assert res.status_code == 401


def test_login_no_username(client):
    res = client.post('/login', json={
        "password": "Password1!"
    })
    assert res.status_code == 401


def test_login_no_password(client):
    res = client.post('/login', json={
        "username": "user"
    })
    assert res.status_code == 401


def test_login_empty_json(client):
    res = client.post('/login', json={})
    assert res.status_code == 401


def test_login_null_json(client):
    res = client.post('/login', json=None)
    assert res.status_code == 401