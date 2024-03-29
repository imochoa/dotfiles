#!/usr/bin/env python3

# std imports
from typing import Union, Sequence
import pdb

# local imports

# TODO ADD Visual studio code: sudo snap install --classic code
# TODO ADD pycharm etc.

BASH_SHEBANG = "#!/usr/bin/env bash"


def aptget_install(
    pkgs: Union[str, Sequence[str]], ppas: Union[None, str, Sequence[str]] = None
) -> str:
    """"""
    cmd_str = f"{BASH_SHEBANG}\n"

    if ppas is not None:
        if isinstance(ppas, str):
            ppas = [ppas]
        for ppa in ppas:
            cmd_str += f"sudo add-apt-repository {ppa} && "
        cmd_str += "sudo apt-get update -y"

    if isinstance(pkgs, str):
        pkgs = [pkgs]
    return f"{cmd_str}\nsudo apt-get install -y {' '.join(pkgs)}"


def aptget_remove(
    pkgs: Union[str, Sequence[str]], ppas: Union[None, str, Sequence[str]] = None
) -> str:
    """"""
    cmd_str = f"{BASH_SHEBANG}\n"

    if ppas is not None:
        if isinstance(ppas, str):
            ppas = [ppas]
        for ppa in ppas:
            cmd_str += f"sudo add-apt-repository --remove {ppa} && "
        cmd_str += "sudo apt-get update -y"

    if isinstance(pkgs, str):
        pkgs = [pkgs]
    return f"{cmd_str}\nsudo apt remove -y {' '.join(pkgs)}"


# TODO Add dependencies?
DEPENDENCY_MAP = dict()
INSTALL_PKGS = dict()
REMOVE_PKGS = dict()

INSTALL_PKGS["7zip"] = aptget_install("p7zip-full")
REMOVE_PKGS["7zip"] = aptget_remove("p7zip-full")

INSTALL_PKGS["bashtop"] = aptget_install("bashtop", ppas="ppa:bashtop-monitor/bashtop")
REMOVE_PKGS["bashtop"] = aptget_remove("bashtop", ppas="ppa:bashtop-monitor/bashtop")

INSTALL_PKGS["tmux"] = aptget_install("tmux")
REMOVE_PKGS["tmux"] = aptget_remove("tmux")

INSTALL_PKGS["fd"] = aptget_install("fd-find")
REMOVE_PKGS["fd"] = aptget_remove("fd-find")

INSTALL_PKGS["sxiv"] = aptget_install("sxiv")
REMOVE_PKGS["sxiv"] = aptget_remove("sxiv")

INSTALL_PKGS["neofetch"] = aptget_install("neofetch")
REMOVE_PKGS["neofetch"] = aptget_remove("neofetch")

INSTALL_PKGS["networking"] = aptget_install(
    [
        "wget",
        "curl",
        "iputils-ping",
    ]
)
REMOVE_PKGS["networking"] = aptget_remove(
    [
        "wget",
        "curl",
        "iputils-ping",
    ]
)

INSTALL_PKGS["entr"] = aptget_install("entr")
REMOVE_PKGS["entr"] = aptget_remove("entr")

INSTALL_PKGS["xclip"] = aptget_install("xclip")
REMOVE_PKGS["xclip"] = aptget_remove("xclip")

INSTALL_PKGS["disk_space"] = aptget_install("baobab")
REMOVE_PKGS["disk_space"] = aptget_remove("baobab")

INSTALL_PKGS["trash_cli"] = aptget_install("trash-cli")
REMOVE_PKGS["trash_cli"] = aptget_remove("trash-cli")

INSTALL_PKGS["exfat"] = aptget_install(["exfat-fuse", "exfat-utils"])
REMOVE_PKGS["exfat"] = aptget_remove(["exfat-fuse", "exfat-utils"])

INSTALL_PKGS["arandr"] = aptget_install("arandr")
REMOVE_PKGS["arandr"] = aptget_remove("arandr")

