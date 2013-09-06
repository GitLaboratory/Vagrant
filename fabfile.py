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
	sudo('echo "" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "################" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "# Charset set. #" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "################" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "en_US.UTF-8 UTF-8" >> "/var/lib/locales/supported.d/local"')

	sudo('echo "" >> "/etc/bash.bashrc"')
	sudo('echo "################" >> "/etc/bash.bashrc"')
	sudo('echo "# Charset set. #" >> "/etc/bash.bashrc"')
	sudo('echo "################" >> "/etc/bash.bashrc"')
	sudo('echo "" >> "/etc/bash.bashrc"')
	sudo('echo "LANGUAGE=en_US.UTF-8" >> "/etc/bash.bashrc"')
	sudo('echo "LANG=en_US.UTF-8" >> "/etc/bash.bashrc"')
	sudo('echo "LC_ALL=en_US.UTF-8" >> "/etc/bash.bashrc"')

	sudo('echo "" >> "/etc/bash.bashrc"')
	sudo('echo "################" >> "/etc/bash.bashrc"')
	sudo('echo "# Charset set. #" >> "/etc/bash.bashrc"')
	sudo('echo "################" >> "/etc/bash.bashrc"')
	sudo('echo "" >> "/etc/bash.bashrc"')
	sudo('echo "LC_ALL=en_US.UTF-8" > "/etc/default/locale"')
	sudo('echo "LANG=en_US.UTF-8" >> "/etc/default/locale"')

	sudo('locale-gen en_US.UTF-8')
	sudo('dpkg-reconfigure locales')

##########
# Setup. #
##########
def setup():
	""" Deploy basic package's. """
	setup_update()
	setup_upgrade()
	setup_locale()