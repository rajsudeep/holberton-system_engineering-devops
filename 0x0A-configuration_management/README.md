# Configuration Management
## Concepts:
* [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
### [0. Create a file](./0-create_a_file.pp)
> Using Puppet, create a file in /tmp
> * File path is /tmp/holberton
> * File permission is 0744
> * File owner is www-data
> * File group is www-data
> * File contains I love Puppet
### [1. Install a package](./1-install_a_package.pp)
> install puppet-lint
### [2. Execute a command](./2-execute_a_command.pp)
> Using Puppet, create a manifest that kills a process named killmenow
> * Must use the exec Puppet resource
> * Must use pkill