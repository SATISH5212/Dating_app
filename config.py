import os

class Config:
    DEBUG = True
    CACHE_TYPE = 'simple'  # Change to a more robust cache store in production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')  # Set your PostgreSQL database URI here
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    DEBUG = False
