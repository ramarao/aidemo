from flask import Flask
from app.routes import main_blueprint
import os

def create_app():
    app = Flask(__name__)
    
    # Load configuration using absolute path
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.py')
    app.config.from_pyfile(config_path)

    # Register blueprints
    app.register_blueprint(main_blueprint)

    return app
