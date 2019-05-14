#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
PROGRAM="FreeCAD"

if [[ "$INSTALL_FREECAD" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y freecad
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
