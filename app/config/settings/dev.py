from pathlib import Path
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import pymysql

pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'djangodb',
    'USER':'admin2',
    'PASSWORD':'password1234',
    'HOST':'127.0.0.1',
    #'HOST':'localhost',
    'PORT':'3306',
    }
}

# AUTH_USER_MODEL = 'accounts.Users'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
