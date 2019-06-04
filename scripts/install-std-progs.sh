#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


pretty_echo 'Installing programs...';
install_envvar INSTALL_GIT 'sudo apt-get install -y git';
install_envvar INSTALL_TREE 'sudo apt-get install -y tree';
install_envvar INSTALL_WGET 'sudo apt-get install -y wget';
install_envvar INSTALL_VIM 'sudo apt-get remove -y vim-tiny gvim && sudo apt-get install -y vim vim-gtk';
install_envvar INSTALL_I3 'sudo apt-get install -y i3';
install_envvar INSTALL_MUPDF 'sudo apt-get install -y mupdf';
install_envvar INSTALL_CHROME 'wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb && sudo dpkg -i /tmp/chrome.deb';
install_envvar INSTALL_GNOME_TWEAK_TOOL 'sudo apt install gnome-tweak-tool';
install_envvar INSTALL_VLC 'sudo apt-get install vlc';
install_envvar INSTALL_SLACK 'sudo apt-get install slack';
install_envvar INSTALL_STRETCHLY 'wget -c https://github.com/hovancik/stretchly/releases/download/v0.19.1/stretchly_0.19.1_amd64.deb -O /tmp/stretchly.deb && sudo dpkg -i /tmp/stretchly.deb';


install_envvar INSTALL_FIREWALL_GUI 'sudo apt-get install -y gufw';
# TODO docker CE, pycharm


#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
