#!/usr/bin/env bash


############
# setup    #
############

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

if [[ -z "$CHOSEN_CONFIG" ]]; 
then    
	echo "NO CONFIG CHOSEN! You need to source one of the files in [$SCRIPTPATH/configs] first";
	exit 125;
else   
	echo "Starting the script with the configuration: [$CHOSEN_CONFIG]";
fi


############
# fonts    #
############
$SCRIPTPATH/fonts/install-fonts.sh;

############
# programs #
############
sudo apt-get update && sudo apt-get upgrade -y;

find $SCRIPTPATH/scripts -type f -iname '*.sh' -exec {} \; 
	
sudo apt-get autoremove -y

############
# cleanup  #
############

function finish {
	  # Your cleanup code here
	  echo "done!";

  }
trap finish EXIT
