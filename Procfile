release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn todo_app.wsgi --log-file -