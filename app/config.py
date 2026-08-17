import os
import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'rp-pharma-secure-secret-key-2026-global-b2b')
    
    # Check if running in Vercel / Serverless environment
    IS_SERVERLESS = os.environ.get('VERCEL') == '1' or 'AWS_LAMBDA_FUNCTION_NAME' in os.environ
    
    if IS_SERVERLESS:
        tmp_dir = os.path.abspath(tempfile.gettempdir())
        db_path = str(Path(tmp_dir) / 'rp_pharma.db').replace('\\', '/')
        db_uri = f"sqlite:///{db_path}"
        UPLOAD_FOLDER = os.path.join(tmp_dir, 'uploads')
    else:
        db_path = str(BASE_DIR / 'instance' / 'rp_pharma.db').replace('\\', '/')
        db_uri = f"sqlite:///{db_path}"
        UPLOAD_FOLDER = str(BASE_DIR / 'app' / 'static' / 'uploads')
        
    # Database Configuration (supports MySQL, Postgres or SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI',
        db_uri
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 10 * 1024 * 1024))  # 10MB limit
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'webp'}
    ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False


class TestingConfig(Config):
    """Testing environment configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig if not os.environ.get('VERCEL') else ProductionConfig
}

config_by_name = config
