web gunicorn mysite.wsgi:application --log-file -
release: python3 manage.py inspectdb
release: python3 manage.py inspectdb > models.py
release: python3 manage.py migrate