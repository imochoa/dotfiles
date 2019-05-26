#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pretty_echo 'Configuring the OS';

install_envvar INSTALL_MEDIA_CODECS 'sudo apt install ubuntu-restricted-extras';
install_envvar ACTIVATE_FIREWALL  'sudo ufw enable';
install_envvar REMOVE_AMAZON_LAUNCHER 'sudo apt purge -y ubuntu-web-launchers'
# TLP – Linux Advanced Power Management
install_envvar INSTALL_TLP 'sudo apt-get install -y tlp tlp-rdw && sudo tlp start'

# TODO Activate software sources? 
# The four main repositories are:
# Main - Canonical-supported free and open-source software.
# Universe - Community-maintained free and open-source software.
# Restricted - Proprietary drivers for devices.
# Multiverse - Software restricted by copyright or legal issues.

#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
