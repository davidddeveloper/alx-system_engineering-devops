# Puppet manifest to configure a web server

# Define a file resource
# to create a file (school) in /tmp/
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
