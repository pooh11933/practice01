from .base import *


env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env')) # BASE_DIR + .env 경로합쳐서 local_env에

while True:
    line = local_env.readline()     # 라인 한 줄을 읽어온다
    if not line:
        break
    line = line.replace('\n', '')   # 줄바꿈줄은 라인 마지막에 항상 있기 때문에 없애줌
    start = line.find('=')          # 구분자
    key = line[:start]              # 'SECRET_KEY'
    value = line[start+1:]          # key
    env_list[key] = value           # env_list['SECRET_KEY'] = key

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
