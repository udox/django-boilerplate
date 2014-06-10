#!/bin/bash

cd /var/django-projects/{{ project_name }};
/var/virtualenvs/{{ project_name }}_dev/bin/uwsgi --env DJANGO_SETTINGS_MODULE=www.conf.dev --ini=webserver/uwsgi/dev.ini
