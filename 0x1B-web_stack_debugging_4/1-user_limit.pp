# a puppet manifest that increases the number of number of open files for the user holberton

exec {'hard_limit':
  command => "sed -i 's/^holberton hard nofile [0-9]\+/holberton hard nofile 100/' /etc/security/limits.conf"
  path    => ['usr/bin', '/bin']
}

exec {'soft_limit':
  command => "sed -i 's/^holberton soft nofile [0-9]\+/holberton soft nofile 50/' /etc/security/limits.conf"
  path    => ['/usr/bin', '/bin']
}
