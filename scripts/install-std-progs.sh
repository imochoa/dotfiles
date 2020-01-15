#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


pretty_echo 'Installing programs...';

# Basics
install_envvar INSTALL_TRASH_CLI 'sudo apt-get install -y trash-cli';
install_envvar INSTALL_GIT 'sudo apt-get install -y git';
install_envvar INSTALL_TREE 'sudo apt-get install -y tree';
install_envvar INSTALL_WGET 'sudo apt-get install -y wget';
install_envvar INSTALL_FIREWALL_GUI 'sudo apt-get install -y gufw';
install_envvar INSTALL_GNOME_TWEAK_TOOL 'sudo apt install gnome-tweak-tool';
install_envvar INSTALL_XCWD 'wget https://github.com/schischi/xcwd/archive/master.zip -O xcwd.zip  && unzip -j xcwd.zip -d xcwd-unzipped && cd xcwd-unzipped/ && make && sudo make install';

# Web stuff
install_envvar INSTALL_CHROME 'wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb && sudo dpkg -i /tmp/chrome.deb';

# Battery life
install_envvar INSTALL_TLP 'sudo apt-get install tlp';
install_envvar INSTALL_TLP_GUI 'sudo add-apt-repository ppa:linuxuprising/apps && apt-get update && sudo apt install tlpui';

# Networking
install_envvar INSTALL_SLACK 'sudo apt-get install slack';

# Work Utils
install_envvar INSTALL_DOCKER 'sudo curl -sSL https://get.docker.com/ | sh && sudo usermod -aG docker ${USER}';
install_envvar INSTALL_STRETCHLY 'wget -c https://github.com/hovancik/stretchly/releases/download/v0.21.0/stretchly_0.21.0_amd64.deb -O /tmp/stretchly.deb && sudo dpkg -i /tmp/stretchly.deb';
install_envvar INSTALL_XOURNAL 'sudo add-apt-repository ppa:andreasbutti/xournalpp-master && sudo apt update -y && sudo apt install -y xournalpp';

# Window managers
install_envvar INSTALL_I3 'sudo apt-get install -y i3';

# For text & documents
install_envvar INSTALL_VIM 'sudo apt-get remove -y vim-tiny gvim && sudo apt-get install -y vim vim-gtk';
install_envvar INSTALL_MUPDF 'sudo apt-get install -y mupdf';
install_envvar INSTALL_CALIBRE 'sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin';

# Audio & video
install_envvar INSTALL_CMUS 'sudo apt-get install -y cmus';
install_envvar INSTALL_PAVUCONTROL 'sudo apt-get install -y pavucontrol';
install_envvar INSTALL_VLC 'sudo apt-get install vlc';
# TODO docker CE, pycharm


#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
