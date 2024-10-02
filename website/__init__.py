from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate() 
DB_NAME = "database.db"  # Name of the SQLite database file


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Prevents warnings
    app.config['MIGRATION_DIR'] = 'website/migrations'  # Set the migration directory

    db.init_app(app)
    migrate.init_app(app, db, directory=app.config['MIGRATION_DIR'])
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment, Like

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


def create_database(app):
    # Create the database if it does not exist
    if not path.exists(path.join("website", DB_NAME)):  # Check for the database in the current directory
        with app.app_context():  # Create an application context
            db.create_all()  # Create all tables based on the models
            print("Created database!")
