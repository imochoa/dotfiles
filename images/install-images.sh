#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

if [[ $SCOPE = "SYSTEM" ]]; 
then    
	echo "Installing system-wide wallpapers";
        IMG_DIR=/usr/local/share/wallpapers/;
	mkdir -p ${IMG_DIR};
	# System-wide install requires sudo
	CP_CMD='sudo cp';
else   
	echo "Installing wallpapers for user $USER";
	IMG_DIR=~/Images/;
	CP_CMD='cp';
fi;

echo ${WALLPAPER_URL};

if [[ -z "${WALLPAPER_URL}" ]]; 
then    
	echo "NO WLLPAPER";
        # FONT_DIR=/usr/share/fonts/opentype
	# System-wide install requires sudo
	# FONT_CMD='sudo cp'
else   
	echo "set url_ ${WALLPAPER_URL}";

	# FONT_DIR=~/.fonts/
	# FONT_CMD='cp'
fi;



# Create the dir if missing
# mkdir -p $FONT_DIR

# Move the fonts to the correct directory
# find $SCRIPTPATH -type f -regex '.*\.\(ttf\|otf\)' -exec $FONT_CMD {} $FONT_DIR \;

# Recreate the fonts cache
# fc fc-cache -f -v

############
# cleanup! #
############

function finish {
	  # Your cleanup code here
	echo "done!";
  }
trap finish EXIT
