import os, mimetypes
from pathlib import Path
from django.contrib.messages import constants as messages

# Fix an error with
#mimetypes.add_type('text/css', '.css', True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent.parent

HOSTNAME = "*.mydomain.com"
if 'HOSTNAME' in os.environ:
    HOSTNAME = os.environ["HOSTNAME"]

ALLOWED_HOSTS = ['*']
# Allow forms to submit
CSRF_TRUSTED_ORIGINS = ['https://' + HOSTNAME, 'http://' + HOSTNAME, 'https://*.127.0.0.1']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$d5c1280&vxrezxgv9jv0rau2zx(+ue^-0)##&ly'
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites', # Needed for Oauth
    'django_user_agents',
    'sass_processor',
    'backend',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            #os.path.join(BASE_DIR, 'views'),
            BASE_DIR / 'views',
        ],
        'OPTIONS': {
            'builtins': [
                'modules.custom_tools',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
"""AUTH_PASSWORD_VALIDATORS = [
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
]"""

# Alerts
"""
MESSAGE_TAGS = {
    message.DEBUG: 'info',
    message.INFO: 'info',
    message.SUCCESS: 'success',
    message.WARNING: 'warning',
    message.ERROR: 'error',
}
"""

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = 'app/assets/'
#STATIC_URL = os.path.join(BASE_DIR, 'assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]

#For Django < 4.1
#SASS_PROCESSOR_ROOT = 'app/assets/'
#For Django >= 4.2
SASS_PROCESSOR_ENABLED = True
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]
SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'assets/scss'),
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# OAuth Config
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL='/'

# ===== Feature Flags ===== #
# All Accounts stuff was removed from this codebase but leaving here as an example on how to do feature flagging for best practices
SOCIALACCOUNT_QUERY_EMAIL = False
ACCOUNT_LOGOUT_ON_GET= False
ACCOUNT_UNIQUE_EMAIL = False
ACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_ONLY = False
PASSKEY_SIGNUP_ENABLED = False
SOCIALACCOUNT_ENABLED = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_CONFIRM_EMAIL_ON_GET= False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