INSTALL_PKGS["texstudio"] = aptget_install(
    [
        "texstudio",
        "texlive-latex-extra",
    ]
)
REMOVE_PKGS["texstudio"] = aptget_remove(
    [
        "texstudio",
        "texlive-latex-extra",
    ]
)

INSTALL_PKGS["git"] = aptget_install("git")
REMOVE_PKGS["git"] = aptget_remove("git")

INSTALL_PKGS["tree"] = aptget_install("tree")
REMOVE_PKGS["tree"] = aptget_remove("tree")

INSTALL_PKGS["firewall_gui"] = aptget_install("gufw")
REMOVE_PKGS["firewall_gui"] = aptget_remove("gufw")
# --fix-broken

INSTALL_PKGS["gnome_tweak_tool"] = aptget_install(["gnome-tweak-tool", "gnome-tweaks"])
REMOVE_PKGS["gnome_tweak_tool"] = aptget_remove(["gnome-tweak-tool", "gnome-tweaks"])

# https://help.ubuntu.com/community/CheckInstall
INSTALL_PKGS["checkinstall"] = aptget_install("checkinstall")
REMOVE_PKGS["checkinstall"] = aptget_remove("checkinstall")

INSTALL_PKGS["mupdf"] = aptget_install("mupdf")
REMOVE_PKGS["mupdf"] = aptget_remove("mupdf")

INSTALL_PKGS["cmus"] = aptget_install("cmus")
REMOVE_PKGS["cmus"] = aptget_remove("cmus")

INSTALL_PKGS["pavucontrol"] = aptget_install("pavucontrol")
REMOVE_PKGS["pavucontrol"] = aptget_remove("pavucontrol")

INSTALL_PKGS["vlc"] = aptget_install("vlc")
REMOVE_PKGS["vlc"] = aptget_remove("vlc")

# TODO Required to add app reps?
INSTALL_PKGS["software-properties-common"] = aptget_install(
    "software-properties-common"
)
REMOVE_PKGS["software-properties-common"] = aptget_remove("software-properties-common")

INSTALL_PKGS["shutter"] = aptget_install("shutter", ppas="ppa:linuxuprising/shutter")
REMOVE_PKGS["shutter"] = aptget_remove("shutter", ppas="ppa:linuxuprising/shutter")

INSTALL_PKGS["openvpn"] = aptget_install(["openvpn", "easy-rsa"])
REMOVE_PKGS["openvpn"] = aptget_remove(["openvpn", "easy-rsa"])

INSTALL_PKGS["tlp"] = aptget_install("tlp")
REMOVE_PKGS["tlp"] = aptget_remove("tlp")

INSTALL_PKGS["tlp_gui"] = aptget_install("tlpui", ppas="ppa:linuxuprising/apps")
REMOVE_PKGS["tlp_gui"] = aptget_remove("tlpui", ppas="ppa:linuxuprising/apps")

INSTALL_PKGS["ssh"] = aptget_install(["openssh-server", "xclip", "xauth"])
REMOVE_PKGS["ssh"] = aptget_remove(["openssh-server", "xclip", "xauth"])
# INSTALL_PKGS['ssh'] = r"""
##!/usr/bin/env bash
# sudo apt install -y openssh-server xclip xauth
## xsel, xauth -> so that you can share the clipboard (prefer xclip over xsel)
## using ssh -Y yourserver
## or by setting that as the default config in ~/.ssh/config
## https://superuser.com/questions/326871/using-clipboard-through-ssh-in-vim
## ~/.ssh/config
## Host myserver
##    ForwardX11 yes
##    ForwardX11Trusted yes
# """
# TODO ## xsel, xauth -> so that you can share the clipboard (prefer xclip over xsel)
# using ssh -Y yourserver
# or by setting that as the default config in ~/.ssh/config
# https://superuser.com/questions/326871/using-clipboard-through-ssh-in-vim
# ~/.ssh/config
# Host myserver
# ForwardX11 yes
# ForwardX11Trusted yes


