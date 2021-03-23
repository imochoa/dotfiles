#!/usr/bin/env python3

# std imports
import pdb

# local imports


# FONT DIRS!
# USER:  ~/.fonts
# GLOBAL: /usr/local/share/fonts

# TODO FIX POLYBAR!
# TODO ADD Visual studio code: sudo snap install --classic code
# TODO ADD pycharm etc.

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

INSTALL_UI = dict()

# THEMES
INSTALL_UI[
    "nordic"
] = r"""
#!/usr/bin/env bash
# https://github.com/EliverLara/Nordic/releases
TEMPDIR=$(mktemp -d -t nordic-XXXXXXXXXX)
VER=1.9.0
wget https://github.com/EliverLara/Nordic/archive/v${VER}.tar.gz --continue --output-document=${TEMPDIR}/nordic.tar.gz

sudo mkdir -p /usr/share/themes/Nordic
sudo rm -rf /usr/share/themes/Nordic
sudo mkdir -p /usr/share/themes/Nordic
sudo tar xzf ${TEMPDIR}/nordic.tar.gz --directory=/usr/share/themes/Nordic --strip-components=1
"""

INSTALL_UI[
    "gtk_themes"
] = r"""
#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# In general for setting themes:
sudo apt-get install -y lxappearance gtk-chtheme 
# qt4-qtconfig # Problematic?

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
"""

# ICON THEMES
INSTALL_UI[
    "papyrus"
] = r"""
#!/usr/bin/env bash
sudo add-apt-repository -y ppa:papirus/papirus
sudo apt install -y papirus-icon-theme
"""

INSTALL_UI[
    "numix"
] = r"""
#!/usr/bin/env bash
sudo add-apt-repository -y ppa:numix/ppa
sudo apt install -y numix-icon-theme-circle
"""

# https://c.wallhere.com/photos/f4/de/1920x1080_px_Brume_Hills_Mount_Everest_mountains-1214842.jpg!d
INSTALL_UI[
    "wallpaper"
] = r"""
#!/usr/bin/env bash
BGDIR=/usr/share/backgrounds
mkdir -p ${BGDIR}
IMG_URL='https://unsplash.com/photos/VzRKG0piEp8/download?force=true'
sudo wget ${IMG_URL} --continue --output-document=${BGDIR}/wallpaper.jpg
sudo convert ${BGDIR}/wallpaper.jpg ${BGDIR}/wallpaper.png

# # export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/
# # Otherwise the set wallpaper command (gsettings) fails, see:
# # https://stackoverflow.com/questions/44934641/glib-gio-message-using-the-memory-gsettings-backend-your-settings-will-not-b
# # https://github.com/conda-forge/glib-feedstock/issues/19
"""

if __name__ == "__main__":
    pass
