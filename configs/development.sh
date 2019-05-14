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