INSTALL_PKGS[
    "nodejs"
] = r"""
#!/usr/bin/env bash
# https://github.com/nodesource/distributions/blob/master/README.md
# Using Ubuntu
sudo apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# update it
sudo npm install -g npm

# [OPTIONAL] To compile and install native addons from npm you may also need to install build tools:
sudo apt-get install -y build-essential
"""

INSTALL_PKGS[
    "python3"
] = r"""
#!/usr/bin/env bash
sudo apt-get install -y python3 python3-pip python3-venv python3-dev  build-essential libssl-dev libffi-dev  libxml2-dev libxslt1-dev zlib1g-dev
# For python+PDF
sudo apt-get install -y texlive texlive-xetex texlive-latex-extra pandoc pandoc-citeproc
# For python+postgreSQL
sudo apt install -y libpq-dev python3-dev

# Upgrade pip
sudo -H pip3  install --upgrade pip
"""

INSTALL_PKGS[
    "polybar"
] = r"""
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

# TODO libreoffice broken!
INSTALL_PKGS[
    "libreoffice"
] = r"""
##!/usr/bin/env bash
#sudo apt-get remove -y libreoffice
#sudo apt-get install -y software-properties-common
#sudo add-apt-repository ppa:libreoffice/ppa
#sudo apt-get update -y
#sudo apt-get install -y libreoffice
"""

# TODO Add checkinstall
INSTALL_PKGS[
    "goxel"
] = r"""
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

INSTALL_PKGS[
    "freecad"
] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
sudo apt-get update -y
sudo apt-get install -y freecad freecad-common freecad-python3

# Default to using py3! (TODO Does this work?)
# sudo update-alternatives --config freecad
"""

INSTALL_PKGS[
    "xcwd"
] = r"""
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

INSTALL_PKGS[
    "chrome"
] = r"""
#!/usr/bin/env bash

TMP_DEB=/tmp/google-chrome.deb

sudo apt-get install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb --continue --output-document=${TMP_DEB}
sudo apt install ${TMP_DEB}
"""

INSTALL_PKGS[
    "slack"
] = r"""
#!/usr/bin/env bash
# # Apt-get (was problematic)
# sudo apt-get install -y slack
# With snaps that would be:
sudo snap install slack --classic
"""

INSTALL_PKGS[
    "docker"
] = r"""
#!/usr/bin/env bash
sudo apt-get install -y curl \
&& sudo curl -sSL https://get.docker.com/ \
| sh && sudo usermod -aG docker ${USER}

# sudo apt install docker.io
# sudo systemctl enable --now docker
# sudo usermod -aG docker ${USER}
"""

INSTALL_PKGS[
    "docker_compose"
] = r"""
#!/usr/bin/env bash
# https://github.com/docker/compose/releases
VER=1.26.2
sudo apt-get install -y curl \
&& sudo curl -L https://github.com/docker/compose/releases/download/${VER}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
&& sudo chmod +x /usr/local/bin/docker-compose
"""

INSTALL_PKGS[
    "stretchly"
] = r"""
#!/usr/bin/env bash

sudo apt-get install -y wget
VER=1.0.0
sudo mkdir -p /opt/
sudo wget https://github.com/hovancik/stretchly/releases/download/v${VER}/Stretchly-${VER}.AppImage --continue --output-document=/opt/stretchly.appimage
sudo chown ${USER}:${USER} /opt/stretchly.appimage
sudo chmod u+x /opt/stretchly.appimage
sudo ln -s /opt/stretchly.appimage /usr/local/bin/stretchly
"""

INSTALL_PKGS[
    "xournal"
] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:andreasbutti/xournalpp-master \
&& sudo apt-get update -y \
&& sudo apt-get install -y xournalpp
"""

INSTALL_PKGS[
    "i3"
] = r"""
#!/usr/bin/env bash
sudo apt-get install -y i3 arandr lxappearance dmenu rofi compton i3blocks xbacklight htop feh i3lock-fancy
# install  i3-snapshot?
"""

# TODO the second i3gaps line probably belongs somewhere else...
INSTALL_PKGS[
    "i3_gaps"
] = r"""
#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:kgilmer/speed-ricer \
&& sudo apt-get update -y \
&& sudo apt-get install -y i3-gaps i3-gaps-wm i3-snapshot arandr \
                        lxappearance rofi compton i3blocks xbacklight \
                        htop feh \
