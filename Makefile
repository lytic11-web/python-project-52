install:
	uv sync

collectstatic:
	uv run python3 manage.py collectstatic --no-input

migrate:
	uv run python3 manage.py migrate

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

run:
	uv run python3 manage.py runserver

shell:
	uv run python3 manage.py shell_plus --ipython

test:
	uv run python3 manage.py test

test-pytest:
	uv run pytest

test-coverage:
	uv run pytest --cov=task_manager --cov-report=xml:coverage.xml
