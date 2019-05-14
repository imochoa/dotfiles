#!/usr/bin/env bash

#############
# Automatic #
#############
# export CHOSEN_CONFIG=[[ $_ != $0 ]] && echo "Script is being sourced" || echo "Script is a subshell"
# export CHOSEN_CONFIG=[[  ]] && echo "Script is being sourced" || echo "Script is a subshell"

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

echo "chose config-> [$CHOSEN_CONFIG]";

##########
# Manual #
########## 

# SCOPE:
# - SYSTEM: System-wide installation
# - USER: (default) install only on the current $USER
export SCOPE=USER

#######################
# Programs to install #
#######################
export INSTALL_I3=true;
export INSTALL_FREECAD=false;
