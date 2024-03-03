#!/bin/sh
set -e

echo "Check postgres service availability"
python ~/check_service.py --service-name "${DATABASE_NAME}" --ip "${DATABASE_HOST}" --port "${DATABASE_PORT}"

echo "Apply database migrations"
python src/manage.py migrate --noinput

echo "Collecting static files"
python src/manage.py collectstatic --noinput

echo "Running app with gunicorn"

gunicorn --env DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE}" --user api --bind 0.0.0.0:8000  core.wsgi

exec "$@"
