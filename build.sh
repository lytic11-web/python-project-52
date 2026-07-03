#!/usr/bin/env bash
# Устанавливаем UV
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Устанавливаем зависимости глобально (для Render)
uv sync --system

# Собираем статику и применяем миграции
python3 manage.py collectstatic --no-input
python3 manage.py migrate
