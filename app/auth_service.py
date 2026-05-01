from .models import User
from . import db
import re

def register_user(username, password):
    if not username or not username.strip():
        raise ValueError("Username cannot be empty")

    if not password or not password.strip():
        raise ValueError("Password cannot be empty")

    # VALIDASI PASSWORD
    if len(password) < 8:
        raise ValueError("Password minimal 8 karakter")

    if not re.search(r"[A-Za-z]", password):
        raise ValueError("Password harus mengandung huruf")

    if not re.search(r"\d", password):
        raise ValueError("Password harus mengandung angka")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError("Password harus mengandung simbol")

    if User.query.filter_by(username=username.strip()).first():
        raise ValueError("User already exists")

    user = User(
        username=username.strip(),
        password=password
    )

    db.session.add(user)
    db.session.commit()

    return user


def login_user(username, password):
    if not username or not username.strip():
        raise ValueError("Username required")

    if not password or not password.strip():
        raise ValueError("Password required")

    user = User.query.filter_by(username=username.strip()).first()

    if not user or user.password != password:
        raise ValueError("Invalid credentials")

    return user