"""
Django settings for admin project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os 

from pathlib import Path
SITE_ID = 1

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOSTS = ['0.0.0.0','localhost','api.'+ os.environ.get('DOMAIN_NAME'),'manage.'+ os.environ.get('DOMAIN_NAME')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('DOMAIN_NAME'), 'https://api.'+ os.environ.get('DOMAIN_NAME'),'https://manage.'+ os.environ.get('DOMAIN_NAME')]

# Application definition

INSTALLED_APPS = [
	'gregory.apps.GregoryConfig',
	'subscriptions.apps.SubscriptionsConfig',
	'rest_framework',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'sitesettings',
	'django_cron',
	'db_maintenance',
	'indexers',
	'api'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.gzip.GZipMiddleware',
	'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'admin.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
	'default': {
		# 'ENGINE': 'django.db.backends.sqlite3',
		# 'NAME': BASE_DIR / 'db.sqlite3',
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.environ.get('POSTGRES_DB'),
		'USER': os.environ.get('POSTGRES_USER'),
		'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
		'HOST': os.environ.get('DB_HOST'),
		'PORT': 5432,
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/code/static'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 10,
	# 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# MAILGUN SMTP

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_MAILGUN_API=os.environ.get('EMAIL_MAILGUN_API')
EMAIL_DOMAIN=os.environ.get('EMAIL_DOMAIN')
EMAIL_MAILGUN_API_URL=os.environ.get('EMAIL_MAILGUN_API_URL')

CRON_CLASSES = [
    'subscriptions.mercury.AdminSummary',
		'subscriptions.mercury.WeeklySummary',
		'subscriptions.mercury.TrialsNotification',
		'db_maintenance.authors.GetAuthors',
		'db_maintenance.rebuild_categories.RebuildCatsArticles',
		'db_maintenance.rebuild_categories.RebuildCatsTrials',
		'gregory.noun_phrases.NounPhrases',
		'gregory.feedreader.FeedReaderTask',
		# 'gregory.1_data_processor.DataProcessor',
		# 'gregory.2_train_models.TrainModels',
		'gregory.3_predict.RunPredictor',
		'db_maintenance.get_doi_from_crossref.GetDoiCrossRef',
]
WEBSITE_DOMAIN = 'gregory-ms.com'


# LOGS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}