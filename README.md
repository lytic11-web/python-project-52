### Hexlet tests and linter status:
[![Actions Status](https://github.com/lytic11-web/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lytic11-web/python-project-52/actions)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-52)

# Task Manager

Система управления задачами, подобная Redmine.
Приложение для управления задачами, позволяющее создавать, редактировать и отслеживать статусы задач, а также назначать исполнителей и метки.

## Демо

[https://task-manager-iplt.onrender.com](https://task-manager-iplt.onrender.com)

## Установка

```bash
Клонируйте репозиторий:
git clone https://github.com/lytic11-web/python-project-52.git

```bash
make install
make migrate
make run


## Технологический стек

- Python 3.12
- Django 5.x
- PostgreSQL / SQLite
- Bootstrap 5 (через `django-bootstrap5`)
- `django-filter` для фильтрации
- `pytest` и `pytest-django` для тестирования
- `rollbar` для мониторинга ошибок
- SonarCloud для анализа качества кода
