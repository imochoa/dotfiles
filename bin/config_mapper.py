#!/usr/bin/python3

# std imports
import collections
import os
import sys
import pathlib
import pdb
import shutil
import enum
import datetime
from typing import Optional, Dict, Set

# Paths
THIS_FILE = pathlib.Path(__file__).resolve()
BIN_DIR = THIS_FILE.parent
REPO_DIR = BIN_DIR.parent
DOTFILE_DIR = REPO_DIR / 'dotfiles'

# local imports
sys.path.append(str(REPO_DIR))
import jumpstart
from jumpstart.dotfile_map import DOTFILE_MAP
from jumpstart.utils import (
        bcolors,
        echo,
        rm,
        cp,
        ln,
        rm,
        mkdirs,
        get_timestamp,
        )

# CONSTANTS
# DOTFILE_MAP = {
#     'bash/bashrc':                   '~/.bashrc',
#     'bash/bash_aliases':             '~/.bash_aliases',
#     'bash/bash_functions':           '~/.bash_functions',
#     'bash/inputrc':                  '~/.inputrc',
#     'bash/bash_profile':             '~/.bash_profile',

#     'debugging/pdbrc': '~/.pdbrc',

#     # 'i3/i3config':                   '~/.config/i3/config',
#     # 'i3/polybar.sh':                 '~/.config/i3/polybar.sh',
#     'polybar/colors.ini':            'path2',
#     'polybar/config.ini':            'path',
#     'polybar/bars.ini':              'path',
#     'polybar/modules.ini':           'path',
#     'polybar/user_modules.ini':      'path',
#     # 'i3/i3blocks.conf':              'path',
#     # 'rofi/config.rasi':              '~/.config/rasi/config.rasi',

#     # 'vim/vimrc':                     '~/.vimrc',
#     # 'vim/vimrc.local':               '~/.vimrc.local',

#     # 'known_hosts':                   'path',

#     # 'termite/config':                'path',
#     # 'nvim/local_init.vim':           'path',
#     # 'nvim/local_bundles.vim':        'path',

#     'gtk-2.0/gtkrc-2.0':             '~/.gtkrc-2.0',
#     'gtk-3.0/gtk.css':               '~/.config/gtk-3.0/gtk.css',
#     'gtk-3.0/settings.ini':          '~/.config/gtk-3.0/settings.ini',
#     'gtk-4.0/settings.ini':          '~/.config/gtk-4.0/settings.ini',

#     # 'plantuml_style.iuml': 'path',

#     # 'X/Xresources':                  '~/.Xresources',
#     # 'X/default_screenlayout.sh':     '~/.screenlayout/default_screenlayout.sh',
#     # 'X/xprofile':                    '~/.xprofile',
# }


def map_dotfiles_to_paths(
        dotfile_map: Dict[str,str],
        homedir: Optional[str] = None,
                          ) -> Dict[str, pathlib.Path]:
    """
    Returns a mapping between each dotfile and its destination
    """

    # -------------------------------------------------------------------------- #
    # Clean up the dotfile map
    # -------------------------------------------------------------------------- #
    missing_fs = {k for k in dotfile_map
                  if not (DOTFILE_DIR/k).is_file()}

    if missing_fs:
        echo(["Removing dotfile mappings with missing src files:"]+sorted(missing_fs),
             color=bcolors.WARNING,
             sep='\n\t> ')
        dotfile_map = {k: v for k, v in dotfile_map.items()
                       if k not in missing_fs}

    if not homedir:
        homedir = os.path.expanduser('~')
        echo(f"Expanding '~' to '{homedir}'\n", color=bcolors.INFO)
        dotfile_map = {k: pathlib.Path(v).expanduser().resolve()
                       for k, v in dotfile_map.items()}
    elif os.path.isdir(homedir):
        echo(f"Using input home directory: {homedir}\n")
        dotfile_map = {k: pathlib.Path(v.replace('~', str(homedir))).resolve()
                       for k, v in dotfile_map.items()}
    elif (pathlib.Path('~')/homedir).is_dir():
        homedir = pathlib.Path('~')/homedir
        echo(f"Using input home directory: {homedir}\n")
        dotfile_map = {k: pathlib.Path(v.replace('~', str(homedir))).resolve()
                       for k, v in dotfile_map.items()}
    else:
        raise OSError(f"Invalid home directory: {homedir}")

    # -------------------------------------------------------------------------- #
    # Match them
    # -------------------------------------------------------------------------- #
    repo_files = {str(f.relative_to(DOTFILE_DIR)): f.resolve()
                  for f in DOTFILE_DIR.rglob('*')}

    matched_ks = set(repo_files).intersection(dotfile_map)
    missed_ks = set(dotfile_map).intersection(repo_files)

    if missed_ks:
        echo(["files without mappings:"]+sorted(missed_ks),
             sep='\n\t> ',
             color=bcolors.WARNING,
             )

    bad_map_ks = {k for k in matched_ks if REPO_DIR in dotfile_map[k].parents}

    if bad_map_ks:
        echo(["invalid dest mappings:"]+sorted(bad_map_ks),
             sep='\n\t> ',
             color=bcolors.WARNING,
             )
        matched_ks = matched_ks.difference(bad_map_ks)

    if not matched_ks:
        echo(f"No known dotfiles were found!", color=bcolors.FAIL)
        raise ValueError(f"No matched_ks found!")

    return {DOTFILE_DIR/k: dotfile_map[k] for k in repo_files if k in matched_ks}


