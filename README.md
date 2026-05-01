# Task Management System

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

Fitur utama:
- Autentikasi user (login & register)
- Validasi password (minimal 8 karakter, angka, dan simbol)
- Penyimpanan data menggunakan SQLite
- UI sederhana menggunakan HTML + Bootstrap

---

## 🏗️ Arsitektur Aplikasi
Task-Management-System/
│
├── app/
│ ├── init.py # Inisialisasi Flask & database
│ ├── models.py # Model database (User, Task)
│ ├── routes.py # Endpoint utama
│ ├── services.py # Logika bisnis task
│ ├── auth_service.py # Logika autentikasi
│
├── templates/
│ ├── index.html # Halaman utama task
│ ├── login.html # Halaman login
│ ├── register.html # Halaman register
│
├── tests/
│ ├── test_services.py # Unit test logic
│ ├── test_routes.py # Integration test API
│ ├── test_auth.py # Test autentikasi
│
├── .github/workflows/
│ └── ci.yml # GitHub Actions CI
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

Aktifkan:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Jalankan Aplikasi
python run.py

Buka browser:
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

Pipeline akan:

Install dependencies
Menjalankan test
Menghitung test coverage

File konfigurasi:
.github/workflows/ci.yml

📊 Test Coverage
Target minimal: 60% ✅
Hasil: ~90% ✅

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
Bootstrap (UI)

👨‍💻 Author

Nama: Stanley Lim
Mata Kuliah: Software Testing