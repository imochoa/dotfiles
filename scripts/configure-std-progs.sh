#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

install_envvar CONFIGURE_VIM "cp ${SCRIPTPATH}/../dotfiles/.vimrc{,.local} ~/";
install_envvar CONFIGURE_BASH "cp ${SCRIPTPATH}/../dotfiles/.bash{rc,_profile,_aliases} ~/";

#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
