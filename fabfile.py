from fabric.colors import green
from fabric.api import cd, sudo

try:
    from fabconfig import *
except ImportError:
    import sys
    print "You need to define a fabconfig.py file with your project settings"
    sys.exit()

def notify(msg):
    bar = '+' + '-' * (len(msg) + 2) + '+'
    print green('')
    print green(bar)
    print green("| %s |" % msg)
    print green(bar)
    print green('')

def update_code():
	notify("Updating code")
	with cd(env.build_path):
		sudo('if [ ! -d "%(project_path)s" ]; then git clone %(user)s@%(git_repo)s %(project_path)s; fi' % env)
	with cd(env.project_path):
		sudo('git reset HEAD --hard')
		sudo('git pull origin %(git_branch)s' % env)		

def update_virtualenv():
	notify("Updating virtualenv")
	sudo('source /usr/local/bin/virtualenvwrapper.sh && if [ ! -d "%(virtual_env_path)s" ]; then WORKON_HOME=%(virtual_env_workon_home)s mkvirtualenv %(virtual_env)s; fi' % env)
	sudo('source %(virtual_env_path)s/bin/activate && pip install -r %(requirements_file)s' % env)

def migrate_database():
	notify("Migrating database")
	sudo('source %(virtual_env_path)s/bin/activate && python %(management_script_path)s syncdb --noinput > /dev/null' % env)
	sudo('source %(virtual_env_path)s/bin/activate && python %(management_script_path)s migrate' % env)

def collect_static():
	notify("Collecting static")
	sudo('source %(virtual_env_path)s/bin/activate && python %(management_script_path)s collectstatic --noinput' % env)

def update_solr_config():
	notify("Updating solr config")
	sudo('rm -rf %(solr_core)s/* && cp -R %(solr_config)s/* %(solr_core)s' % env)
	sudo('chown -R tomcat6.tomcat6 %(solr_core)s' % env)
	sudo('service tomcat6 stop && service tomcat6 start')

def deploy_nginx_config():
	notify("Deploying nginx config")
	with cd('/etc/nginx/sites-enabled/'):
		sudo('if [ -h %(nginx_config)s ]; then unlink %(nginx_config)s; fi' % env)
		sudo('ln -s %(nginx_config_path)s' % env)
	sudo('sudo /etc/init.d/nginx reload')

def restart_webserver():
	notify("Restarting webserver")
	sudo('/bin/bash %(restart_webserver_script)s' % env)

def deploy():
	update_code()
	update_virtualenv()
	migrate_database()
	collect_static()
	update_solr_config()
	deploy_nginx_config()
	restart_webserver()
