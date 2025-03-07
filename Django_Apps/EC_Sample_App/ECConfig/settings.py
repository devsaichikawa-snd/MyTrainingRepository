import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$4g3-c#wwbj1q%^dg&d2acq31i1y$hfx7y-5%4w8s0(-e7fp2_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # django-allauth(必須モジュール)
    'allauth', # django-allauth(必須モジュール)
    'allauth.account', # django-allauth(必須モジュール)
    'allauth.socialaccount', # django-allauth(必須モジュール)
    'allauth.socialaccount.providers.google', # django-allauth-googleAuth
    'accounts', # 追加(アカウント)
    'stores', # 追加(ECサイト)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# All-Authの追加
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'ECConfig.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ECConfig.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Authentication&Authorization
AUTH_USER_MODEL = 'accounts.Users' # app名.クラス名
LOGIN_URL = '/accounts/user_login' # ログイン制御時のリダイレクト先
LOGIN_REDIRECT_URL = '/accounts/home' # ログイン成功後のリダイレクト先
LOGOUT_REDIRECT_URL = '/accounts/user_login' # ログアウト後のリダイレクト先

# All-Auth
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED= True # Eメールを必要とするか
ACCOUNT_UNIQUE_EMAIL = True # Eメールが一意であるか
ACCOUNT_USERNAME_REQUIRED = True # ユーザーネームを必要とするか

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

# Session
#SESSION_COOKIE_AGE = 5


# MEDIA
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Logging(ログの設定)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
        }
    },
    'handlers': {
        'console_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'timed_file_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join('logs', 'application.log'),
            'when': 'S',
            'interval': 10,
            'backupCount': 10,
            'formatter': 'simple',
            'encoding': 'utf-8',
            'delay': True,
        },
        'timed_error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join('logs', 'application_error.log'),
            'when': 'S',
            'interval': 10,
            'backupCount': 10,
            'formatter': 'simple',
            'encoding': 'utf-8',
            'delay': True,
        },
        'timed_performance_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join('logs', 'application_performance.log'),
            'when': 'S',
            'interval': 10,
            'backupCount': 10,
            'formatter': 'simple',
            'encoding': 'utf-8',
            'delay': True,
        }
    },
    'loggers': {
        'application-logger': {
            'handlers': ['console_handler', 'timed_file_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'error-logger': {
            'handlers': ['timed_error_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'performance-logger': {
            'handlers': ['timed_performance_handler'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
