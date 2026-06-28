#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Superuser auto create - username env nundi teeskuntadi
python manage.py createsuperuser --noinput || echo "Superuser already exists, skipping."
