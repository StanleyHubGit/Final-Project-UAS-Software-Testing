from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), 'templates'),
        static_folder=os.path.join(os.getcwd(), 'static')
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret123'

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app