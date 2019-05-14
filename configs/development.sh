#!/usr/bin/env bash

#############
# Automatic #
#############

if [[ $_ != $0 ]]; 
then   
	# Script is being sourced	
	# echo "Sourcing";
	export CHOSEN_CONFIG=${BASH_SOURCE[0]};

else   
	# Script is in a subshell
	# echo "subshell";
	echo "You need to source the file *. file.sh*, not execute it!";
	exit 125;
	export CHOSEN_CONFIG=`basename "$0"`;

fi

echo "Chose config-> [$CHOSEN_CONFIG]";

##########
# Manual #
########## 

# SCOPE:
# - SYSTEM: System-wide installation
# - USER: (default) install only on the current $USER
export SCOPE=SYSTEM;


#######################
# Programs to install #
#######################
export INSTALL_I3=true;
export INSTALL_FREECAD=true;
export INSTALL_GIT=true;
export INSTALL_TREE=true;
export INSTALL_WGET=true;
