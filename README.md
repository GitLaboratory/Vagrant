Vagrant
=======

Vagrant is open source software for creating and configuring virtual development environment's. It can be considered a wrapper around Virtual Box and configuration management software such as Chef, Salt and Puppet. Although written in Ruby, it is usable in projects written in other language's such as P.H.P., Python, Java, and C#.

Installing the necessary component's
------------------------------------

    $ sudo apt-get --yes update; sudo apt-get --yes upgrade
    $ sudo aptitude -y update; sudo aptitude -y upgrade
    $ sudo apt-get --yes install vagrant fabric git

Virtual machine install script's
--------------------------------

    $ git clone https://github.com/GitOrganization/Vagrant.git
    $ cd Vagrant
    $ vagrant up
    $ fab connect setup

License
-------

 * [Lesser General Public License](https://github.com/GitOrganization/Vagrant/blob/master/LICENSE)
