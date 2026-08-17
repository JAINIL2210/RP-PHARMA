import os
import sys

# Ensure root directory is on Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Set Vercel environment marker
os.environ['VERCEL'] = '1'

from app import create_app

app = create_app('production')

# Required by Vercel WSGI runner
if __name__ == '__main__':
    app.run()
