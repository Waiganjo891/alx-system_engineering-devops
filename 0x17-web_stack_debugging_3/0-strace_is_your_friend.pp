# This Puppet manifest is used to fix a typo in a WordPress file to resolve a 500 error returned by Apache.

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin',
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
