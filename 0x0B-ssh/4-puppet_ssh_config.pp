# configures server so that one can connect to server without password
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}