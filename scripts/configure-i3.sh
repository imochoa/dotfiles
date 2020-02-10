#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

	
if [[ "${CONFIGURE_I3:-false}" == true ]] 
	then 
		pretty_echo 'Configuring i3'; 

        # Install programs
        sudo apt-get install -y arandr lxappearance rofi compton i3blocks xbacklight htop feh;
	#  pactl was missing. Not required on Ubuntu 18?

        # Configure xbacklight!

         sudo echo -e 'Section "Device"\nIdentifier  "Card0"\nDriver      "intel"\nOption      "Backlight"  "/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-eDP-1/intel_backlight"\nEndSection' > /etc/X11/xorg.conf
         # You might need to setup xbacklight for it to work, google it!

        # Copy over the config files

        # TODO
        cp ${SCRIPTPATH}/../dotfiles/.vimrc{,.local} ~/

        # For the audio:
fi


#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
