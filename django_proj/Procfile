web: gunicorn-b "0.0.0.0:$PORT" -W 3 blog_api.wsgi 
release: python manage.py migrate 