#!/usr/bin/python3

import os
import enum
import pdb
import shutil

# Paths
THIS_FILE = os.path.abspath(__file__)
REPO_DIR = os.path.dirname(THIS_FILE)
DOTFILE_DIR = os.path.join(REPO_DIR, 'dotfiles')


class Config(enum.Enum):
    # BASH
    bashrc = enum.auto()
    bash_aliases = enum.auto()
    bash_functions = enum.auto()
    bash_inputrc = enum.auto()

    # GTK
    gtk_2 = enum.auto()
    gtk_3 = enum.auto()
    vim_local_init = enum.auto()
    vim_local_bundles = enum.auto()
    nvim_local_init = enum.auto()
    nvim_local_bundles = enum.auto()

    i3 = enum.auto()
    i3_polybar = enum.auto()
    termite = enum.auto()

    i3_rofi = enum.auto()
    xresources = enum.auto()
    xprofile = enum.auto()
    i3_blocks = enum.auto()
    pdbpp_rc = enum.auto()
    plantuml = enum.auto()


SRC_CONFIG_MAP = {
    'bash/bash_functions':            Config.bash_functions,
    'bash/inputrc':                   Config.bash_inputrc,
    'bash/bashrc':                    Config.bashrc,
    'bash/bash_aliases':              Config.bash_aliases,
    'bash/bash_profile':              Config.bash_profile,
    'i3/i3config':                    'path1',
    'i3/polybar/colors.ini':          'path2',
    'dev-utils/pdbrc.py':             'path3',
    'vim/vimrc':                      'path4',
    'i3/polybar/config.ini':          'path',
    'i3/polybar/bars.ini':            'path',
    'X/default_screenlayout.sh':      'path',
    'vim/vimrc.local':                'path',
    'known_hosts':                    'path',
    'nvim/local_init.vim':            'path',
    'i3/polybar.sh':                  'path',
    'X/Xresources':                   'path',
    'gtk-3.0/gtk.css':                'path',
    'rofi/config.rasi':               'path',
    'i3/i3blocks.conf':               'path',
    'nvim/local_bundles.vim':         'path',
    'termite/config':                 'path',
    'i3/polybar/user_modules.ini':    'path',
    'dev-utils/plantuml_style.iuml':  'path',
    'i3/polybar/modules.ini':         'path',
    'X/xprofile':                     'path',
}

DEST_CONFIG_MAP = {
    Config.bashrc:              '/where/to/save',
    Config.bash_aliases:        '/where/to/save',
    Config.bash_functions:      '/where/to/save',
    Config.bash_inputrc:        '/where/to/save',
    Config.gtk_2:               '/where/to/save',
    Config.gtk_3:               '/where/to/save',
    Config.vim_local_init:      '/where/to/save',
    Config.vim_local_bundles:   '/where/to/save',
    Config.nvim_local_init:     '/where/to/save',
    Config.nvim_local_bundles:  '/where/to/save',
    Config.i3:                  '/where/to/save',
    Config.i3_polybar:          '/where/to/save',
    Config.termite:             '/where/to/save',
    Config.i3_rofi:             '/where/to/save',
    Config.xresources:          '/where/to/save',
    Config.xprofile:            '/where/to/save',
    Config.i3_blocks:           '/where/to/save',
    Config.pdbpp_rc:            '/where/to/save',
    Config.plantuml:            '/where/to/save',
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

    print(SRC_CONFIG_MAP)
