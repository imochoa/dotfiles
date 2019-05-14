#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
PROGRAM="i3"

if [[ "$INSTALL_I3" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y i3
	else   
	echo "Not installing $PROGRAM";
fi

############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
