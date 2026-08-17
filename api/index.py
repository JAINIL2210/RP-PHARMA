import os
import sys
import traceback

# Ensure root directory is on Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Set Vercel environment marker
os.environ['VERCEL'] = '1'

try:
    from app import create_app
    app = create_app('production')
except Exception as e:
    sys.stderr.write(f"[FATAL VERCEL STARTUP ERROR]: {str(e)}\n")
    traceback.print_exc(file=sys.stderr)
    
    # Fallback diagnostic app: Renders the exact traceback directly if container initialization fails
    from flask import Flask, Response
    app = Flask(__name__)
    captured_err = traceback.format_exc()
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return Response(
            f"""<!DOCTYPE html>
            <html>
            <head><title>RP PHARMA - Diagnostic Log</title></head>
            <body style="font-family: monospace; padding: 2rem; background: #0A3D62; color: #fff;">
              <h2 style="color: #00E5CC;">RP PHARMA — Serverless Initialization Notice</h2>
              <p>The application encountered the following startup exception:</p>
              <pre style="background: #061527; padding: 1.5rem; border-radius: 8px; overflow-x: auto; color: #ffb86c;">{captured_err}</pre>
            </body>
            </html>""",
            status=500,
            mimetype='text/html'
        )

# Required for local testing or Vercel WSGI
if __name__ == '__main__':
    app.run()
