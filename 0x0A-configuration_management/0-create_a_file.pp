file { '/tmp/school'
  ensure => '/tmp/school',
  content => 'I love Puppet',
  mode => '0744',
  owner => 'www-data',
  group => 'www-data'
}
