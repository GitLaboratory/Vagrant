Vagrant::Config.run do |config|
	config.vm.box = 'Vagrant'
	config.vm.box_url = 'http://files.vagrantup.com/precise64.box'
	config.vm.host_name = 'Vagrant-Virtual-Machine'

	# Multiple Network's.
	#config.vm.network :hostonly, "0.0.0.0", :netmask => "255.255.0.0"

	# Name: Secure Shell: N.P.
	# Link: https://www.wikipedia.org/wiki/Secure_Shell
	#config.vm.forward_port 22, 2222

	# Name: F.T.P.
	# Link: https://www.wikipedia.org/wiki/File_Transfer_Protocol
	config.vm.forward_port 21, 2121

	# Name: Air Time: S.A.B.S.
	# Link: http://www.sourcefabic.org/
	config.vm.forward_port 80, 5000

	# Name: Ice Cast: A.S.
	# Link: http://www.icecast.org/
	config.vm.forward_port 8000, 5050
end
