#!/usr/bin/env python3

# import os
# import sys
import pathlib
# import pdb
# import shutil
import tempfile
# from enum import Enum, auto

# Paths
PY_PKG = pathlib.Path(__file__).resolve()
REPO_DIR = PY_PKG.parent
DOTFILE_DIR = REPO_DIR / 'dotfiles'
TMP = tempfile.gettempdir()


# class InstallKeys(Enum):
#     shutter = 'shutter'
#     polybar = 'polybar'
#     exfat = 'exfat'
#     libreoffice = 'libreoffice'
#     ssh = 'ssh'
#     texstudio = 'texstudio'
#     trash_cli = 'trash_cli'
#     git = 'git'
#     tree = 'tree'
#     wget = 'wget'
#     firewall_gui = 'firewall_gui'
#     gnome_tweak_tool = 'gnome_tweak_tool'
#     xcwd = 'xcwd'
#     chrome = 'chrome'
#     tlp = 'tlp'
#     tlp_gui = 'tlp_gui'
#     slack = 'slack'
#     docker = 'docker'
#     docker_compose = 'docker_compose'
#     stretchly = 'stretchly'
#     xournal = 'xournal'
#     calibre = 'calibre'
#     i3 = 'i3'
#     i3_gaps = 'i3_gaps'
#     openvpn = 'openvpn'
#     goxel = 'goxel'
#     freecad = 'freecad'
#     arandr = 'arandr'
#     vim = 'vim'
#     neovim = 'neovim'
#     mupdf = 'mupdf'
#     cmus = 'cmus'
#     pavucontrol = 'pavucontrol'
#     vlc = 'vlc'
#     pycharm = 'pycharm'
#     clipster = 'clipster'
#     gtk_themes = 'gtk_themes'
#     entr = 'entr'
#     xclip = 'xclip'

#     # Fonts
#     fontawesome = 'fontawesome'
#     wuncon_siji = 'wuncon_siji'
#     xos4_terminus = 'xos4_terminus'
#     misc_termsyn = 'misc_termsyn'
#     icomoon_feather = 'icomoon_feather'
#     unifont = 'unifont'  # really?


#     # Themes
#     # fontawesome = 'fontawesome'
    
#     # Icon themes
#     moka = 'moka'
