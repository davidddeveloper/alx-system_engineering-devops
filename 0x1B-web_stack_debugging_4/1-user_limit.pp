# a puppet manifest that increases the number of number of open files for the user holberton

exec {'hard_limit':
  command => "sudo sed -i 's/^holberton hard nofile [0-9]\+/holberton hard nofile 100/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin']
}

exec {'soft_limit':
  command => "sudo sed -i 's/^holberton soft nofile [0-9]\+/holberton soft nofile 50/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin']
}
