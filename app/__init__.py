from flask import Flask  # framework utama
from flask_sqlalchemy import SQLAlchemy  # ORM untuk database
import os  # untuk handle path folder

db = SQLAlchemy()  # inisialisasi database (belum terhubung ke app)

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), 'templates'),  # lokasi HTML
        static_folder=os.path.join(os.getcwd(), 'static')  # lokasi file static (css/js)
    )

    # =====================
    # CONFIG APP
    # =====================
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # gunakan SQLite sebagai database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # matikan tracking untuk performa
    app.config['SECRET_KEY'] = 'test-secret-key'  # kunci untuk session (login)
    

    # =====================
    # INIT DATABASE
    # =====================
    db.init_app(app)  # hubungkan database dengan aplikasi Flask
    

    # =====================
    # REGISTER ROUTES
    # =====================
    from .routes import main  # import blueprint
    app.register_blueprint(main)  # daftarkan route ke app

    return app