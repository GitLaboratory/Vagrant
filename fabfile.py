from cuisine import *
from fabric.api import *

############################
# Connect "Secure" server. #
############################
def connect():
	""" Virtual machine host. """
	env.user = 'vagrant'
	env.hosts = ['127.0.0.1:2222']
	result = local('vagrant ssh-config | grep IdentityFile', capture = True)
	env.key_filename = result.lstrip('IdentityFile').strip()

###########
# Update. #
###########
def setup_update():
	""" Update package. """
	sudo('apt-get --yes update')
	sudo('aptitude -y update')

############
# Upgrade. #
############
def setup_upgrade():
	""" Upgrade package. """
	sudo('apt-get --yes upgrade')
	sudo('aptitude -y upgrade')

#################
# Setup locale. #
#################
def setup_locale():
	""" Set "UTF-8" locale. """
	sudo('export LC_ALL=en_US.UTF-8')

#############################
# Setup "Air Time: S.A.B.S. #
#############################
def setup_audio():
	""" Install "Air Time: S.A.B.S. """
	sudo('echo "" >> "/etc/apt/sources.list"')
	sudo('echo "# Name: Air Time: S.A.B.S." >> "/etc/apt/sources.list"')
	sudo('echo "# Link: http://www.sourcefabric.org/" >> "/etc/apt/sources.list"')
	sudo('echo "deb http://apt.sourcefabric.org/ precise main" >> "/etc/apt/sources.list"')
	sudo('apt-get --yes update')
	sudo('apt-get --force-yes -y install sourcefabric-keyring')
	sudo('apt-get --yes update')
	sudo('apt-get --yes install airtime')

##############################
# Setup install "PostgreSQL" #
##############################
def setup_base():
	""" Install data base server. """
	sudo('apt-get --yes install postgresql')

##################
# Show encoding. #
##################
def setup_base_encoding():
	""" Encoding "PostgreSQL" """
	sudo('sudo -u postgres psql -c "SHOW SERVER_ENCODING"')

#######################
# Web server "Apache" #
#######################
def setup_server():
	""" Setting's host. """
	sudo('mv "/etc/apache2/sites-enabled/000-default" "/etc/apache2/sites-enabled/"')
	sudo('service apache2 restart')

##########
# Setup. #
##########
def setup():
	""" Deploy basic package's. """
	setup_locale()
	setup_update()
	setup_upgrade()
	setup_base()
	setup_base_encoding()
	setup_audio()
	setup_server()
