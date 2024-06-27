# a puppet manifest that increases the ulimit of nginx
# so that nginx can process all request at high traffic

exec { 'comment_out_ulimit':
  command => 'sudo sed -i \'s/^ULIMIT="-n [0-9]\+"/# &/\' /etc/default/nginx',
  path    => ['/usr/bin', '/bin'],
}

exec { 'the_sky_is_the_limit':
  command => 'echo \'ULIMIT="-n 4096"\' | sudo tee -a /etc/default/nginx',
  path    => ['/usr/bin', '/bin'],
  require => Exec['comment_out_ulimit'],
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => Exec['the_sky_is_the_limit'],
}
