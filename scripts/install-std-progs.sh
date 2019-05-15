#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

install_envvar INSTALL_GIT 'sudo apt-get install -y git';
install_envvar INSTALL_TREE 'sudo apt-get install -y tree';
install_envvar INSTALL_WGET 'sudo apt-get install -y wget';
install_envvar INSTALL_FREECAD 'sudo apt-get install -y freecad';
install_envvar INSTALL_I3 'sudo apt-get install -y i3';
install_envvar INSTALL_I3 'sudo apt-get install -y i3';
install_envvar INSTALL_MUPDF 'sudo apt-get install -y mupdf';

#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
