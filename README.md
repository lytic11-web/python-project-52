# Task Manager

[![GitHub Actions](https://github.com/lytic11-web/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lytic11-web/python-project-52/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lytic11-web_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lytic11-web_python-project-52)

Система управления задачами, подобная Redmine. Приложение для управления задачами, позволяющее создавать, редактировать и отслеживать статусы задач, а также назначать исполнителей и метки.

##  Технологический стек

Backend: Python 3.12, Django 5.x
Database: PostgreSQL / SQLite
Frontend: Bootstrap 5 (django-bootstrap5)
Testing: pytest, pytest-django
CI/CD: GitHub Actions
Code Quality: SonarCloud


##  Требования

- Python 3.12
- Django 5.x
- PostgreSQL / SQLite

##  Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/lytic11-web/python-project-52.git
cd python-project-52

# Установите зависимости
make install

# Примените миграции
make migrate

# Запустите сервер
make run
