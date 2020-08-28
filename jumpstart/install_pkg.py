#!/usr/bin/env python3

# std imports
import pdb

# local imports

# TODO ADD Visual studio code: sudo snap install --classic code
# TODO ADD pycharm etc.

INSTALL_PKGS = dict()

INSTALL_PKGS['fd'] = r"""
#!/usr/bin/env bash
sudo apt install -y fd-find
"""


INSTALL_PKGS['sxiv'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y sxiv
"""

INSTALL_PKGS['neofetch'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y neofetch
"""

INSTALL_PKGS['disk_space'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y baobab
"""

INSTALL_PKGS['nodejs'] = r"""
#!/usr/bin/env bash
# https://github.com/nodesource/distributions/blob/master/README.md
# Using Ubuntu
sudo apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# [OPTIONAL] To compile and install native addons from npm you may also need to install build tools:
sudo apt-get install -y build-essential
"""


INSTALL_PKGS['python3'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y python3 python3-pip python3-venv python3-dev  build-essential libssl-dev libffi-dev  libxml2-dev libxslt1-dev zlib1g-dev
# For python+PDF
sudo apt-get install -y texlive texlive-xetex texlive-latex-extra pandoc pandoc-citeproc
# For python+postgreSQL
sudo apt install -y libpq-dev python3-dev

# Upgrade pip
sudo -H pip3  install --upgrade pip

"""


INSTALL_PKGS['polybar'] = r"""
#!/usr/bin/env bash
# TODO FONTS NOT FOUND:
# -- Font not found: fixed:pixelsize=10
# -- Font not found: unifont:fontformat=truetype
# -- Font not found: siji:pixelsize=10

# -- Trying to enable ccache
# -- Couldn't locate ccache, disabling ccache...

# Deps
sudo apt-get install -y build-essential git cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev

# optional deps
sudo apt-get install -y libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev

# i3-wm  # REMOVED it!

cd /opt
sudo git clone --recursive https://github.com/polybar/polybar.git polybar
sudo chown -R ${USER}:${USER} /opt/polybar

cd polybar
# Get new tags from remote
git fetch --tags
# Get latest tag name
latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)

# Checkout latest tag
git checkout $latestTag
 ./build.sh --all-features --gcc -f --install-config --auto
"""

INSTALL_PKGS['trash_cli'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y trash-cli
"""

INSTALL_PKGS['exfat'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y exfat-fuse exfat-utils
"""

INSTALL_PKGS['ssh'] = r"""
#!/usr/bin/env bash
# TODO PREFER XCLIP OVER XSEL
# sudo apt install -y openssh-server xsel xauth
sudo apt install -y openssh-server xclip xauth
# xsel, xauth -> so that you can share the clipboard
# using ssh -Y yourserver 
# or by setting that as the default config in ~/.ssh/config
# https://superuser.com/questions/326871/using-clipboard-through-ssh-in-vim
# ~/.ssh/config
# Host myserver
#    ForwardX11 yes
#    ForwardX11Trusted yes
"""

# TODO libreoffice broken!
INSTALL_PKGS['libreoffice'] = r"""
##!/usr/bin/env bash
#sudo apt-get remove -y libreoffice
#sudo apt-get install -y software-properties-common
#sudo add-apt-repository ppa:libreoffice/ppa
#sudo apt-get update -y
#sudo apt-get install -y libreoffice
"""


INSTALL_PKGS['openvpn'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y openvpn easy-rsa
"""

INSTALL_PKGS['goxel'] = r"""
#!/usr/bin/env bash

mkdir -p ~/Applications \
&& cd ~/Applications \
&& sudo apt-get install -y scons pkg-config libglfw3-dev libgtk-3-dev git \
&& git clone https://github.com/guillaumechereau/goxel \
&& cd goxel \
&& make release \
&& sudo ln -s ~/Applications/goxel/goxel /usr/local/bin/goxel
"""

# TODO Really slow install...
INSTALL_PKGS['freecad'] = r"""
#!/usr/bin/env bash

# sudo apt-get install -y software-properties-common
# sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
# sudo apt-get update -y
# sudo apt-get install -y freecad freecad-common freecad-python2 freecad-python3

# Default to using py3! (TODO Does this work?)
# sudo update-alternatives --config freecad
"""

INSTALL_PKGS['arandr'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y arandr
"""

INSTALL_PKGS['texstudio'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y texstudio texlive-latex-extra
"""

INSTALL_PKGS['shutter'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:linuxuprising/shutter \
&& sudo apt-get update -y \
&& sudo apt-get install -y shutter
"""

INSTALL_PKGS['git'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y git
"""
INSTALL_PKGS['tree'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y tree
"""
INSTALL_PKGS['wget'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y wget
"""
INSTALL_PKGS['firewall_gui'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y gufw
"""
# --fix-broken

INSTALL_PKGS['gnome_tweak_tool'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y gnome-tweak-tool gnome-tweaks
"""
INSTALL_PKGS['xcwd'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y wget unzip \
&& wget https://github.com/schischi/xcwd/archive/master.zip -O xcwd.zip  \
&& unzip -j xcwd.zip -d xcwd-unzipped \
&& cd xcwd-unzipped/ \
&& make \
&& sudo make install
# Use checkinstall instead of make install?
"""

INSTALL_PKGS['chrome'] = r"""
#!/usr/bin/env bash

TMP_DEB=/tmp/google-chrome.deb

sudo apt-get install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb --continue --output-document=${TMP_DEB}
sudo apt install ${TMP_DEB}
"""

INSTALL_PKGS['tlp'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y tlp
"""

INSTALL_PKGS['tlp_gui'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:linuxuprising/apps \
&& apt-get update -y \
&& sudo apt install -y tlpui
"""
INSTALL_PKGS['slack'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y slack
"""
INSTALL_PKGS['docker'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y curl \
&& sudo curl -sSL https://get.docker.com/ \
| sh && sudo usermod -aG docker ${USER}

# sudo apt install docker.io
# sudo systemctl enable --now docker
# sudo usermod -aG docker ${USER}
"""

INSTALL_PKGS['docker_compose'] = r"""
#!/usr/bin/env bash
# https://github.com/docker/compose/releases
VER=1.26.2
sudo apt-get install -y curl \
&& sudo curl -L https://github.com/docker/compose/releases/download/${VER}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
&& sudo chmod +x /usr/local/bin/docker-compose
"""

INSTALL_PKGS['stretchly'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y wget \
&& mkdir -p ~/Applications \
&& wget -O ~/Applications/stretchlyx86_64.AppImage https://github.com/hovancik/stretchly/releases/download/v0.21.1/stretchly-0.21.1-x86_64.AppImage \
&& chmod u+x ~/Applications/stretchlyx86_64.AppImage \
&& sudo ln -s ~/Applications/stretchlyx86_64.AppImage /usr/local/bin/stretchly

# wget -c https://github.com/hovancik/stretchly/releases/download/v0.21.0/stretchly_0.21.0_amd64.deb -O /tmp/stretchly.deb \
# && sudo dpkg -i /tmp/stretchly.deb

"""

INSTALL_PKGS['xournal'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:andreasbutti/xournalpp-master \
&& sudo apt-get update -y \
&& sudo apt-get install -y xournalpp
"""

INSTALL_PKGS['i3'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y i3 arandr lxappearance dmenu rofi compton i3blocks xbacklight htop feh i3lock-fancy
# install  i3-snapshot?
"""

# TODO the second i3gaps line probably belongs somewhere else...
INSTALL_PKGS['i3_gaps'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:kgilmer/speed-ricer \
&& sudo apt-get update -y \
&& sudo apt-get install -y i3-gaps i3-gaps-wm i3-snapshot arandr \
                        lxappearance rofi compton i3blocks xbacklight \
                        htop feh \
&& sudo apt-get install -y fonts-source-code-pro-ttf nordic moka-icon-theme
"""


INSTALL_PKGS['vim'] = r"""
#!/usr/bin/env bash
sudo apt-get remove -y vim-tiny gvim \
&& sudo apt-get install -y vim vim-gtk \
&& vim +PluginInstall +qall
# Update!
"""

INSTALL_PKGS['neovim'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y wget git xclip exuberant-ctags ncurses-term curl python3-pip python3-autopep8 nodejs

VER=0.4.4
mkdir -p /opt/
sudo wget https://github.com/neovim/neovim/releases/download/v${VER}/nvim.appimage --continue --output-document=/opt/nvim.appimage
sudo chown ${USER}:${USER} /opt/nvim.appimage
sudo chmod u+x /opt/nvim.appimage
sudo update-alternatives --install /usr/bin/neovim  editor /opt/nvim.appimage 100


# py3
sudo -H /usr/bin/pip3  install --upgrade pip
sudo -H /usr/bin/pip3  install --upgrade neovim pynvim flake8 jedi autopep8


# Basic config
mkdir -p ~/.config/nvim
touch ~/.config/nvim/init.vim
mkdir -p ~/.config/nvim/pack/minpac/opt/minpac
git clone https://github.com/k-takata/minpac.git ~/.config/nvim/pack/minpac/opt/minpac

# Config deps
# Required by CoC
sudo snap install node --classic --channel=8
sudo npm install -g neovim


neovim +PackUpdate +qall

# sudo apt-get install llvm and sudo apt-get install clang

# something like that...
# https://clangd.llvm.org/installation.html

# sudo apt-get installZQZQ clangd-9
# sudo update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-9 100


sudo update-alternatives --install /usr/bin/neovim  editor ~/Applications/nvim.appimage 100
sudo update-alternatives --config editor

&& sudo ln -s /opt/nvim.appimage /usr/local/bin/nvim \
&& sudo apt install -y python-pip python3-pip python-autopep8 \
&& pip2 install --upgrade pip \
&& pip3 install --upgrade pip \
&& pip install flake8 jedi autopep8 \
&& pip2 install --user --upgrade neovim pynvim \
&& pip3 install --user --upgrade neovim pynvim \
&& sudo apt-get install -y git exuberant-ctags ncurses-term curl \
&& mkdir -p ~/.config/nvim \
&& curl 'https://vim-bootstrap.com/generate.vim' --data 'langs=javascript&langs=c&langs=html&langs=python&langs=typescript&editor=nvim' > ~/.config/nvim/init.vim
 


# Update!

# neovim +PluginInstall +qall
# neovim +VimBootstrapUpdate +qall
"""

INSTALL_PKGS['mupdf'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y mupdf
"""

INSTALL_PKGS['cmus'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y cmus
"""

INSTALL_PKGS['pavucontrol'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y pavucontrol
"""

INSTALL_PKGS['vlc'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y vlc
"""


INSTALL_PKGS['pycharm'] = r"""
#!/usr/bin/env bash
echo 'TODO'
"""

INSTALL_PKGS['calibre'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y wget \
&& sudo -v \
&& wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh \
| sudo sh /dev/stdin
"""

INSTALL_PKGS['clipster'] = r"""
#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Clipster
# Config at ~/.config/clipster/clipster.ini

mkdir -p ~/Applications \
&& cd ~/Applications \
&& sudo apt-get install -y python-gi gir1.2-gtk-3.0 git \
&& git clone https://github.com/mrichar1/clipster.git clipster-repo \
&& cp clipster-repo/clipster clipster \
&& rm -rf clipster-repo \
&& sudo ln -s $(realpath clipster) /usr/bin/clipster


# Roficlip
# git clone https://github.com/gilbertw1/roficlip.git roficlip-repo
# cp roficlip-repo/roficlip roficlip
# rm -rf roficlip-repo
# sudo ln -s $(realpath roficlip) /usr/bin/roficlip
"""


INSTALL_PKGS['entr'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y entr
"""

INSTALL_PKGS['xclip'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y xclip
"""

#INSTALL_PKGS['gtk_themes'] = r"""
##!/usr/bin/env bash

#SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

## if [[ ${SCOPE} = "SYSTEM" ]]; 
## then    
## 	echo "Installing system-wide wallpapers";
##         IMG_DIR=/usr/local/share/wallpapers/;
## 	# System-wide install requires sudo
## 	CP_CMD='sudo cp';
## else   
## 	echo "Installing wallpapers for user $USER";
## 	IMG_DIR=~/Images/;
## 	CP_CMD='cp';
## fi;
## In general for setting themes:
#sudo apt-get install -y lxappearance gtk-chtheme qt4-qtconfig
## Use sudo lxappearance and gtk-chteme for GTK2.0 and GTK+ 
## Use qtconfig and qtconfig-q4 to set the qt themes
## Note, for the qtconfig themes, delete this first (otherwise the changes don't stick!)
## rm -y ~/.config/Trolltech.conf

## From: https://www.ubuntupit.com/materia-theme-a-material-design-theme-for-gnome-gtk/
## Install Material theme requirements
#sudo apt install -y gnome-themes-standard gtk2-engines-murrine libglib2.0-dev libxml2-utils;
#sudo apt install -y materia-gtk-theme
## Remove with: 
## sudo rm -rf /usr/share/themes/Materia{,-compact,-dark,-dark-compact,-light,-light-compact}

#sudo mkdir -p ${IMG_DIR};

#echo ${WALLPAPER_URL};

## if [[ -z "${WALLPAPER_URL}" ]]; 
## then    
## 	echo "NO WLLPAPER";
##         # FONT_DIR=/usr/share/fonts/opentype
## 	# System-wide install requires sudo
## 	# FONT_CMD='sudo cp'
## else   
## 	echo "set url_ ${WALLPAPER_URL}";

## 	# FONT_DIR=~/.fonts/
## 	# FONT_CMD='cp'
## fi;

## export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/
## Otherwise the set wallpaper command (gsettings) fails, see:
## https://stackoverflow.com/questions/44934641/glib-gio-message-using-the-memory-gsettings-backend-your-settings-will-not-b
## https://github.com/conda-forge/glib-feedstock/issues/19
#"""



if __name__ == '__main__':
    pass
