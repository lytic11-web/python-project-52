#!/usr/bin/env bash
# Устанавливаем UV
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Устанавливаем зависимости (создаст .venv)
uv sync

# Собираем статику и применяем миграции через uv run
uv run python3 manage.py collectstatic --no-input
uv run python3 manage.py migrate
