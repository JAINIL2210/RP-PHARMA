import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'rp-pharma-secure-secret-key-2026-global-b2b')
    
    # Database Configuration (SQLite default with Vercel /tmp support and MySQL / Postgres support)
    if os.environ.get('VERCEL'):
        db_path = "/tmp/rp_pharma.db"
    else:
        db_path = str(BASE_DIR / 'instance' / 'rp_pharma.db').replace('\\', '/')
        
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI',
        f"sqlite:///{db_path}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Uploads Configuration
    if os.environ.get('VERCEL'):
        UPLOAD_FOLDER = '/tmp/uploads'
    else:
        UPLOAD_FOLDER = str(BASE_DIR / 'app' / 'static' / 'uploads')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 10 * 1024 * 1024))  # 10MB limit
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'webp'}
    ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}
    
    # Security & Session
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 86400  # 24 hours in seconds


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    SESSION_COOKIE_SECURE = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
