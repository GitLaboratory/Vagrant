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
	sudo('echo "###############" > "/var/lib/locales/supported.d/local"')
	sudo('echo "# Set locale. #" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "###############" >> "/var/lib/locales/supported.d/local"')
	sudo('echo "en_US.UTF-8 UTF-8" >> "/var/lib/locales/supported.d/local"')

	sudo('echo "" >> "/etc/bash.bashrc"')
	sudo('echo "###############" >> "/etc/bash.bashrc"')
	sudo('echo "# Set locale. #" >> "/etc/bash.bashrc"')
	sudo('echo "###############" >> "/etc/bash.bashrc"')
	sudo('echo "LANG=en_US.UTF-8" >> "/etc/bash.bashrc"')
	sudo('echo "LC_ALL=en_US.UTF-8" >> "/etc/bash.bashrc"')
	sudo('echo "LANGUAGE=en_US.UTF-8" >> "/etc/bash.bashrc"')

	sudo('echo "###############" > "/etc/default/locale"')
	sudo('echo "# Set locale. #" >> "/etc/default/locale"')
	sudo('echo "###############" >> "/etc/default/locale"')
	sudo('echo "LANG=en_US.UTF-8" >> "/etc/default/locale"')
	sudo('echo "LC_ALL=en_US.UTF-8" >> "/etc/default/locale"')

	sudo('locale-gen en_US.UTF-8')
	sudo('dpkg-reconfigure locales')

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
    with prefix('export LC_ALL=en_US.UTF-8'):
        sudo('apt-get --yes install postgresql')
        sudo('apt-get --yes install postgresql-9.1')
        sudo('apt-get --yes install postgresql-client-9.1')
        sudo('apt-get --yes install postgresql-contrib-9.1')
        sudo('apt-get --yes install libossp-uuid16')

################
# Show locale. #
################
def setup_base_locale():
	""" Locale data base server. """
	sudo('sudo -u postgres locale')

##################
# Show encoding. #
##################
def setup_base_encoding():
	""" Encoding data base server. """
	sudo('sudo -u postgres psql -c "SHOW SERVER_ENCODING"')

#######################
# Web server "Apache" #
#######################
def setup_server():
	""" Setting's host. """
	sudo('mv "/etc/apache2/sites-enabled/000-default" "/etc/apache2/"')
	sudo('invoke-rc.d apache2 restart', pty=False)

########################
# Install time server. #
########################
def setup_time():
	""" Install network time protocol server. """
	sudo('apt-get install ntp')

######################
# Show current time. #
######################
def setup_time_current():
	sudo('sudo date')

##########
# Setup. #
##########
def setup():
	""" Deploy basic package's. """
	setup_locale()
	setup_update()
	setup_upgrade()
	setup_base()
	setup_base_locale()
	setup_base_encoding()
	setup_time()
	setup_time_current()
	setup_audio()
	setup_server()
