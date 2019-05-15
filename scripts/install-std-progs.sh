#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

install_envvar INSTALL_GIT 'sudo apt-get install -y git';
install_envvar INSTALL_TREE 'sudo apt-get install -y tree';
install_envvar INSTALL_WGET 'sudo apt-get install -y wget';
install_envvar INSTALL_FREECAD 'sudo apt-get install -y freecad';
install_envvar INSTALL_VIM 'sudo apt-get install -y vim';
install_envvar INSTALL_I3 'sudo apt-get install -y i3';
install_envvar INSTALL_MUPDF 'sudo apt-get install -y mupdf';
install_envvar INSTALL_CHROME 'wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O $TMP_DIR/chrome.deb && sudo dpkg -i $TMP_DIR/chrome.deb';
install_envvar INSTALL_MEDIA_CODECS 'sudo apt install ubuntu-restricted-extras';
install_envvar INSTALL_GNOME_TWEAK_TOOL 'sudo apt install gnome-tweak-tool';
install_envvar INSTALL_VLC 'sudo apt-get install vlc';
install_envvar INSTALL_SLACK 'sudo apt-get install slack';


# TODO docker CE, pycharm


#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
