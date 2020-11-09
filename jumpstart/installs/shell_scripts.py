#!/usr/bin/env python3

# std imports
from typing import Union, Sequence
import pdb

# local imports
INSTALL_PKGS = dict()
UPDATE_PGKS = dict()
REMOVE_PKGS = dict()

# https://stackoverflow.com/questions/10649814/get-last-git-tag-from-a-remote-repo-without-cloning

# Get last tag using newer versions of git that support --sort:
# git -c 'versionsort.suffix=-' \
#     ls-remote --exit-code --refs --sort='version:refname' --tags <repository> '*.*.*' \
#     | tail --lines=1 \
#     | cut --delimiter='/' --fields=3

# For older versions of git that support --version-sort
# git ls-remote --refs --tags <repository> \
#     | cut --delimiter='/' --fields=3     \
#     | tr '-' '~'                         \
#     | sort --version-sort                \
#     | tail --lines=1

# https://github.com/nodesource/distributions/blob/master/README.md
INSTALL_PKGS['nodejs'] = r"""
#!/usr/bin/env bash
# Using Ubuntu
sudo apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# update it
sudo npm install -g npm

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

# TODO Add checkinstall
INSTALL_PKGS['goxel'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y scons pkg-config libglfw3-dev libgtk-3-dev git \
&& cd /opt/ \
&& git clone https://github.com/guillaumechereau/goxel goxel \
&& cd goxel \
&& make release \
&& sudo ln -s /opt/goxel/goxel /usr/local/bin/goxel
"""

## TODO Really slow install...
# INSTALL_PKGS['freecad'] = r"""
##!/usr/bin/env bash
# VER=0.18.4
# sudo apt-get install -y git software-properties-common apt-utils \
# && sudo mkdir -p /opt/ \
# && cd /opt/ \
# && sudo git clone https://github.com/FreeCAD/FreeCAD.git FreeCAD \
# && sudo chown -R ${USER}:${USER} /opt/FreeCAD \
# && cd FreeCAD/ \
# && git checkout ${VER} \
# && sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable \
# && sudo apt-get update -y \
# && sudo apt-get install -y cmake cmake-qt-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-signals-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev libqt5webkit5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2uic qtbase5-dev qttools5-dev swig \
# && make \
# && sudo checkinstall
# """
## PROBLEMS WITH:
##   python3-pyside2uic
## sudo apt-get install -y cmake cmake-qt-gui libboost-date-time-dev        libboost-dev         libboost-filesystem-dev         libboost-graph-dev         libboost-iostreams-dev         libboost-program-options-dev         libboost-python-dev         libboost-regex-dev         libboost-serialization-dev         libboost-dev         libboost-thread-dev         libeigen3-dev         libgts-bin         libgts-dev         libkdtree++-dev         libmedc-dev         libopencv-dev         libproj-dev         libqt5opengl5-dev         libqt5svg5-dev         libqt5webkit5-dev         libqt5x11extras5-dev         libqt5xmlpatterns5-dev         libspnav-dev         libvtk7-dev         libx11-dev         libxerces-c-dev         libzipios++-dev         python3-dev         python3-matplotlib         python3-ply         qtbase5-dev         qttools5-dev         swig
## ADD PPA
## sudo apt-get install -y         libocct-data-exchange-dev         libocct-ocaf-dev         libocct-visualization-dev         occt-draw         libcoin-dev         python3-pyside2.qtgui         python3-pyside2.qtsvg         python3-pyside2.qtwidgets                pyside2-tools         libshiboken2-dev         python3-pivy         libpyside2-dev         python3-pyside2.qtcore
## sudo apt-get install -y libsimage-dev

