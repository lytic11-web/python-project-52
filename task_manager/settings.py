import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Загрузка переменных окружения из .env
load_dotenv()
ROLLBAR_ACCESS_TOKEN = os.getenv('ROLLBAR_ACCESS_TOKEN', '')

BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ из переменной окружения
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-change-me-in-production'
)

# Режим отладки из переменной окружения
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Разрешённые хосты из переменной окружения
ALLOWED_HOSTS = os.getenv(
    'ALLOWED_HOSTS',
    'localhost,127.0.0.1,webserver'
).split(',')

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

    # Сторонние приложения
    'django_bootstrap5',
    'rollbar',

    # Локальные приложения
    'users',
    'tasks',
]

MIDDLEWARE = [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'task_manager.wsgi.application'

# База данных через dj-database-url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    )
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Интернационализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Тип первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки аутентификации
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

# Rollbar configuration
if ROLLBAR_ACCESS_TOKEN:
    ROLLBAR = {
        'access_token': ROLLBAR_ACCESS_TOKEN,
        'environment': 'production' if not DEBUG else 'development',
        'root': str(BASE_DIR),
        'enabled': True,
    }

    # Логирование - исправленный путь!
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'rollbar': {
                'level': 'WARNING',
                'class': 'rollbar.logger.RollbarHandler',  # ← ИСПРАВЛЕНО!
            },
        },
        'loggers': {
            'django': {
                'handlers': ['rollbar'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }
