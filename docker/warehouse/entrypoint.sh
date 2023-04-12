#!/bin/sh

ls /api/warehouse
set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres to start..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"
