release: python -m playwright install chromium
web: gunicorn web:app --bind 0.0.0.0:$PORT
worker: python keep_alive.py
