#!/bin/sh

# Apply database migrations
python manage.py migrate

# Create superuser if it doesn't exist
if [ ! -z "$DJANGO_SUPERUSER_USERNAME" ]; then
    python DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --noinput --username=admin --email=admin@example.com
fi

# Start the Django development server
exec "$@"
