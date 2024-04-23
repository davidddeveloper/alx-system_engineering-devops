# Puppet manifest to install flask

# Package resource to install pip
package { 'python3-pip':
  ensure => installed,
}

# Package resource to install flask using pip
package { 'flask':
  ensure   => '2.1.0', # Version of Flask
  provider => 'pip3', # Use pip to install flask
  require  => Package['python3-pip'], # Ensure that pip is installed 
}
