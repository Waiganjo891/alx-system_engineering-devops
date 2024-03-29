#!/usr/bin/pup
# Puppet manifest to install Flask via pip3
# File: install_flask.pp
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
