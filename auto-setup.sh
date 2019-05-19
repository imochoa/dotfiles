#!/usr/bin/env bash


############
# setup    #
############

REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PREV_DIR=$(pwd); 
TMP_DIR=/tmp/auto-install-tmp-dir${RANDOM};
mkdir -p ${TMP_DIR};

# Move to the repo dir for the duration of this script
cd ${REPO_DIR};

#############################################################

# source the files in "src/"
echo "${REPO_DIR}";
for i in $(find ${REPO_DIR}/src -type f -iname '*.sh'); 
do
	. $i;
done;

# Chosen a config file?
if [ -n "${CONFIG_TO_TEST}" ];  
then 
  # Control will enter here if /repo exists 
  # TODO NOT WORKING!!
  echo "existed"!; 
  source ${REPO_DIR}/configs/${CONFIG_TO_TEST};
fi;

# Loaded a config file? If not, ask for one
if [[ -z "${CHOSEN_CONFIG}" ]]; 
then    
	pretty_echo "Choose a configuration: \n(look at the top of the screen and use the arrows to select one)";
	CONFIG_FILE=$(find ${REPO_DIR}/configs/ -type f -iname '*.sh' | dmenu -l 20);
	# ... and source it
	source ${CONFIG_FILE};
fi;

# Confirm that a config file has been sourced
if [[ -z "${CHOSEN_CONFIG}" ]]; 
then    
	pretty_echo "NO CONFIG CHOSEN! You need to source one of the files in [${REPO_DIR}/configs] first";
	exit 125;
else   
	pretty_echo "Starting the script with the configuration: [${CHOSEN_CONFIG}]";
fi;



################################
# Run all scripts in "sripts/" #
################################
# sudo apt-get update already ran in one of the "src" scripts!
sudo apt-get upgrade -y;

for i in $(find ${REPO_DIR}/scripts -type f -iname '*.sh'); 
do
	pretty_echo "Running: ${i}";
	source $i;
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
