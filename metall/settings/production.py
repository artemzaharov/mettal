from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://spbvtormetlom.ru"]
ALLOWED_HOSTS = ["server", "http://spbvtormetlom.ru"]