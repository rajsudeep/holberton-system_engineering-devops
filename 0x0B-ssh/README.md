# SSH
## Concepts:
* [SSH Essentials](./https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config File](./https://www.ssh.com/ssh/config/)
* [How SSH Works](./https://www.youtube.com/watch?v=ORcvSkgdA58)
* [SSH Crash Course](./https://www.youtube.com/watch?v=hQWRp-FdTpc)
### [0. Use a private key](./0-use_a_private_key)
> Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu
### [1. Create an SSH key pair](./1-create_ssh_key_pair)
> Write a Bash script that creates an RSA key pair
> * Name of the created private key must be holberton
> * Number of bits in the created key to be created 4096
> * The created key must be protected by the passphrase betty
### [2. Client configuration file](./2-ssh_config)
> Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
> * Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
> * Your SSH client configuration must be configured to refuse to authenticate using a password
### [Client configuration file (w/ Puppet)](./4-puppet_ssh_config.pp)
> Set up your client SSH configuration file so that you can connect to a server without typing a password