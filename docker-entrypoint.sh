#!/bin/sh

set -e

python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000

#exec uwsgi \
##      --http :${LISTEN_PORT} \
##      --module ${WSGI_NAME}.wsgi \
##      --workers ${WORKERS_COUNT} \
##      --ini /app/uwsgi-config.ini \
##      --master