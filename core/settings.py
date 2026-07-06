"""
Django settings for core project.
"""

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# SECURITY
# ==========================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure--pa%6hx*g1=t=u0$+mca*v_^9(swcsm17786y46*@ikrsqi&an"
)

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "cheapskate-production.up.railway.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://cheapskate-production.up.railway.app",
]

# ==========================
# INSTALLED APPS
# ==========================

INSTALLED_APPS = [

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",

    # Local Apps
    "accounts",
    "vouchers",
    "categories",
    "claims",
    "pages",

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ==========================
# MIDDLEWARE
# ==========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# ==========================
# TEMPLATES
# ==========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# ==========================
# DATABASE
# ==========================

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# ==========================
# PASSWORD VALIDATION
# ==========================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ==========================
# LANGUAGE
# ==========================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# ==========================
# STATIC FILES
# ==========================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# ==========================
# STORAGE
# ==========================

if os.getenv("CLOUDINARY_CLOUD_NAME"):

    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
        "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
        "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
    }

    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

else:

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

# ==========================
# DEFAULT AUTO FIELD
# ==========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"