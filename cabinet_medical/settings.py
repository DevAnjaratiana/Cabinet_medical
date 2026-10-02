"""
Django settings for cabinet_medical project.
"""

from pathlib import Path
import os
import dj_database_url
from decouple import config, Csv

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SÉCURITÉ
# ============================================================

SECRET_KEY = config(
    'SECRET_KEY',
    default='django-insecure-l(xcubr7rg4q6a8w7a)7ut%pz%=*_w-ph!i0k6gtgkt+z+$q33'
)
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='', cast=Csv())


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',   # WhiteNoise en dev
    'django.contrib.staticfiles',
    'patients',
    'medecins',
    'dashboard',
    'rendezvous',
    'consultations',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # WhiteNoise en prod
    'cabinet_medical.middleware.NoCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cabinet_medical.urls'

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

WSGI_APPLICATION = 'cabinet_medical.wsgi.application'


# ============================================================
# BASE DE DONNÉES
# ============================================================

DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL',
            default='postgres://postgres:postgres@localhost:5432/cabinet_medical'
        ),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Force l'UTF-8 (utile pour PostgreSQL avec locale française)
DATABASES['default'].setdefault('OPTIONS', {})
DATABASES['default']['OPTIONS']['client_encoding'] = 'UTF8'


# ============================================================
# MOTS DE PASSE
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================================
# INTERNATIONALISATION
# ============================================================

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Indian/Antananarivo'   # ou 'Europe/Paris' si vous préférez
USE_I18N = True
USE_TZ = True


# ============================================================
# FICHIERS STATIQUES
# ============================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # où collectstatic écrit
STATICFILES_DIRS = [BASE_DIR / 'static'] # vos fichiers sources

# WhiteNoise : compression + cache
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Médias (uploads utilisateur)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ============================================================
# DIVERS
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'