import os
import sys
import traceback
import tempfile

# Force Vercel / serverless environment flag
os.environ['VERCEL'] = '1'

# Ensure root directory is in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from app import create_app
    app = create_app('production')
except Exception as e:
    sys.stderr.write(f"[FATAL VERCEL STARTUP ERROR]: {str(e)}\n")
    traceback.print_exc(file=sys.stderr)
    
    # Robust diagnostic fallback app so that Vercel always loads cleanly
    from flask import Flask, Response
    app = Flask(__name__)
    captured_err = traceback.format_exc()
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return Response(
            f"""<!DOCTYPE html>
            <html>
            <head><title>RP PHARMA - System Notice</title></head>
            <body style="font-family: monospace; padding: 2rem; background: #0A3D62; color: #fff;">
              <h2 style="color: #00E5CC;">RP PHARMA — Serverless Initialization Notice</h2>
              <p>Startup exception details:</p>
              <pre style="background: #061527; padding: 1.5rem; border-radius: 8px; overflow-x: auto; color: #ffb86c;">{captured_err}</pre>
            </body>
            </html>""",
            status=500,
            mimetype='text/html'
        )

# Explicit top-level exports for Vercel WSGI / Python Serverless runtime
application = app
handler = app

if __name__ == '__main__':
    app.run()
