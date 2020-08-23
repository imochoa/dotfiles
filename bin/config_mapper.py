#!/usr/bin/python3

import collections
import os
import pathlib
import pdb
import shutil
import enum
import datetime
from typing import Optional, Dict

# Paths
THIS_FILE = pathlib.Path(__file__).resolve()
BIN_DIR = THIS_FILE.parent
REPO_DIR = BIN_DIR.parent
DOTFILE_DIR = REPO_DIR / 'dotfiles'

# CONSTANTS
DOTFILE_MAP = {
    'bash/bashrc':                   '~/.bashrc',
    'bash/bash_aliases':             '~/.bash_aliases',
    'bash/bash_functions':           '~/.bash_functions',
    'bash/inputrc':                  '~/.inputrc',
    'bash/bash_profile':             '~/.bash_profile',

    'debugging/pdbrc': '~/.pdbrc',

    # 'i3/i3config':                   '~/.config/i3/config',
    # 'i3/polybar.sh':                 '~/.config/i3/polybar.sh',
    'polybar/colors.ini':            'path2',
    'polybar/config.ini':            'path',
    'polybar/bars.ini':              'path',
    'polybar/modules.ini':           'path',
    'polybar/user_modules.ini':      'path',
    # 'i3/i3blocks.conf':              'path',
    # 'rofi/config.rasi':              '~/.config/rasi/config.rasi',

    # 'vim/vimrc':                     '~/.vimrc',
    # 'vim/vimrc.local':               '~/.vimrc.local',

    # 'known_hosts':                   'path',

    # 'termite/config':                'path',
    # 'nvim/local_init.vim':           'path',
    # 'nvim/local_bundles.vim':        'path',

    'gtk-2.0/gtkrc-2.0':             '~/.gtkrc-2.0',
    'gtk-3.0/gtk.css':               '~/.config/gtk-3.0/gtk.css',
    'gtk-3.0/settings.ini':          '~/.config/gtk-3.0/settings.ini',
    'gtk-4.0/settings.ini':          '~/.config/gtk-4.0/settings.ini',

    # 'plantuml_style.iuml': 'path',

    # 'X/Xresources':                  '~/.Xresources',
    # 'X/default_screenlayout.sh':     '~/.screenlayout/default_screenlayout.sh',
    # 'X/xprofile':                    '~/.xprofile',
}


class bcolors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    DEBUG = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def echo(msg: collections.Iterable,
         color: bcolors = bcolors.INFO,
         sep: str = '',
         ) -> None:
    if not isinstance(msg, str):
        msg = sep.join(msg)
    print(f"{color}{msg}{bcolors.ENDC}", sep=sep)


