#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

###############################
# font awesome .otf fonts     #
###############################

if [[ $SCOPE = "SYSTEM" ]]; 
then    
	echo "Installing system-wide fonts";
        FONT_DIR=/usr/share/fonts/opentype
	# System-wide install requires sudo
	FONT_CMD='sudo cp'
else   
	echo "Installing fonts for user $USER";
	FONT_DIR=~/.fonts/
	FONT_CMD='cp'
fi;

# Create the dir if missing
mkdir -p $FONT_DIR

# Move the fonts to the correct directory
find $SCRIPTPATH -type f -regex '.*\.\(ttf\|otf\)' -exec $FONT_CMD {} $FONT_DIR \;

# Recreate the fonts cache
fc fc-cache -f -v

############
# cleanup! #
############

function finish {
	  # Your cleanup code here
	echo "done!";
  }
trap finish EXIT
