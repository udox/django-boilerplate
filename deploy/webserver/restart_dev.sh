#!/bin/bash

cd /var/django-projects/def003-website-preproduction/webserver/bin;
./stop_preproduction.sh;
sleep 2;
./start_preproduction.sh;
