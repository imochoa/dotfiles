#!/usr/bin/python3

import os
import enum
import pdb
import shutil

# Paths
THIS_FILE = os.path.abspath(__file__)
REPO_DIR = os.path.dirname(THIS_FILE)
DOTFILE_DIR = os.path.join(REPO_DIR, 'dotfiles')

CONFIG_MAP = {
    'bash/bash_functions':           '~/.bash_functions',
    'bash/inputrc':                  '~/.inputrc',
    'bash/bashrc':                   '~/.bashrc',
    'bash/bash_aliases':             '~/.bash_aliases',
    'bash/bash_profile':             '~/.bash_profile',

    'i3/i3config':                   '~/.config/i3/config',
    'i3/polybar.sh':                 '~/.config/i3/polybar.sh',
    'i3/polybar/colors.ini':         'path2',
    'i3/polybar/config.ini':         'path',
    'i3/polybar/bars.ini':           'path',
    'i3/polybar/modules.ini':        'path',
    'i3/polybar/user_modules.ini':   'path',
    'i3/i3blocks.conf':              'path',
    'rofi/config.rasi':              '~/.config/rasi/config.rasi',

    'dev-utils/pdbrc.py':            '~/.pdbrc.py',
    'vim/vimrc':                     '~/.vimrc',
    'vim/vimrc.local':               '~/.vimrc.local',

    'known_hosts':                   'path',

    'termite/config':                'path',
    'nvim/local_init.vim':           'path',
    'nvim/local_bundles.vim':        'path',

    'gtk-2.0/gtkrc-2.0':             '~/.gtkrc-2.0',
    'gtk-3.0/gtk.css':               '~/.config/gtk-3.0/gtk.css',
    'gtk-3.0/settings.ini':          '~/.config/gtk-3.0/settings.ini',

    'dev-utils/plantuml_style.iuml': 'path',

    'X/Xresources':                  '~/.Xresources',
    'X/default_screenlayout.sh':     '~/.screenlayout/default_screenlayout.sh',
    'X/xprofile':                    '~/.xprofile',
}

if __name__ == "__main__":
    dotfiles = set()
    for root, subdirs, files in os.walk(DOTFILE_DIR):
        dotfiles = dotfiles.union(
            {os.path.relpath(
                os.path.join(root, f),
                DOTFILE_DIR)
             for f in files}
        )

    print(CONFIG_MAP)
    a = 3
