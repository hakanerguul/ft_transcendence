#!/bin/bash
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "postgres" -U "$POSTGRES_USER" -c '\q'; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 1
done

echo "PostgreSQL is up - executing command"

# For running docker compose
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    python3 manage.py makemigrations --noinput
    python3 manage.py migrate --noinput
    python3 manage.py collectstatic --noinput
    python3 manage.py createsuperuser \
        --noinput \
        --first_name "$DJANGO_SUPERUSER_FIRSTNAME" \
        --last_name "$DJANGO_SUPERUSER_LASTNAME" \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL"
    python3 manage.py compilemessages
    daphne -b 0.0.0.0 -p 8000 main.asgi:application
fi
