# app/__init__.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
  



def create_app():
    # Initialize and configure the app here (routes, extensions, etc.)
    from app import routes  # Import the routes module
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints or any other configuration here if needed

    return app


