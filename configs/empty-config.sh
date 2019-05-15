#!/usr/bin/env bash

# Empty config file

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
	# export CHOSEN_CONFIG=`basename "$0"`;

fi;

echo "Chose config-> [$CHOSEN_CONFIG]";
