from core.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# Повне відключення SSL
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_HOST = None
USE_X_FORWARDED_HOST = False

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Переконайтеся, що медіа файли доступні локально
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