INSTALL_PKGS['freecad'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
sudo apt-get update -y
sudo apt-get install -y freecad freecad-common freecad-python3

# Default to using py3! (TODO Does this work?)
# sudo update-alternatives --config freecad
"""

INSTALL_PKGS['xcwd'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y git \
&& sudo mkdir -p /opt/ \
&& cd /opt/ \
&& sudo git clone https://github.com/schischi/xcwd.git xcwd \
&& sudo chown -R ${USER}:${USER} /opt/xcwd \
&& cd xcwd/ \
&& make \
&& sudo checkinstall
# && sudo make install
"""

INSTALL_PKGS['chrome'] = r"""
#!/usr/bin/env bash

TMP_DEB=/tmp/google-chrome.deb

sudo apt-get install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb --continue --output-document=${TMP_DEB}
sudo apt install ${TMP_DEB}
"""

INSTALL_PKGS["duf"] = r"""
#!/usr/bin/env bash

sudo apt-get install -y wget git

VER=$(git ls-remote --refs --tags https://github.com/muesli/duf \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);
# e.g. VER=v0.3.1

TMP_DEB=/tmp/duf.deb
wget https://github.com/muesli/duf/releases/download/${VER}/duf_${VER:1}_linux_amd64.deb --continue --output-document=${TMP_DEB}
sudo apt install ${TMP_DEB}
"""

INSTALL_PKGS['tmpmail'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y curl w3m jq
sudo wget https://raw.githubusercontent.com/sdushantha/tmpmail/master/tmpmail --continue --output-document=/usr/local/bin/tmpmail
sudo chown -R ${USER}:${USER} /usr/local/bin/tmpmail
sudo chmod +x /usr/local/bin/tmpmail
# Prepare first email
/usr/local/bin/tmpmail --generate
"""
REMOVE_PKGS['tmpmail'] = r"""
#!/usr/bin/env bash
sudo rm -f /usr/local/bin/tmpmail
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

INSTALL_PKGS['beekeeper-studio'] = r"""
#!/usr/bin/env bash

# https://docs.beekeeperstudio.io/installation/#apt-deb

# Install our GPG key
wget --quiet -O - https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -

# add our repo to your apt lists directory
echo "deb https://dl.bintray.com/beekeeper-studio/releases disco main" | sudo tee /etc/apt/sources.list.d/beekeeper-studio.list

# Update apt and install
sudo apt update
sudo apt install beekeeper-studio

# Installed to '/opt/' by default!
BEEKEEPER_DIR="/opt/Beekeeper Studio"
sudo chown -R ${USER}:${USER} "${BEEKEEPER_DIR}"
sudo rm -f /usr/local/bin/beekeeper-studio
ln -s ${BEEKEEPER_DIR}/beekeeper-studio /usr/local/bin/beekeeper-studio
sudo ln -s "${BEEKEEPER_DIR}/beekeeper-studio" /usr/local/bin/beekeeper-studio
"""

# r"""
# #!/usr/bin/env bash
#
# # https://docs.beekeeperstudio.io/installation/#apt-deb
#
# sudo rm -f /usr/local/bin/beekeeper-studio
# sudo wget https://www.beekeeperstudio.io/download/?platform=appimage --continue --output-document=/usr/local/bin/beekeeper-studio
# sudo chmod +x /usr/local/bin/beekeeper-studio
# """

# TODO add
# bpytop
# INSTALL_PKGS['bpytop'] = r"""
# pip3 install bpytop --upgrade
# """
# UPDATE_PGKS['bpytop'] = INSTALL_PKGS['bpytop']

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

VER=$(git ls-remote --refs --tags https://github.com/hovancik/stretchly \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);
# e.g. VER=v1.2.0
sudo rm -f /usr/local/bin/stretchly \
&& sudo wget https://github.com/hovancik/stretchly/releases/download/${VER}/Stretchly-${VER:1}.AppImage \
    --output-document=/usr/local/bin/stretchly \
&& sudo chmod +x /usr/local/bin/stretchly;
"""
UPDATE_PGKS['stretchly'] = INSTALL_PKGS['stretchly']

# https://github.com/jrfonseca/gprof2dot
INSTALL_PKGS['gprof2dot'] = r"""
#!/usr/bin/env bash
sudo rm -f /usr/local/bin/gprof2dot.py
sudo wget https://raw.githubusercontent.com/jrfonseca/gprof2dot/master/gprof2dot.py --continue --output-document=/usr/local/bin/gprof2dot.py
sudo chmod +x /usr/local/bin/gprof2dot.py
# Usage:
# python -m cProfile -o foo.stats foo.py
$ gprof2dot foo.stats -f pstats > foo.dot
"""
UPDATE_PGKS['gprof2dot'] = INSTALL_PKGS['gprof2dot']

INSTALL_PKGS['xournal'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:andreasbutti/xournalpp-master \
&& sudo apt-get update -y \
&& sudo apt-get install -y xournalpp
"""

# In the apt-get section?
# INSTALL_PKGS['i3'] = r"""
# #!/usr/bin/env bash
# sudo apt-get install -y i3 arandr lxappearance dmenu rofi compton i3blocks xbacklight htop feh i3lock-fancy
# # install  i3-snapshot?
# """

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

INSTALL_PKGS['dunst'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y dunst
# Enable and configure it in systemd
systemctl restart --user dunst.service
"""

REMOVE_PKGS['dunst'] = r"""
#!/usr/bin/env bash
sudo apt-get remove -y dunst
# Enable and configure it in systemd
systemctl disable --user dunst.service
"""

INSTALL_PKGS['alacritty'] = r"""
#!/usr/bin/env bash
# TODO FROM https://github.com/alacritty/alacritty/blob/master/INSTALL.md

# Default? 
# sudo gsettings set org.gnome.desktop.default-applications.terminal exec /usr/bin/alacritty
# sudo gsettings set org.gnome.desktop.default-applications.terminal exec-arg "-x"
sudo update-alternatives --install /usr/local/bin/alacritty  x-terminal-emulator `realpath alacritty` 100
# https://blog.arranfrance.com/post/alacritty-and-byobu/
# apt-get install -y byobu
"""

INSTALL_PKGS['neovim'] = r"""
#!/usr/bin/env bash

sudo apt-get install -y wget curl git xclip exuberant-ctags ncurses-term python3-pip python3-autopep8

# DEPENDS ON NODEJS (install it as well)

VER=$(git ls-remote --refs --tags https://github.com/neovim/neovim \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);
# e.g. VER=v0.4.4

sudo rm -f /usr/local/bin/nvim
sudo wget https://github.com/neovim/neovim/releases/download/${VER}/nvim.appimage --output-document=/usr/local/bin/nvim
# sudo chown ${USER}:${USER} /usr/local/bin/nvim
sudo chmod +x /usr/local/bin/nvim
# sudo update-alternatives --install /usr/bin/neovim  editor /opt/nvim.appimage 100
# nvr expects "nvim" not "neovim"!
sudo update-alternatives --install /usr/bin/nvim  editor /usr/local/bin/nvim 100

# TODO FZF!
# mkdir -p ~/.config/nvim/pack/minpac/start/
# git clone --depth 1 https://github.com/junegunn/fzf.git ~/.config/nvim/pack/minpac/start/fzf
# ~/.config/nvim/pack/minpac/start/fzf/install

# py3
sudo -H pip3  install --upgrade pip
sudo -H pip3  install --upgrade neovim pynvim flake8 jedi autopep8 neovim-remote


# Basic config
mkdir -p ~/.config/nvim
touch ~/.config/nvim/init.vim
mkdir -p ~/.config/nvim/pack/minpac/opt/minpac
git clone https://github.com/k-takata/minpac.git ~/.config/nvim/pack/minpac/opt/minpac

# Config deps


# Update npm
sudo npm install -g npm

# nodejs Required by CoC

sudo npm install -g neovim
sudo npm install -g eslint

# sudo apt-get install llvm and sudo apt-get install clang

# something like that...
# https://clangd.llvm.org/installation.html

# sudo apt-get installZQZQ clangd-9
# sudo update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-9 100

# Update!
neovim +PackUpdate +qall
neovim +CocInstall +qall
"""

UPDATE_PGKS['neovim'] = r"""

VER=$(git ls-remote --refs --tags https://github.com/neovim/neovim \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);
# e.g. VER=v0.4.4

sudo rm -f /usr/local/bin/nvim
sudo wget https://github.com/neovim/neovim/releases/download/${VER}/nvim.appimage --output-document=/usr/local/bin/nvim
# sudo chown ${USER}:${USER} /usr/local/bin/nvim
sudo chmod +x /usr/local/bin/nvim

# python
sudo -H pip3  install --upgrade pip
sudo -H pip3  install --upgrade neovim pynvim flake8 jedi autopep8 neovim-remote

# Update npm
sudo npm install -g npm

" command to update everything: (The "Pack..." commands are my custom mappings for minpac's cmds... replace?)
/usr/local/bin/nvim +PackUpdate +qall
/usr/local/bin/nvim +PackClean +qall
/usr/local/bin/nvim +PackDocks +qall
/usr/local/bin/nvim +CocInstall +qall

"""

INSTALL_PKGS['calibre'] = r"""
#!/usr/bin/env bash
sudo apt-get install -y wget \
&& sudo -v \
&& wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh \
| sudo sh /dev/stdin
"""

# TODO
INSTALL_PKGS['clipster'] = r"""
#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Clipster
# Config at ~/.config/clipster/clipster.ini

# TODO MOVE TO OPT
mkdir -p ~/Applications \
&& cd ~/Applications \
&& sudo apt-get install -y python-gi gir1.2-gtk-3.0 git \
&& git clone https://github.com/mrichar1/clipster.git clipster-repo \
&& cp clipster-repo/clipster clipster \
&& rm -rf clipster-repo \
&& sudo ln -s $(realpath clipster) /usr/local/bin/clipster


# Roficlip
# git clone https://github.com/gilbertw1/roficlip.git roficlip-repo
# cp roficlip-repo/roficlip roficlip
# rm -rf roficlip-repo
# sudo ln -s $(realpath roficlip) /usr/bin/roficlip
"""

DEPENDENCY_MAP = dict()
DEPENDENCY_MAP['neovim'] = ['python3', 'nodejs', 'networking', 'xclip', 'git']
DEPENDENCY_MAP['calibre'] = ['networking']
DEPENDENCY_MAP['docker'] = ['networking']
DEPENDENCY_MAP['tmpmail'] = ['networking']
DEPENDENCY_MAP['docker_compose'] = ['networking']
DEPENDENCY_MAP['nodejs'] = ['networking']
DEPENDENCY_MAP['stretchly'] = ['networking']
DEPENDENCY_MAP['clipster'] = ['git']
DEPENDENCY_MAP['polybar'] = ['git']
DEPENDENCY_MAP['goxel'] = ['git', 'checkinstall']
DEPENDENCY_MAP['xcwd'] = ['git', 'checkinstall']
DEPENDENCY_MAP['freecad'] = ['git', 'checkinstall']

if __name__ == '__main__':
    sep = 80 * '-'
    # print('\n'.join(
    #     ['PKGs WITH THEIR INSTALL COMMANDS']
    #     + [f'{sep}\n\tINSTALLING [{k}]\n{sep}\n{INSTALL_PKGS[k]}\n' for k in sorted(INSTALL_PKGS)])
    # )
    #
    # print('\n'.join(
    #     ['PKGs WITH THEIR REMOVE COMMANDS']
    #     + [f'{sep}\n\tREMOVING [{k}]\n{sep}\n{REMOVE_PKGS[k]}\n' for k in sorted(REMOVE_PKGS)])
    # )
