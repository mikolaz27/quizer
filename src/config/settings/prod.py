from config.settings.base_settings import *  # NOQA

SECRET_KEY = "django-insecure-+%hn^$e^8)u!($k@e6jaz-#9zwttnx02r9h(we)(0auge@7-#8"

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
