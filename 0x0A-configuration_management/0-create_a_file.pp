# Puppet manifest to create a file in /tmp
# File: create_school_file.pp

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n",
}
