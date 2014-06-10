#!/bin/bash

sudo kill -9 $(cat /tmp/{{ project_name }}_dev.pid);
