#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [[ ${SCOPE} = "SYSTEM" ]]; 
then    
	echo "Installing system-wide wallpapers";
        IMG_DIR=/usr/local/share/wallpapers/;
	# System-wide install requires sudo
	CP_CMD='sudo cp';
else   
	echo "Installing wallpapers for user $USER";
	IMG_DIR=~/Images/;
	CP_CMD='cp';
fi;


mkdir -p ${IMG_DIR};

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

export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/
# Otherwise the set wallpaper command (gsettings) fails, see:
# https://stackoverflow.com/questions/44934641/glib-gio-message-using-the-memory-gsettings-backend-your-settings-will-not-b
# https://github.com/conda-forge/glib-feedstock/issues/19


############
# cleanup! #
############

function finish {
	  # Your cleanup code here
	echo "done!";
  }
trap finish EXIT
