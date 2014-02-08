Vagrant
=======

Vagrant is open source software for creating and configuring virtual development environment's. It can be considered a wrapper around Virtual Box and configuration management software such as Chef, Salt and Puppet. Although written in Ruby, it is usable in projects written in other language's such as P.H.P., Python, Java, and C Sharp.

Installing the necessary component's
------------------------------------

    Install in O.S. Ubuntu, Version 12.04 and O.S. Ubuntu, Version 13.10
    $ sudo apt-get --yes update; sudo apt-get --yes upgrade
    $ sudo aptitude -y update; sudo aptitude -y upgrade
    $ sudo apt-get --yes install vagrant fabric git

    Install in O.S. Debian, Version 7.3
    $ sudo apt-get --yes update; sudo apt-get --yes upgrade
    $ sudo aptitude -y update; sudo aptitude -y upgrade
    $ sudo apt-get --yes install python-pip;
    $ sudo pip install fabric
    $ sudo apt-get --yes install vagrant git

Virtual machine install script's
--------------------------------

    $ git clone https://github.com/GitOrganization/Vagrant.git
    $ cd Vagrant
    $ vagrant up
    $ fab connect setup

Management Virtual Machine
--------------------------

Suspend...

    $ vagrant suspend

Resume...

    $ vagrant resume

Stop...

    $ vagrant halt

Start...

    $ vagrant up

Restart...

    $ vagrant reload

Status...

    $ vagrant status

Stop and delete all the virtual machine file's.

    $ vagrant destroy

License
-------

 * [Lesser General Public License](LICENSE)
