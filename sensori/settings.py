"""
Django settings for sensori project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@fc__lzd#z%j5t)hts+628%$x$*j4af#os=@c^peakl02g4j)!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', #Gestisce l'interfaccia di amministrazione.
    'django.contrib.auth', #Gestisce l'autenticazione e i permessi degli utenti.
    'django.contrib.contenttypes', #Supporta tipi di contenuto generici per il framework.
    'django.contrib.sessions', #Gestisce le sessioni utente.
    'django.contrib.messages', #Consente di visualizzare messaggi temporanei (es. messaggi di successo o errore).
    'django.contrib.staticfiles', #Gestisce file statici come CSS, immagini e JavaScript.

    'gestioneSensori.apps.GestionesensoriConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sensori.urls'

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

WSGI_APPLICATION = 'sensori.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Il backend da usare (in questo caso MySQL).
        'NAME':'mydb',                          # Nome del database.
        'USER': 'root',                      # Nome utente per accedere al database.
        'PASSWORD': 'MySQL2024',                # Password dell'utente per accedere al database.
        'HOST': 'localhost',                    # Indirizzo del database (localhost significa locale).
        'PORT': '3306',                         # Porta su cui il database è in ascolto (di default per MySQL è 3306)
        'TEST': {
            'NAME': 'test_db',
        },
    }
}

IS_TESTING = False
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/' #indica il path in cui si trovano le risorse statiche (file css)

STATICFILES_DIRS = [
    "gestioneSensori/static",  # Optional: Global static directory (if needed)
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
