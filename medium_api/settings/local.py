from .base import * #noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="rPalOlvWZ-7HkF-Qc1bWnk-jD5D66Gts2sbjj1Dg8thrkfZEYhk"),

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]