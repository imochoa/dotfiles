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

# TODO Included in nerdfonts?
INSTALL_UI['fontawesome'] = r"""
#!/usr/bin/env bash
apt install fonts-font-awesome
sudo apt-get install fonts-noto-color-emoji
fc-cache -f -v
"""

INSTALL_UI['nerdfonts'] = r"""
#!/usr/bin/env bash

VER=2.1.0

sudo apt-get install -y wget

INSTALL_DIR=/usr/local/share/fonts/nerdfonts
FONT_TEMPDIR=$(mktemp -d -t fonts-XXXXXXXXXX)
wget https://github.com/ryanoasis/nerd-fonts/archive/v${VER}.tar.gz --continue --output-document=${FONT_TEMPDIR}/nerdfonts.tar.gz

tar xzf ${FONT_TEMPDIR}/nerdfonts.tar.gz --directory=${FONT_TEMPDIR} --strip-components=1
sudo ${FONT_TEMPDIR}/install.sh --install-to-system-path
fc-cache -f -v -r
"""

INSTALL_UI['siji'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y git \
&& cd /tmp/ \
&& git clone https://github.com/stark/siji \
&& cd siji \
&& ./install.sh \
&& fc-cache -f -v -r
# By default Siji will be installed in your $HOME/.fonts directory, it will be created if the directory is non-existent.
# If you wish to install Siji in another directory then run the install.sh script with the -d flag and specify the font directory as an argument.
"""


# TODO?
# [nvr]ignacio@ignacio-XPS-13-9370:/tmp/fonts-NAp5GtykHG$ find ${FONT_TEMPDIR} -type f \( -iname \*.  otf -o -iname \*.ttf \)

INSTALL_UI['feather'] = r"""
#!/usr/bin/env bash

VER=2.1.0

sudo apt-get install -y wget

# INSTALL_DIR=/usr/local/share/fonts/nerdfonts
FONT_TEMPDIR=$(mktemp -d -t fonts-XXXXXXXXXX)
# wget https://github.com/ryanoasis/nerd-fonts/archive/v${VER}.tar.gz --continue --output-document=${FONT_TEMPDIR}/nerdfonts.tar.gz
wget https://github.com/Keyamoon/IcoMoon-Free/archive/master.tar.gz  --continue --output-document=${FONT_TEMPDIR}/icomoon.tar.gz
tar xzf ${FONT_TEMPDIR}/icomoon.tar.gz --directory=${FONT_TEMPDIR} --strip-components=1
sudo ${FONT_TEMPDIR}/install.sh --install-to-system-path
fc-cache -f -v -r
"""
# feather
# 

INSTALL_UI['feather'] = r"""
#!/usr/bin/env bash

VER=2.1.0

sudo apt-get install -y wget

# INSTALL_DIR=/usr/local/share/fonts/nerdfonts
FONT_TEMPDIR=$(mktemp -d -t fonts-XXXXXXXXXX)
# wget https://github.com/ryanoasis/nerd-fonts/archive/v${VER}.tar.gz --continue --output-document=${FONT_TEMPDIR}/nerdfonts.tar.gz
wget https://github.com/Keyamoon/IcoMoon-Free/archive/master.tar.gz  --continue --output-document=${FONT_TEMPDIR}/icomoon.tar.gz
tar xzf ${FONT_TEMPDIR}/icomoon.tar.gz --directory=${FONT_TEMPDIR} --strip-components=1
sudo ${FONT_TEMPDIR}/install.sh --install-to-system-path
fc-cache -f -v -r
"""


INSTALL_UI['jetbrains-mono-font'] = r"""
#!/usr/bin/env bash
# https://github.com/JetBrains/JetBrainsMono
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)"
"""

if __name__ == '__main__':
    pass
