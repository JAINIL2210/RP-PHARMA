import os
from app import create_app
from app.models import db
from app.seed_data import seed_database

env_mode = os.environ.get('FLASK_ENV', 'development')
app = create_app(env_mode)

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
        # Seed initial data if tables are freshly created
        seed_database()
        
    port = int(os.environ.get('PORT') or 5000)
    print(f"[*] RP PHARMA Corporate Portal running at: http://127.0.0.1:{port}")
    print(f"[*] Admin Portal running at: http://127.0.0.1:{port}/admin")
    print(f"[*] Default Admin Credentials: admin / Admin@RP2026")
    app.run(host='0.0.0.0', port=port, debug=True)
