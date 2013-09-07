Vagrant
=======

Vagrant is open-source software for creating and configuring virtual development environments. It can be considered a wrapper around VirtualBox and configuration management software such as Chef, Salt and Puppet. Although written in Ruby, it is usable in projects written in other languages such as PHP, Python, Java, and C#.

Installing the necessary component's
------------------------------------

    $ sudo apt-get --yes update
    $ sudo apt-get --yes upgrade
    $ sudo aptitude -y update
    $ sudo aptitude -y upgrade
    $ sudo apt-get --yes install vagrant \ fabric \

Virtual machine install script's
--------------------------------

    $ git clone https://github.com/GitOrganization/Vagrant.git
    $ cd Vagrant
    $ vagrant up
    $ fab vagrant setup

License
-------

 * [Lesser General Public License](https://github.com/GitOrganization/Vagrant/blob/master/LICENSE)
