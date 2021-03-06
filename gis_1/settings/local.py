from .base import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env'))
while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace("\n", "")
    start = line.find("=")
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value
SECRET_KEY = env_list["SECRET_KEY"]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}