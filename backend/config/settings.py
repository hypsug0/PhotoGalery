"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from decouple import config
from dj_database_url import parse as db_url


def gettext(s):
    """Lambda getters function"""
    return s


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="625a5459bc6e0d2e5227f9d7ec697c4a473f8697a84f5f7c8a",
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=False)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "sinp_organisms": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="127.0.0.1,localhost,0.0.0.0",
)

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="http://127.0.0.1,http://localhost,http://0.0.0.0",
)


# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.gis",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_gis",
    "core",
    "core.user",
    "core.auth",
    "galery",
    # "user",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    "default": config(
        "DATABASE_URL", default="sqlite:///db.sqlite3", cast=db_url
    )
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation." "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


LANGUAGES = (
    ("fr", gettext("French")),
    ("en", gettext("English")),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "fr"

MODELTRANSLATION_LANGUAGES = ("fr", "en")

# MODELTRANSLATION_FALLBACK_LANGUAGES = {"default": ("fr","en"), "en": ("fr",)}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_HOST = config("EMAIL_HOST", default="smtp.mail.net")
EMAIL_PORT = config("EMAIL_PORT", cast=int, default=465)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="<MyEmailPwd>")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="username@email.net")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)


# APPLICATION SPECIFICS
MEDIA_UPLOAD = "media/"
print("BASE_DIR", BASE_DIR)
MEDIA_ROOT = BASE_DIR / MEDIA_UPLOAD
print("MEDIA_ROOT", MEDIA_ROOT)
# print("MEDIA_ROOT", MEDIA_ROOT)
MEDIA_URL = "api/v1/media/"
# DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"


AUTH_USER_MODEL = "core_user.User"
