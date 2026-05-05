from flask import Blueprint, request, jsonify, render_template  # handle route & response
from .services import add_task, get_tasks, complete_task, delete_task, update_task  # logic task
from .auth_service import register_user, login_user  # logic auth
from flask import session, redirect, url_for  # session & redirect
from .models import User  # model user

main = Blueprint('main', __name__)  # blueprint untuk modular route

# =====================
# UI ROUTES
# =====================

@main.route('/')
def index():
    user_id = session.get('user_id')  # ambil user dari session

    if not user_id:
        return redirect(url_for('main.login_page'))  # jika belum login → redirect

    user = User.query.get(user_id)  # ambil user dari database

    if not user:
        session.pop('user_id', None)  # jika user tidak ada → hapus session
        return redirect(url_for('main.login_page'))

    return render_template('index.html', username=user.username)  
    # kirim username ke HTML

@main.route('/login-page')
def login_page():
    return render_template('login.html')  # tampilkan halaman login

@main.route('/register-page')
def register_page():
    return render_template('register.html')  # tampilkan halaman register

@main.route('/logout')
def logout():
    session.pop('user_id', None)  # hapus session → logout
    return redirect(url_for('main.login_page'))  # kembali ke login


# =====================
# TASK API
# =====================

@main.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(get_tasks())  # ambil semua task (200 OK)

@main.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()  # ambil data JSON dari request
        task = add_task(data.get('title'))  # kirim ke service
        return jsonify(task), 201  # berhasil create → 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # input salah → 400

@main.route('/tasks/<int:id>', methods=['PUT'])
def complete(id):
    try:
        task = complete_task(id)  # tandai task selesai
        return jsonify(task)  # sukses → 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404  # task tidak ada → 404

@main.route('/tasks/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        task = delete_task(id)  # hapus task
        return jsonify(task)  # sukses → 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404  # task tidak ditemukan → 404

@main.route('/tasks/<int:id>', methods=['PATCH'])
def edit_task(id):
    try:
        data = request.get_json()  # ambil JSON
        task = update_task(id, data.get('title'))  # update title
        return jsonify(task)  # sukses → 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # input salah → 400


# =====================
# AUTH API
# =====================

@main.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()  # ambil data user
        user = register_user(data.get('username'), data.get('password'))  
        return jsonify({"id": user.id, "username": user.username}), 201  
        # berhasil register → 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # input salah → 400

@main.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  # ambil data login
        user = login_user(data.get('username'), data.get('password'))  

        session['user_id'] = user.id  # simpan user di session (login)

        return jsonify({"message": "Login success"})  # sukses → 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401  # login gagal → 401