from .models import User
from . import db
import re

def register_user(username, password):
    if not username or not password:
        raise ValueError("Username and password required")

    # VALIDASI PASSWORD
    if len(password) < 8:
        raise ValueError("Password minimal 8 karakter")

    if not re.search(r"[A-Za-z]", password):
        raise ValueError("Password harus mengandung huruf")

    if not re.search(r"\d", password):
        raise ValueError("Password harus mengandung angka")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError("Password harus mengandung simbol")

    if User.query.filter_by(username=username).first():
        raise ValueError("User already exists")

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def login_user(username, password):
    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        raise ValueError("Invalid credentials")

    return user