def config_copy(src: pathlib.Path,
                dest: pathlib.Path,
                dry_run: bool = True,
                keep_backup: bool = True,
                ) -> bool:
    """
    returns: True if it worked, False otherwise
    """
    if not src.is_file():
        echo(f'{src} NOT FOUND!', color=bcolors.DEBUG)
        return False

    if dest.is_file() and os.path.samefile(src,dest):
        echo(f"Already hard-linked: {dest}\n", color=bcolors.DEBUG)
        # resolved dest hard-link points back to the source!
        return False

    if not dest.parent.is_dir():
        mkdirs(dest.parent, dry_run=dry_run)

    if dest.is_file() and keep_backup:
        backup_path = dest.parent / f"{dest.name}_{get_timestamp()}"
        cp(src=dest, dest=backup_path, dry_run=dry_run)

    ln(src=src, dest=dest, dry_run=dry_run)
    return True


def apply_dotfiles(input_dotfiles:Set,
        dry_run: bool = True,
                   homedir: Optional[str] = None,
                   keep_backup: bool = True,
                   ):

    if not input_dotfiles:
        echo("Empty dotfile input, skipping!",color=bcolors.WARNING)

    if not isinstance(input_dotfiles,set):
        input_dotfiles=set(input_dotfiles)

    invalid_keys={k for k in input_dotfiles 
            if k not in DOTFILE_MAP}

    if invalid_keys:
        echo(["Removing invalid install keys:"]+sorted(invalid_keys),
             color=bcolors.WARNING,
             sep='\n\t> ')
        input_dotfiles = input_dotfiles.difference(invalid_keys)

    dotfile_map = {k:DOTFILE_MAP[k] for k in input_dotfiles}

    matched_configs = map_dotfiles_to_paths(dotfile_map, homedir=homedir)
    for src_config_file, dest_config_file in matched_configs.items():
        if config_copy(src_config_file,
                    dest_config_file,
                    dry_run=dry_run,
                    keep_backup=keep_backup,
                    ):
            echo(f"{src_config_file} -> {dest_config_file}", color=bcolors.INFO)

if __name__ == "__main__":

    dotfile_keys={

            'bash/bashrc',
            'bash/bash_aliases',
            'bash/bash_functions',
            'bash/inputrc',
            'bash/bash_profile',

            'i3/config',

            'i3/scripts/polybar.sh',
            'i3/scripts/lock.sh',
            'i3/polybar/config.ini',
            'i3/polybar/colors.ini',
            'i3/polybar/bars.ini',
            'i3/polybar/modules.ini',
            'i3/polybar/user_modules.ini',

            'nvim/init.vim',
            'nvim/coc-settings.json',
            'nvim/package-lock.json',
            'nvim/after/autocommands.vim',
            'nvim/after/general-settings.vim',
            'nvim/after/mappings.vim',
            'nvim/after/visual.vim',
            'nvim/after/plugin/plugin-config.vim',
            'nvim/after/compiler/cpp.vim'            ,
            'nvim/after/compiler/dummy.vim'          ,
            'nvim/after/compiler/tardyscript.vim'    ,
            'nvim/after/compiler/tsconfig.vim'       ,
            'nvim/after/compiler/tslint.vim'         ,
            'nvim/after/compiler/typescript.vim'     ,
    }




    apply_dotfiles(dotfile_keys, dry_run=False)
    echo("\n\nDone!\n\n", color=bcolors.BOLD+bcolors.DEBUG)

