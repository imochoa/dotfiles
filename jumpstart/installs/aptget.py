#!/usr/bin/env python3

# std imports
from typing import Union, Sequence, Dict, Tuple, Optional

# local imports
from jumpstart.utils import echo, bcolors
from jumpstart.installs.cmd_builders import aptget_install, aptget_remove

# TODO  libreoffice broken!
# INSTALL_PKGS['libreoffice'] = r"""
# ##!/usr/bin/env bash
# #sudo apt-get remove -y libreoffice
# #sudo apt-get install -y software-properties-common
# #sudo add-apt-repository ppa:libreoffice/ppa
# #sudo apt-get update -y
# #sudo apt-get install -y libreoffice
# """

# https://help.ubuntu.com/community/CheckInstall
# What is 'software-properties-common'? is it required to add ppas?

# For trash-put, the files need a place to go to. Which can be problematic if you're on a separate partition:
# https://askubuntu.com/questions/677396/trash-cannot-trash-regular-file
# Run this command at the root of the other partition
# sudo mkdir .Trash-$UID && sudo chown $USER:$USER .Trash-$UID

TRIVIAL_PGKS = [
    # real packages
    'vlc',
    'pavucontrol',
    'cmus',
    'tree',
    'software-properties-common',
    'firewall_gui',
    'git',
    'mupdf',
    'checkinstall',
    '7zip',
    'bashtop',
    'tmux',
    'sxiv',
    'neofetch',
    'entr',
    'xclip',
    'trash-cli',
    'disk_space',
    'arandr',
    'tlp',
    'shutter',
    'flameshot',
    'lmms',
    'mutt',
    'pinta',
    'peek',
    # virtual packages (mapped in *MULTIPLE_PKGs* or *RENAMED_PKGs*)
    'networking',
    'exfat',
    'texstudio',
    'ssh',
    'tlp-gui',
    'openvpn',
    'gnome_tweak_tool',
    'i3',
    'regolith',
]

# [1st STEP] Expand packages with dependencies
MULTIPLE_PKGs = {
    'networking':       ['wget', 'curl', 'iputils-ping', ],
    'exfat':            ['exfat-fuse', 'exfat-utils', ],
    'texstudio':        ['texstudio', 'texlive-latex-extra', ],
    'ssh':              ['openssh-server', 'xclip', 'xauth'],
    'tlp-gui':          ['tlp'],
    'openvpn':          ['openvpn', 'easy-rsa'],
    'gnome_tweak_tool': ['gnome-tweak-tool', 'gnome-tweaks'],
    'i3':               ['i3', 'arandr', 'lxappearance', 'dmenu', 'rofi', 'compton', 'i3blocks', 'xbacklight', 'htop',
                         'feh', 'i3lock-fancy', 'i3-snapshot', ],
    # https://www.digitalocean.com/community/tutorials/installing-and-using-ranger-a-terminal-file-manager-on-a-ubuntu-vps
    'ranger':           ['ranger', 'caca-utils', 'highlight', 'atool', 'w3m', 'poppler-utils', 'mediainfo', 'xclip'],
    'regolith':         ['regolith', 'i3xrocks-battery', ],
}

# See more i3xrocks packages with:
# apt list | grep i3xrocks-

# [2nd STEP] Add any PPAs
PKG_PPAs = {
    'bashtop': 'ppa:bashtop-monitor/bashtop',
    'tlp-gui': 'ppa:linuxuprising/apps',
    'shutter': 'ppa:linuxuprising/shutter',
    'peek':    'ppa:peek-developers/stable',
}

# [3rd STEP] get the REAL names
RENAMED_PKGs = {
    '7zip':         'p7zip-full',
    'fd':           'fd-find',
    'disk_space':   'baobab',
    'firewall_gui': 'gufw',
    'tlp-gui':      'tlpui',
}


# --fix-broken


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

def build_aptget_pkg_maps(pkg_keys: Optional[Sequence[str]] = None) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Gets the commands for the packages with keys *pkg_keys* and returns the (*install_map*, *remove map*)
    """
    pkg_subset = set(TRIVIAL_PGKS).union(PKG_PPAs).union(RENAMED_PKGs).union(MULTIPLE_PKGs)

    if pkg_keys:
        pkg_subset = pkg_subset.intersection(pkg_keys)
        lost_inputs = set(pkg_keys).difference(pkg_subset)
        if lost_inputs:
            echo(([f'[{len(lost_inputs)}] UNKNOWN APT-GET pkg(s)']
                  + [f'[{idx:> 3}] {p}' for idx, p in enumerate(sorted(lost_inputs), start=1)]),
                 color=bcolors.WARNING, sep='\n\t> ')

    if not pkg_subset:
        echo('No APT-GET pkgs will be installed!', color=bcolors.WARNING, sep='\n\t> ')
        return dict(), dict()

    if pkg_keys:
        echo(([f'[{len(pkg_subset)}] Filtered APT-GET pkgs:']
              + [f'[{idx:> 3}] {p}' for idx, p in enumerate(sorted(pkg_subset), start=1)]),
             color=bcolors.DEBUG, sep='\n\t> ')

    install_map, remove_map = dict(), dict()

    for pkg in pkg_subset:
        # Explode each name into all of the subpackages it contains
        subpkgs_to_install = MULTIPLE_PKGs.get(pkg, [pkg])

        # Get their "real-names" as opposed to our keys
        pkgs = [RENAMED_PKGs.get(p, p) for p in subpkgs_to_install]
        ppas = [PKG_PPAs.get(p, p) for p in subpkgs_to_install]

        install_map[pkg] = aptget_install(pkgs=pkgs, ppas=ppas)
        remove_map[pkg] = aptget_remove(pkgs=pkgs, ppas=ppas)

    return install_map, remove_map


if __name__ == '__main__':
    full_install_map, full_remove_map = build_aptget_pkg_maps()  # All commands:
    # full_install_map, full_remove_map = build_aptget_pkg_maps(['xclip', 'ssh'])  # OK subset
    # full_install_map, full_remove_map = build_aptget_pkg_maps(['poop'])  # All commands:

    sep = 80 * '-'
    print('\n'.join(
        ['PKGs WITH THEIR INSTALL COMMANDS']
        + [f'{sep}\n\tINSTALLING [{k}]\n{sep}\n{full_install_map[k]}\n' for k in sorted(full_install_map)])
    )

    print('\n'.join(
        ['PKGs WITH THEIR REMOVE COMMANDS']
        + [f'{sep}\n\tREMOVING [{k}]\n{sep}\n{full_remove_map[k]}\n' for k in sorted(full_remove_map)])
    )
