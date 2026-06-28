#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Auto create superuser 'mawa' if not exists
python manage.py createsuperuser --noinput || true
