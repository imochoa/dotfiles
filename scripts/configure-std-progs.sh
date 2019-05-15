#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"


# TODO distinguish between user and system?

if [[ "${CONF_BASH_ALIASES:-false}" == true ]] 
then 
	pretty_echo "Flag set to true: [CONF_BASH_ALIASES] "; #> running [$2]"; 
	# eval $2;
	cp $SCRIPTPATH/../dotfiles/.bash_aliases ~/ ;
else
	pretty_echo "Flag not true: [$1]"; 
fi;

#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
