#!/usr/bin/env bash
set -e

# Устанавливаем UV
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Устанавливаем зависимости (создаст .venv)
uv sync

# Собираем статику и применяем миграции
uv run python3 manage.py collectstatic --no-input
uv run python3 manage.py migrate
