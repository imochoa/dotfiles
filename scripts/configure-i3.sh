#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

	
if [[ "${CONFIGURE_I3:-false}" == true ]] 
	then 
		pretty_echo 'Configuring i3'; 

        # Install programs
        sudo apt-get install -y pactl lxappearance rofi compton i3blocks;
        # Copy over the config files
        # TODO
        cp ${SCRIPTPATH}/../dotfiles/.vimrc{,.local} ~/
fi


#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
