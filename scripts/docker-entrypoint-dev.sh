#!/bin/sh
set -e

echo "Check postgres service availability"
python ~/check_service.py --service-name "${DATABASE_HOST}" --ip "${DATABASE_HOST}" --port "${DATABASE_PORT}"

echo "Apply database migrations"
python src/manage.py migrate --noinput

echo "Running app with wsgi"

python src/manage.py runserver 0.0.0.0:8000 --settings="${DJANGO_SETTINGS_MODULE}"

exec "$@"
