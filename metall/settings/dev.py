from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-67-r&^f89dg!6%vk3o%qu7vf1o9$t5yzwy_x%vq$zw+2&oe4m7"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok.io', "server"]
# CSRF_TRUSTED_ORIGINS = ["https://a81d-83-50-248-74.ngrok.io/",]
CSRF_TRUSTED_ORIGINS = ["http://localhost",]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
