#!/usr/bin/env bash

# Re-download the fonts

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

###############################
# Get font awesome .otf fonts #
###############################
FONTAWESOME_URL='https://github.com/FortAwesome/Font-Awesome/releases/download/5.8.2/fontawesome-free-5.8.2-desktop.zip' 

# DIR SHOULD NOT END IN "/"
FONTAWESOME_TMP_DIR=/tmp/fontawesome$RANDOM


mkdir -p $FONTAWESOME_TMP_DIR && rm -rfv $FONTAWESOME_TMP_DIR/*

wget -c $FONTAWESOME_URL -O $FONTAWESOME_TMP_DIR/fontawesome.zip && unzip $FONTAWESOME_TMP_DIR/fontawesome.zip -d  $FONTAWESOME_TMP_DIR

find $FONTAWESOME_TMP_DIR -type f -name "*.otf" -exec mv {} $SCRIPTPATH \;

# The directory you're looking for is /usr/share/fonts/opentype. If it's not there, you can just create it. Copy your OTF files there; this will install the font for all users. Then, recreate the fonts cache with the command sudo fc-cache -f -v.

# You can also install fonts per user at ~/.fonts/. It makes no difference whether they're in any sub-folders or what type they are. Mine, as an example, are organised by foundry.


###############################
# Get font awesome .otf fonts #
###############################

############
# cleanup! #
############

function finish {
	  # Your cleanup code here

  rm -rf $FONTAWESOME_TMP_DIR

  }
trap finish EXIT
