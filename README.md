# 🚀 Task Management System

![CI](https://github.com/StanleyHubGit/Final-Project-UAS-Software-Testing/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Aplikasi web sederhana untuk mengelola task (CRUD) dengan fitur autentikasi pengguna.  
Dibangun menggunakan Flask, SQLite, dan diuji dengan pytest serta CI GitHub Actions.

---

## 📌 Deskripsi Sistem

Task Management System memungkinkan pengguna untuk:

- Registrasi dan login akun
- Menambahkan task
- Melihat daftar task
- Menandai task sebagai selesai
- Menghapus task

Fitur tambahan:
- Validasi password (minimal 8 karakter, angka, dan simbol)
- Penyimpanan data menggunakan SQLite
- Antarmuka sederhana dengan Bootstrap

---

## 🏗️ Arsitektur Aplikasi


Final-Project-UAS-Software-Testing/
│
├── app/
│ ├── init.py # Inisialisasi Flask & database
│ ├── models.py # Model database (User, Task)
│ ├── routes.py # Endpoint API & routing
│ ├── services.py # Logika bisnis task
│ ├── auth_service.py # Logika autentikasi user
│
├── templates/
│ ├── index.html # Halaman utama task
│ ├── login.html # Halaman login
│ ├── register.html # Halaman register
│
├── tests/
│ ├── test_services.py # Unit testing
│ ├── test_routes.py # Integration testing API
│ ├── test_auth.py # Testing autentikasi
│
├── .github/workflows/
│ └── ci.yml # Pipeline GitHub Actions
│
├── requirements.txt
├── run.py
└── README.md


---

## ⚙️ Cara Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/StanleyHubGit/Final-Project-UAS-Software-Testing.git
cd Final-Project-UAS-Software-Testing
2. Buat Virtual Environment
python -m venv venv
3. Aktifkan Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Jalankan Aplikasi
python run.py

Buka di browser:

http://127.0.0.1:5000
🧪 Menjalankan Testing
pytest --cov=app

Hasil:

Unit Test ✅
Integration Test ✅
Coverage ≥ 90% ✅
🔄 Continuous Integration (CI)

CI menggunakan GitHub Actions yang berjalan otomatis saat:

Push ke repository
Pull request

Pipeline melakukan:

Install dependencies
Menjalankan seluruh test
Generate test coverage

File konfigurasi:

.github/workflows/ci.yml
📊 Test Coverage
Target minimal: 60% ✅
Hasil saat ini: ~90% ✅
🎯 Fitur Utama
✔️ CRUD Task
✔️ Login & Register
✔️ Validasi input
✔️ Database SQLite
✔️ Automated Testing
✔️ CI/CD dengan GitHub Actions
📝 Teknologi yang Digunakan
Python 3.10
Flask
SQLite
Pytest
GitHub Actions
Bootstrap
👨‍💻 Author

Nama: Stanley Lim
Mata Kuliah: Software Testing