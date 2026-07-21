#!/usr/bin/env bash
set -e

# Устанавливаем UV
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Устанавливаем зависимости (создаст .venv)
uv sync

# Собираем статику
uv run python3 manage.py collectstatic --no-input

# Сброс PostgreSQL для чистых миграций
uv run python3 -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
import django
django.setup()
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('DROP SCHEMA IF EXISTS public CASCADE')
    cursor.execute('CREATE SCHEMA public')
    cursor.execute('GRANT ALL ON SCHEMA public TO public')
print('Database schema reset')
"

# Применяем миграции
uv run python3 manage.py migrate
