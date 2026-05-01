from flask import Blueprint, request, jsonify, render_template
from .services import add_task, get_tasks, complete_task, delete_task
from .auth_service import register_user, login_user
from flask import session, redirect, url_for

main = Blueprint('main', __name__)

# =====================
# UI ROUTES
# =====================
@main.route('/')
def index():
    if not session.get('user_id'):
        return redirect(url_for('main.login_page'))
    return render_template('index.html')

@main.route('/login-page')
def login_page():
    return render_template('login.html')

@main.route('/register-page')
def register_page():
    return render_template('register.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.login_page'))

# =====================
# TASK API
# =====================
@main.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(get_tasks())

@main.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        task = add_task(data.get('title'))
        return jsonify(task), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@main.route('/tasks/<int:id>', methods=['PUT'])
def complete(id):
    try:
        task = complete_task(id)
        return jsonify(task)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@main.route('/tasks/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        task = delete_task(id)
        return jsonify(task)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# =====================
# AUTH API
# =====================
@main.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = register_user(data.get('username'), data.get('password'))
        return jsonify({"id": user.id, "username": user.username}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@main.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = login_user(data.get('username'), data.get('password'))

        session['user_id'] = user.id 

        return jsonify({"message": "Login success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 401