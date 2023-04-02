from .base import *

DEBUG = False
SECRET_KEY = "django-insecure-67-r&^f89dg!6%vk3o%qu7vf1o9$t5yzwy_x%vq$zw+2&oe4m7"

try:
    from .local import *
except ImportError:
    pass

CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://spbvtormetlom.ru"]
ALLOWED_HOSTS = ["server", "http://spbvtormetlom.ru"]