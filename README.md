# 🚀 Task Management System

![CI](https://github.com/StanleyHubGit/Final-Project-UAS-Software-Testing/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Aplikasi web sederhana berbasis **Flask** untuk mengelola task (CRUD) dengan fitur autentikasi, automated testing, dan CI/CD menggunakan GitHub Actions.

---

## 📌 Deskripsi Sistem

Task Management System memungkinkan pengguna untuk:

* Membuat task
* Melihat daftar task
* Menandai task sebagai selesai
* Menghapus task

### ✨ Fitur Tambahan

* 🔐 Login & Register user
* ✅ Validasi input (password kuat)
* 💾 Penyimpanan data menggunakan SQLite
* 🧪 Automated testing (unit & integration)
* 🔄 CI/CD dengan GitHub Actions

---

## 🏗️ Arsitektur Aplikasi

```
Final-Project-UAS-Software-Testing/
│
├── app/
│   ├── __init__.py        # Inisialisasi Flask & database
│   ├── models.py          # Model database (User, Task)
│   ├── routes.py          # Endpoint API & halaman web
│   ├── services.py        # Logika bisnis task
│   └── auth_service.py    # Logika autentikasi user
│
├── templates/
│   ├── index.html         # Halaman utama task
│   ├── login.html         # Halaman login
│   └── register.html      # Halaman register
│
├── tests/
│   ├── test_services.py   # Unit test logic
│   ├── test_routes.py     # Integration test API
│   └── test_auth.py       # Test autentikasi
│
├── .github/workflows/
│   └── ci.yml             # GitHub Actions CI
│
├── run.py                 # Entry point aplikasi
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚙️ Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/StanleyHubGit/Final-Project-UAS-Software-Testing.git
cd Final-Project-UAS-Software-Testing
```

---

### 2. Buat Virtual Environment

```bash
python -m venv venv
```

Aktifkan:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Jalankan Aplikasi

```bash
python run.py
```

Buka di browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Menjalankan Testing

```bash
pytest --cov=app --cov-report=term-missing
```

### ✅ Hasil yang Diharapkan

* Unit Test ✔️
* Integration Test ✔️
* Coverage ≥ 90%

---

## 🔄 Continuous Integration (CI)

Project ini menggunakan **GitHub Actions**.

Pipeline otomatis berjalan saat:

* Push ke repository
* Pull request

### ⚙️ Pipeline akan:

* Install dependencies
* Menjalankan semua test
* Menghitung test coverage

📁 File konfigurasi:

```
.github/workflows/ci.yml
```

---

## 📊 Test Coverage

* 🎯 Target minimal: **60%**
* ✅ Coverage saat ini: **100%**

---

## 🎯 Fitur Utama

* ✔️ CRUD Task
* ✔️ Login & Register
* ✔️ Validasi password (8+ karakter, angka & simbol)
* ✔️ Database SQLite
* ✔️ Automated Testing
* ✔️ CI/CD dengan GitHub Actions

---

## 🧰 Teknologi yang Digunakan

| Bagian   | Teknologi          |
| -------- | ------------------ |
| Backend  | Python 3.10, Flask |
| Database | SQLite             |
| Testing  | Pytest, pytest-cov |
| CI/CD    | GitHub Actions     |
| Frontend | HTML, Bootstrap    |

---

## 🔐 Validasi Keamanan

* Password minimal:

  * 8 karakter
  * Mengandung huruf
  * Mengandung angka
  * Mengandung simbol
* Username harus unik
* Error handling pada setiap endpoint

---

## 👨‍💻 Author

Nama: **Stanley Lim**
Mata Kuliah: **Software Testing**

---

## 🎯 Status Project

✅ Final Project
✅ CI/CD Active
✅ Tested (Unit + Integration)
✅ Production Ready (Basic Level)
