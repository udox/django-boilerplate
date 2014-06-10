from www.conf.settings import *

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

WSGI_APPLICATION = 'www.conf.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name}}dev',
        'USER': '{{ project_name}}_dev',
        'PASSWORD': '{{ project_name}}_dev',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'autocommit': True,
        },

    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8080/solr4/{{ project_name}}_dev',
    },
}