&& sudo apt-get install -y fonts-source-code-pro-ttf nordic moka-icon-theme
"""

INSTALL_PKGS[
    "vim"
] = r"""
#!/usr/bin/env bash
sudo apt-get remove -y vim-tiny gvim \
&& sudo apt-get install -y vim vim-gtk \
&& vim +PluginInstall +qall
# Update!
"""

INSTALL_PKGS[
    "neovim"
] = r"""
#!/usr/bin/env bash

sudo apt-get install -y wget curl git xclip exuberant-ctags ncurses-term python3-pip python3-autopep8

# DEPENDS ON NODEJS (install it as well)

VER=0.4.4
mkdir -p /opt/
sudo wget https://github.com/neovim/neovim/releases/download/v${VER}/nvim.appimage --continue --output-document=/opt/nvim.appimage
sudo chown ${USER}:${USER} /opt/nvim.appimage
sudo chmod u+x /opt/nvim.appimage
# sudo update-alternatives --install /usr/bin/neovim  editor /opt/nvim.appimage 100
# nvr expects "nvim" not "neovim"!
sudo update-alternatives --install /usr/bin/nvim  editor /opt/nvim.appimage 100


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

# Required by CoC
# sudo snap install node --classic --channel=8 -> Use nodejs installer instead!

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

INSTALL_PKGS[
    "pycharm-community"
] = r"""
#!/usr/bin/env bash
sudo snap install pycharm-community --classic
"""

INSTALL_PKGS[
    "pycharm-professional"
] = r"""
#!/usr/bin/env bash
sudo snap install pycharm-professional --classic
"""
# sudo snap install pycharm-educational --classic

INSTALL_PKGS[
    "calibre"
] = r"""
#!/usr/bin/env bash
sudo apt-get install -y wget \
&& sudo -v \
&& wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh \
| sudo sh /dev/stdin
"""

# TODO
INSTALL_PKGS[
    "clipster"
] = r"""
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
&& sudo ln -s $(realpath clipster) /usr/bin/clipster


# Roficlip
# git clone https://github.com/gilbertw1/roficlip.git roficlip-repo
# cp roficlip-repo/roficlip roficlip
# rm -rf roficlip-repo
# sudo ln -s $(realpath roficlip) /usr/bin/roficlip
"""

DEPENDENCY_MAP["neovim"] = ["python3", "nodejs", "networking", "xclip"]
DEPENDENCY_MAP["ssh"] = ["xclip"]
DEPENDENCY_MAP["calibre"] = ["networking"]
DEPENDENCY_MAP["docker"] = ["networking"]
DEPENDENCY_MAP["docker_compose"] = ["networking"]
DEPENDENCY_MAP["nodejs"] = ["networking"]
DEPENDENCY_MAP["stretchly"] = ["networking"]
DEPENDENCY_MAP["clipster"] = ["git"]
DEPENDENCY_MAP["polybar"] = ["git"]
DEPENDENCY_MAP["goxel"] = ["git", "checkinstall"]
DEPENDENCY_MAP["xcwd"] = ["git", "checkinstall"]
DEPENDENCY_MAP["freecad"] = ["git", "checkinstall"]

if __name__ == "__main__":
    sep = 80 * "-"
    print(
        "\n".join(
            ["PKGs WITH THEIR INSTALL COMMANDS"]
            + [
                f"{sep}\n\tINSTALLING [{k}]\n{sep}\n{INSTALL_PKGS[k]}\n"
                for k in sorted(INSTALL_PKGS)
            ]
        )
    )

    print(
        "\n".join(
            ["PKGs WITH THEIR REMOVE COMMANDS"]
            + [
                f"{sep}\n\tREMOVING [{k}]\n{sep}\n{REMOVE_PKGS[k]}\n"
                for k in sorted(REMOVE_PKGS)
            ]
        )
    )
