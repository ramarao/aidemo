import os

# Flask configuration
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Use the appropriate config
config = DevelopmentConfig if os.getenv("FLASK_ENV") == "development" else ProductionConfig
