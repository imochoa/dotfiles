#!/usr/bin/env python3

# std imports
import pdb

# local imports

# TODO FIX POLYBAR!
# TODO ADD Visual studio code: sudo snap install --classic code
# TODO ADD pycharm etc.

INSTALL_UI = dict()

INSTALL_UI['gtk_themes'] = r"""
#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# if [[ ${SCOPE} = "SYSTEM" ]]; 
# then    
# 	echo "Installing system-wide wallpapers";
#         IMG_DIR=/usr/local/share/wallpapers/;
# 	# System-wide install requires sudo
# 	CP_CMD='sudo cp';
# else   
# 	echo "Installing wallpapers for user $USER";
# 	IMG_DIR=~/Images/;
# 	CP_CMD='cp';
# fi;
# In general for setting themes:
sudo apt-get install -y lxappearance gtk-chtheme qt4-qtconfig
# Use sudo lxappearance and gtk-chteme for GTK2.0 and GTK+ 
# Use qtconfig and qtconfig-q4 to set the qt themes
# Note, for the qtconfig themes, delete this first (otherwise the changes don't stick!)
# rm -y ~/.config/Trolltech.conf

# From: https://www.ubuntupit.com/materia-theme-a-material-design-theme-for-gnome-gtk/
# Install Material theme requirements
sudo apt install -y gnome-themes-standard gtk2-engines-murrine libglib2.0-dev libxml2-utils;
sudo apt install -y materia-gtk-theme
# Remove with: 
# sudo rm -rf /usr/share/themes/Materia{,-compact,-dark,-dark-compact,-light,-light-compact}

sudo mkdir -p ${IMG_DIR};

echo ${WALLPAPER_URL};

# if [[ -z "${WALLPAPER_URL}" ]]; 
# then    
# 	echo "NO WLLPAPER";
#         # FONT_DIR=/usr/share/fonts/opentype
# 	# System-wide install requires sudo
# 	# FONT_CMD='sudo cp'
# else   
# 	echo "set url_ ${WALLPAPER_URL}";

# 	# FONT_DIR=~/.fonts/
# 	# FONT_CMD='cp'
# fi;

# export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/
# Otherwise the set wallpaper command (gsettings) fails, see:
# https://stackoverflow.com/questions/44934641/glib-gio-message-using-the-memory-gsettings-backend-your-settings-will-not-b
# https://github.com/conda-forge/glib-feedstock/issues/19
"""



if __name__ == '__main__':
    pass
