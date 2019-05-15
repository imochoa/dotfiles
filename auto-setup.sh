#!/usr/bin/env bash


############
# setup    #
############

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )";
PREV_DIR=$(pwd); 
TMP_DIR=/tmp/auto-install-tmp-dir${RANDOM};
mkdir -p ${TMP_DIR};

# Move to the repo dir for the duration of this script
cd ${SCRIPTPATH};

#############################################################

# source the files in "src/"
echo "${SCRIPTPATH}";
for i in $(find src -type f -iname '*.sh'); 
do
	. $i;
done;

# Ask for a config file (if it hasn't been already set)...
if [[ -z "$CHOSEN_CONFIG" ]]; 
then    
	pretty_echo "Choose a configuration: \n(look at the top of the screen and use the arrows to select one)";
	CONFIG_FILE=$(find configs/ -type f -iname '*.sh' | dmenu -l 20);
	# ... and source it
	. ${CONFIG_FILE};
fi;

# Confirm that a config file has been sourced
if [[ -z "$CHOSEN_CONFIG" ]]; 
then    
	pretty_echo "NO CONFIG CHOSEN! You need to source one of the files in [$SCRIPTPATH/configs] first";
	exit 125;
else   
	pretty_echo "Starting the script with the configuration: [$CHOSEN_CONFIG]";
fi;



################################
# Run all scripts in "sripts/" #
################################
sudo apt-get update && sudo apt-get upgrade -y;

for i in $(find scripts -type f -iname '*.sh'); 
do
	pretty_echo "Running: ${i}";
	. $i;
done;
	
sudo apt-get autoremove -y

############
# cleanup  #
############

function finish {
	  # cleanup the tmp data
	  rm -rf ${TMP_DIR};
	  # Recover the original working directory
	  cd ${PREV_DIR};

  }
trap finish EXIT
