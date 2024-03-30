# This Puppet manifest kills all processes named 'killmenow' using pkill.

exec { 'kill_killmenow_processes':
 command => '/usr/bin/pkill -f killmenow',
 path    => ['/usr/bin', '/bin'],
 onlyif => '/usr/bin/pgrep -f killmenow',
}
