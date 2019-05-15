#!/usr/bin/env bash


############
# setup    #
############

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )";
PREV_DIR=$(pwd);
TMP_DIR=/tmp/auto-install-tmp-dir${RANDOM};
mkdir -p ${TMP_DIR};


cd ${SCRIPTPATH};

echo "Choose a configuration:";

CONFIG_FILE=$(find configs/ -type f -iname '*.sh' | dmenu);

. ${CONFIG_FILE};


if [[ -z "$CHOSEN_CONFIG" ]]; 
then    
	echo "NO CONFIG CHOSEN! You need to source one of the files in [$SCRIPTPATH/configs] first";
	exit 125;
else   
	echo "Starting the script with the configuration: [$CHOSEN_CONFIG]";
fi;



############
# programs #
############
sudo apt-get update && sudo apt-get upgrade -y;

install_envvar () {
	VAL=$(echo $echo ${!1}); 
	echo $VAL;
	
	if [[ "${VAL:-false}" == true ]] 
	then 
		echo "Flag set to true: [$1] > running [$2]"; 
		eval $2;
	else
		echo "Flag not true: [$1]"; 
	fi
}

for i in $(find scripts -type f -iname '*.sh'); 
do
	echo "Running: ${i}";
	. $i;
done;
	
sudo apt-get autoremove -y

############
# fonts    #
############
# . fonts/install-fonts.sh;

############
# images   #
############

for i in $(find images -type f -iname '*.sh'); 
do
	echo "Running: ${i}";
	. $i;
done;
# find images -type f -iname '*.sh' -exec . {} \; 

############
# cleanup  #
############

function finish {
	  # Your cleanup code here
	  rm -rf ${TMP_DIR};
	  cd ${PREV_DIR};

  }
trap finish EXIT
