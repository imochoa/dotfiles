#!/usr/bin/env bash

# https://bitbucket.org/pandozer/rofi-clipboard-manager/src/master/

(sudo apt-get install -y python-pyperclip xautomation xsel \
&& cd /opt/ \
&& sudo git clone https://bitbucket.org/pandozer/rofi-clipboard-manager.git \
&& cd rofi-clipboard-manager \
&& sudo ln -s $(realpath mclip.py) /usr/bin/mclip.py \
&& mclip.py daemon & 
    )

# Command looks like: rofi -modi "clipboard:/usr/bin/mclip.py menu" -show clipboard && /usr/bin/mclip.py paste \

############
# cleanup! #
############

function finish {
	  # Your cleanup code here
	echo "done!";
  }
trap finish EXIT
