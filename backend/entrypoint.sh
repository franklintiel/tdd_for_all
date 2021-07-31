#!/bin/sh
sleep 20s
echo "PostgreSQL is Up!"
echo "Executing migrations..."
python manage.py migrate --database default
echo "Migrations executed!."

echo "Static files loading..."
python manage.py collectstatic --noinput
echo "Static Files Loaded!"

echo "Starting Django Application..."
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
echo "Django Application Started!"
exec "$@"

