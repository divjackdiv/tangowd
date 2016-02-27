"""
Django settings for AdeleWebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '00yv*90knm6@6apqvb+5--lj%=b_+y@f&$)$=y69jf0%9fajzs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False



# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'rango',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)
PASSWORD_HASHERS = (
	'django.contrib.auth.hashers.PBKDF2PasswordHasher',
	'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)

ROOT_URLCONF = 'tango_with_django_project.urls'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'

SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LOGIN_URL = "/accounts/login"
LOGIN_REDIRECT_URL = "/accounts/profile"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/' # You may find this is already defined as such.

MEDIA_URL = '/static/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')


STATICFILES_DIRS = (
    STATIC_PATH,
    MEDIA_ROOT,
)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] #TODO
#SECURITY

#CSRF_COOKIE_HTTPONLY = True
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#X_FRAME_OPTIONS = 'DENY'

#SECURE_HSTS_SECONDS = 3600
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER =True
#SECURE_SSL_REDIRECT = True
#SESSION_EXPIRE_AT_BROWSER_CLOSE=True

# REGISTRATION
#REGISTRATION_OPEN = True                # If True, users can register
#ACCOUNT_ACTIVATION_DAYS = 1     # One-week activation window; you may, of course, use a different value.
#REGISTRATION_AUTO_LOGIN = False  # If True, the user will be automatically logged in.
#LOGIN_REDIRECT_URL = '/trustworthybank/'  # The page you want users to arrive at after they successful log in
#LOGIN_URL = '/trustworthybank/login/'  # The page users are directed to if they are not logged in,


TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
    TEMPLATE_PATH + "/rango/"
)
