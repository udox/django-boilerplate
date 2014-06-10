from fabric.api import env
from fabric.api import run
from fabric.operations import put, prompt
from fabric.colors import green, red
from fabric.api import local, cd, sudo


def _general_setup():
    env.user = prompt(red('Username for remote host? [default is current user] '))
    env.build_path = '/var/django-projects/'
    env.virtual_env_workon_home = '/var/virtualenvs'
    env.shell = "/bin/bash -l -i -c" 

def _configure():
    env.virtual_env_path = '%(virtual_env_workon_home)s/%(virtual_env)s' % env
    env.management_script_path = '%(project_path)s/www/manage.py' % env
    env.requirements_file = '%(project_path)s/deploy/requirements.txt' % env
    env.nginx_config_path = '%(project_path)s/deploy/nginx/%(nginx_config)s' % env
    env.git_repo = ''
    env.solr_config = '%(project_path)s/deploy/solr/conf/' % env

def dev():
    _general_setup()
    env.virtual_env = '{{ project_name }}'
    env.project_path = '%(build_path)s/{{ project_name }}_dev/' % env    
    env.nginx_config = 'dev.conf'
    env.restart_webserver_script = '%(project_path)s/deploy/webserver/restart_dev.sh' % env
    env.git_branch = 'master'
    env.hosts = ['']
    env.solr_core = '/opt/solr4/{{ project_name }}/conf/'
    _configure()
