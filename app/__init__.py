import os
from flask import Flask, render_template, request
from app.config import config
from app.models import db, Product, Category, Enquiry, SiteSetting, AdminUser
from app.seed_data import seed_database

import tempfile

def create_app(config_name=None):
    """Flask application factory."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
        
    is_serverless = os.environ.get('VERCEL') == '1' or 'AWS_LAMBDA_FUNCTION_NAME' in os.environ
    
    if is_serverless:
        app = Flask(__name__, instance_path=os.path.abspath(tempfile.gettempdir()))
    else:
        app = Flask(__name__)
        
    cfg_class = config.get(config_name, config['default'])
    app.config.from_object(cfg_class)
    
    # Safely handle directory creation without crashing on read-only serverless filesystems
    upload_folder = app.config.get('UPLOAD_FOLDER', '/tmp/uploads')
    try:
        os.makedirs(upload_folder, exist_ok=True)
        os.makedirs(os.path.join(upload_folder, 'enquiries'), exist_ok=True)
        os.makedirs(os.path.join(upload_folder, 'products'), exist_ok=True)
    except Exception as e:
        print(f"[!] Upload dir notice: {e}")

    if not is_serverless:
        try:
            os.makedirs(os.path.join(app.root_path, '..', 'instance'), exist_ok=True)
        except Exception:
            pass
    
    # Initialize extensions
    db.init_app(app)
    
    with app.app_context():
        try:
            db.create_all()
            seed_database()
        except Exception as e:
            print(f"[!] DB init notice: {e}")
    
    # Context processor to inject global settings & navigation categories into all templates
    @app.context_processor
    def inject_global_data():
        settings_dict = {}
        try:
            settings = SiteSetting.query.all()
            for s in settings:
                settings_dict[s.key] = s.value
        except Exception:
            pass
            
        pharma_cats = []
        nutra_cats = []
        try:
            pharma_cats = Category.query.filter_by(type='pharmaceutical', is_active=True).order_by(Category.display_order).all()
            nutra_cats = Category.query.filter_by(type='nutraceutical', is_active=True).order_by(Category.display_order).all()
        except Exception:
            pass

        return {
            'site_settings': settings_dict,
            'pharma_nav_categories': pharma_cats,
            'nutra_nav_categories': nutra_cats,
            'current_year': 2026,
            'current_path': request.path
        }
        
    # Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500
        
    # Register Blueprints
    from app.routes.main import main_bp
    from app.routes.products import products_bp
    from app.routes.enquiries import enquiries_bp
    from app.routes.api import api_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(enquiries_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app