def cp(src: pathlib.Path, dest: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would CP:\n\t{src} -> {dest}", color=bcolors.DEBUG)
    else:
        shutil.copy2(src=src, dst=dest)


def ln(src: pathlib.Path, dest: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would LINK:\n\t{src} -> {dest}", color=bcolors.DEBUG)
    else:
        if dest.is_file():
            rm(dest, dry_run=dry_run)
        os.link(src=src.resolve(), dst=dest.resolve())


def mkdirs(src: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would MKDIRS:\n\t{src}", color=bcolors.DEBUG)
    else:
        os.makedirs(src)


def rm(src: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would RM {src}", color=bcolors.DEBUG)
    else:
        os.remove(src)


def get_timestamp() -> str:
    return datetime.datetime.now().strftime('backup_%Y_%m_%d_T_%H_%M_%s')


def map_dotfiles_to_paths(homedir: Optional[str] = None,
                          ) -> Dict[str, pathlib.Path]:
    """
    Returns a mapping between each dotfile and its destination
    """

    global DOTFILE_MAP
    # -------------------------------------------------------------------------- #
    # Clean up the dotfile map
    # -------------------------------------------------------------------------- #
    missing_fs = {k for k in DOTFILE_MAP
                  if not (DOTFILE_DIR/k).is_file()}

    if missing_fs:
        echo(["Removing dotfile mappings with missing src files:"]+sorted(missing_fs),
             color=bcolors.WARNING,
             sep='\n\t> ')
        DOTFILE_MAP = {k: v for k, v in DOTFILE_MAP.items()
                       if k not in missing_fs}

    if not homedir:
        homedir = os.path.expanduser('~')
        echo(f"Expanding '~' to '{homedir}'", color=bcolors.INFO)
        DOTFILE_MAP = {k: pathlib.Path(v).expanduser().resolve()
                       for k, v in DOTFILE_MAP.items()}
    elif os.path.isdir(homedir):
        echo(f"Using input home directory: {homedir}")
        DOTFILE_MAP = {k: pathlib.Path(v.replace('~', str(homedir))).resolve()
                       for k, v in DOTFILE_MAP.items()}
    elif (pathlib.Path('~')/homedir).is_dir():
        homedir = pathlib.Path('~')/homedir
        echo(f"Using input home directory: {homedir}")
        DOTFILE_MAP = {k: pathlib.Path(v.replace('~', str(homedir))).resolve()
                       for k, v in DOTFILE_MAP.items()}
    else:
        raise OSError(f"Invalid home directory: {homedir}")

    # -------------------------------------------------------------------------- #
    # Match them
    # -------------------------------------------------------------------------- #
    repo_files = {str(f.relative_to(DOTFILE_DIR)): f.resolve()
                  for f in DOTFILE_DIR.rglob('*')}

    matched_ks = set(repo_files).intersection(DOTFILE_MAP)
    missed_ks = set(DOTFILE_MAP).intersection(repo_files)

    if missed_ks:
        echo(["files without mappings:"]+sorted(missed_ks),
             sep='\n\t> ',
             color=bcolors.WARNING,
             )

    bad_map_ks = {k for k in matched_ks if REPO_DIR in DOTFILE_MAP[k].parents}

    if bad_map_ks:
        echo(["invalid dest mappings:"]+sorted(bad_map_ks),
             sep='\n\t> ',
             color=bcolors.WARNING,
             )
        matched_ks = matched_ks.difference(bad_map_ks)

    if not matched_ks:
        echo(f"No known dotfiles were found!", color=bcolors.FAIL)
        raise ValueError(f"No matched_ks found!")

    return {DOTFILE_DIR/k: DOTFILE_MAP[k] for k in repo_files if k in matched_ks}


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

    if dest.is_file():
        # with open(src, 'rb') as src_fp, open(dest, 'rb') as dest_fp:
        #     same_file = src_fp.readlines() == dest_fp.readlines()
        if keep_backup:
            backup_path = dest.parent / f"{dest.name}_{get_timestamp()}"
            cp(src=dest, dest=backup_path, dry_run=dry_run)

    # TODO HOW TO DETECT HARD LINKS?
    # TODO HOW TO COMPARE SRC AND DEST HARD LINKS?
    pdb.set_trace()
    if src == dest:
        # resolved dest symlink points back to the source!
        return True

    if not dest.parent.is_dir():
        mkdirs(dest.parent, dry_run=dry_run)

    pdb.set_trace()
    ln(src=src, dest=dest, dry_run=dry_run)
    return True


def apply_dotfiles(dry_run: bool = True,
                   homedir: Optional[str] = None,
                   keep_backup: bool = True,
                   ):
    matched_configs = map_dotfiles_to_paths(homedir=homedir)
    for src_config_file, dest_config_file in matched_configs.items():
        print(src_config_file)
        echo(f"{src_config_file} -> {dest_config_file}")
        config_copy(src_config_file,
                    dest_config_file,
                    dry_run=dry_run,
                    keep_backup=keep_backup,
                    )


if __name__ == "__main__":
    apply_dotfiles(dry_run=False)

    echo("\n\nDone!\n\n", color=bcolors.BOLD+bcolors.INFO)
