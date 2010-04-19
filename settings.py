# Django settings for ecomstore project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ENABLE_SSL = not DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'ecomstore'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a^c4@y+yn)hom&6*y*0sk5e!6fwhjey7)@bak$mulcye$$v(70'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'ecomstore.SSLMiddleware.SSLRedirect',
    'djangodblog.middleware.DBLogMiddleware',
)

ROOT_URLCONF = 'ecomstore.urls'

import os
CURRENT_PATH = \
os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')

TEMPLATE_DIRS = (
    os.path.join(CURRENT_PATH, 'templates'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'ecomstore.catalog',
    'ecomstore.utils',
    'ecomstore.cart',
    'django.contrib.flatpages',
    'ecomstore.checkout',
    'djangodblog',
)

SITE_NAME = 'Modern Musician'
META_KEYWORDS = 'Music, instruments, music accessories, musician supplies'
META_DESCRIPTION = 'Modern Musician is an online supplier of instruments, \
                            sheet music, and other accessories for musicians'
MEDIA_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
     'django.core.context_processors.auth',
     'django.core.context_processors.debug',
     'django.core.context_processors.i18n',
     'django.core.context_processors.media',
     'ecomstore.utils.context_processors.ecomstore',
)

GOOGLE_CHECKOUT_MERCHANT_ID = 'your id here'
GOOGLE_CHECKOUT_MERCHANT_KEY = 'your key here'
GOOGLE_CHECKOUT_URL = 'https://sandbox.google.com/checkout/ \
                api/v2/merchantCheckout/Merchant/' + GOOGLE_CHECKOUT_MERCHANT_ID

AUTHNET_POST_URL = 'test.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = 'your login hear'
AUTHNET_KEY = 'your key here'