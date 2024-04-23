# Puppet manifest to Kill a process called killmenow

exec { 'pkill':
  command => '/bin/pkill killmenow',
}
