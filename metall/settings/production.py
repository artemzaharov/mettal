from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = "Fake key"

CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://spbvtormetlom.ru", "https://www.spbvtormetlom.ru", "https://spbvtormetlom.ru", ]
ALLOWED_HOSTS = ["localhost","server", "http://spbvtormetlom.ru", "https://www.spbvtormetlom.ru"]
