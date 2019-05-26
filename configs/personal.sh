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
	echo "You need to source the file *. file.sh*, not execute it!";
	exit 125;
	export CHOSEN_CONFIG=`basename "$0"`;

fi

echo "chose config-> [$CHOSEN_CONFIG]";

##########
# Manual #
########## 

# SCOPE:
# - SYSTEM: System-wide installation
# - USER: (default) install only on the current $USER
# export SCOPE=SYSTEM
export SCOPE=USER

#######################
# Programs to install #
#######################
export INSTALL_I3=true;
export INSTALL_GIT=true;
export INSTALL_TREE=true;
export INSTALL_WGET=true;
export INSTALL_MUPDF=true;
export WALLPAPER_URL='https://c.wallhere.com/photos/f4/de/1920x1080_px_Brume_Hills_Mount_Everest_mountains-1214842.jpg!d';
