# Python modules
from pathlib import Path
import os
import sys
# Django modules
from django.utils.translation import gettext_lazy as _
# Third part modules
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = config('SECRET_KEY', cast=str)

DEBUG = config('DEBUG', cast=str)

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'bootstrap5',
]

PROJECT_APPS = [
    'auths.apps.AuthsConfig',
    'dictionaries.apps.DictionariesConfig',
    'main.apps.MainConfig',
    'abstracts.apps.AbstractsConfig',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'kk'

LANGUAGES = [
    ('ru', _('Russian')),     
    ('kk', _('Kazakh')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'auths.CustomUser'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files')

DATE_FORMAT = 'd.m.Y'

DATE_INPUT_FORMATS = [
    '%Y-%m-%d',
    '%m/%d/%Y',
]

# Debug-toolbar
INTERNAL_IPS = (
    '127.0.0.1',
)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Shell-plus
SHELL_PLUS_PRE_IMPORTS = [
    ('django.db', ('connection', 'connections', 'reset_queries')),
    ('datetime', ('datetime', 'timedelta', 'date')),
    ('json', ('loads', 'dumps'))
]
SHELL_PLUS_MODEL_ALIASES = {
    'auths': {
        'CustomUser': 'U',
    },
    'dictionaries': {
        'Department': 'Dep',
        'Management': 'Man',
        'Degree': 'Deg',
    },
    'main': {
        'Holiday': 'H',
    },
}
SHELL_PLUS = 'ipython'
SHELL_PLUS_PRINT_SQL = False
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000