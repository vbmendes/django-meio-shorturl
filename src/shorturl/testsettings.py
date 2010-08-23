import os

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/shorturl.db'
INSTALLED_APPS = (
    'django.contrib.sites',
    'shorturl',
)
ROOT_URLCONF = ['shorturl.urls']
SITE_ID = 1

SHORTURL_MODELS = {
    '': 'shorturl.URL',
}

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'tests', 'templates'),
)

