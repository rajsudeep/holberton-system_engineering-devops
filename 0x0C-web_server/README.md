# Web Server
## Concept Guidance:
* [lelolelolelo]()
### [0. Transfer a file to your server](./0-transfer_file)
> Write a Bash script that transfers a file from our client to a server:
> * Parameter 1: The path to the file to be transferred
> * Parameter 2: The IP of the server we want to transfer the file to
> * Parameter 3: The username scp connects with
> * Parameter 4: The path to the SSH private key that scp uses
> * scp must transfer the file to the user home directory ~/
> * Strict host key checking must be disabled when using scp
### [1. Install nginx web server](./1-install_nginx_web_server)
> * Install nginx on your web-01 server
> * Nginx should be listening on port 80
> * When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
> * As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements