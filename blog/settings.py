import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$1h#eqs+&td+z4co=0b-13=*!6k(bh7&f9tzr9fd-yci6-z@6d'

# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = ['luk-blog.herokuapp.com']
ALLOWED_HOSTS = ['*','luk-blog.herokuapp.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'allauth',
    'crispy_forms',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'django.contrib.postgres',

    'ckeditor',
    'ckeditor_uploader',

    'post',
    'search',
    'taggit',

]



CKEDITOR_UPLOAD_PATH = "ckeditor"

CKEDITOR_CONFIGS = {
    "default": {
        'toolbar': 'Custom',
        'height': 'auto',
        'width': 'auto',
        'toolbar_Custom': [
            ['Bold', '-','Image'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source','codesnippet'],

        ],
       
    },
    'special': {
        'toolbar': 'Special',
        'toolbar_Special': [
            ['Bold', 'Image','Link','Unlink', 'CodeSnippet'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['RemoveFormat', 'Source','codesnippet'],


        ],
        'extraPlugins':'codesnippet',
    }

}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

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

WSGI_APPLICATION = 'blog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8ias1c1glbma2',
        'USER': 'hlmrxaezvtcmze',
        'PASSWORD':'0a4f696842599667464cab03f1b5126a66589800f64f861cca680f40d8f9eebf',
        'HOST': 'ec2-54-211-174-60.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd4b1kbnpcccam5',
#         'USER': 'levtayewoatjcg',
#         'PASSWORD':'230a73672c40a9943ca7e6346b78045f385da6cb8947c46d944654a12677e4d6',
#         'HOST': 'ec2-3-224-157-224.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap4'



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'AKIAVR6PCI4EKPRKW4H5'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME ='sylarport'
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com.s3.amazonaws.com"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_QUERYSTRING_AUTH = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sylarnano688@gmail.com'
EMAIL_HOST_PASSWORD = 'ozaxdfucozadbnyu'