from flask import Flask
from app.routes import main_blueprint

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_pyfile('../config.py')

    # Register blueprints
    app.register_blueprint(main_blueprint)

    return app
