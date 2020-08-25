##!/usr/bin/env python3

#import pdb
#import os
#import pathlib
#import sys
#import logging
#from enum import Enum, auto
#import subprocess
#from typing import Tuple, Optional

#from . import Fonts
#from .utils import decode, run_shell_str, tab

#CONFIG_CMDS = dict()


#def install_key(key,
#                verbose: bool = False,
#                ) -> Tuple[int, str]:
#    return run_shell_str(
#        shell_str=INSTALL_CMDS[key],
#        verbose=verbose,
#    )


#DOTFILE_MAP = {
#    'bash/bash_functions':           '~/.bash_functions',
#    'bash/inputrc':                  '~/.inputrc',
#    'bash/bashrc':                   '~/.bashrc',
#    'bash/bash_aliases':             '~/.bash_aliases',
#    'bash/bash_profile':             '~/.bash_profile',

#    'i3/i3config':                   '~/.config/i3/config',
#    'i3/polybar.sh':                 '~/.config/i3/polybar.sh',
#    'polybar/colors.ini':            'path2',
#    'polybar/config.ini':            'path',
#    'polybar/bars.ini':              'path',
#    'polybar/modules.ini':           'path',
#    'polybar/user_modules.ini':      'path',
#    'i3/i3blocks.conf':              'path',
#    'rofi/config.rasi':              '~/.config/rasi/config.rasi',

#    'dev-utils/pdbrc.py':            '~/.pdbrc.py',
#    'vim/vimrc':                     '~/.vimrc',
#    'vim/vimrc.local':               '~/.vimrc.local',

#    'known_hosts':                   'path',

#    'termite/config':                'path',
#    'nvim/local_init.vim':           'path',
#    'nvim/local_bundles.vim':        'path',

#    'gtk-2.0/gtkrc-2.0':             '~/.gtkrc-2.0',
#    'gtk-3.0/gtk.css':               '~/.config/gtk-3.0/gtk.css',
#    'gtk-3.0/settings.ini':          '~/.config/gtk-3.0/settings.ini',

#    'plantuml_style.iuml': 'path',

#    'X/Xresources':                  '~/.Xresources',
#    'X/default_screenlayout.sh':     '~/.screenlayout/default_screenlayout.sh',
#    'X/xprofile':                    '~/.xprofile',
#}


#def map_dotfiles_to_paths(homedir: Optional[str] = None,
#                          ) -> Dict[str, str]:

#    # Find all of the files
#    repo_files = set()
#    for root, subdirs, files in os.walk(DOTFILE_DIR):
#        repo_files = repo_files.union(
#            {os.path.join(root, f) for f in files}
#        )
#    repo_files = {os.path.relpath(f, DOTFILE_DIR): f for f in repo_files}

#    matched_configs = dict()
#    unmatched_files = []

#    while repo_files:
#        matched_keys = set(repo_files).intersection(DOTFILE_MAP)
#        matched_configs.update(
#            {repo_files[k]: DOTFILE_MAP[k] for k in matched_keys}
#        )
#        repo_files = {k: repo_files[k]
#                      for k in repo_files if k not in matched_keys}

#        # Drill down one level
#        file_remap = {k: pathlib.Path(k).parts[1:] for k in repo_files}

#        lost_files = {k for k, v in file_remap.items() if not v}
#        if lost_files:
#            lost_filepaths = [repo_files[k] for k in lost_files]
#            unmatched_files.extend(lost_filepaths)
#            # print(
#            # f"lost: [{len(lost_files)}]", *lost_filepaths, sep='\n\t> ')

#        repo_files = {os.path.join(*file_remap[k]): v
#                      for k, v in repo_files.items()
#                      if k not in lost_files}

#    # Prepare output report!
#    matched_keys = sorted(matched_configs)

#    print(f"Expanding '~' to '{os.path.expanduser('~')}'")

#    matched_configs = {k: os.path.expanduser(v)
#                       for k, v in matched_configs.items()}

#    match_report_list = [
#        f'[{idx: >2}] '
#        # f'{os.path.relpath(k,DOTFILE_DIR): >30}'
#        f'{os.path.join(*pathlib.Path(k).parts[-2:]): >30}'
#        f' -> {matched_configs[k]: <30}'
#        for idx, k in enumerate(matched_keys, start=1)]
#    print(f"Matched [{len(matched_configs)}]:",
#          *match_report_list,
#          sep='\n\t')

#    if unmatched_files:
#        print(f"Unmatched: [{len(unmatched_files)}]",
#              *unmatched_files,
#              sep='\n\t> ')

#    return matched_configs


#def config_copy(src: str,
#                dest: str,
#                dry_run: bool = True,
#                keep_backup: bool = True,
#                ) -> bool:
#    """
#    returns: True if it worked, False otherwise
#    """
#    print()
#    if not os.path.isfile(src):
#        print(f'{src} NOT FOUND!')
#        return False

#    # TODO If it's a hardlink to src... skip!
#    if keep_backup and os.path.isfile(dest):
#        suffix_idx = 1
#        while True:
#            backup_path = f"{dest}.bak{suffix_idx}"

#            if os.path.isfile(backup_path):
#                suffix_idx += 1
#            else:
#                break

#        if dry_run:
#            op_str = "Would MOVE"
#        else:
#            op_str = "MOVED"
#            # TODO
#            print("DO!")
#        print(f"\t{op_str}:\n\t   {dest} ->\n\t-> {backup_path}")

#    if dry_run:
#        op_str = "Would HARD-LINK"
#    else:
#        op_str = "HARD-LINKED"
#        # TODO
#        print("DO!")
#    print(f"\t{op_str}:\n\t   {src} ->\n\t-> {dest}")
#    return True


#def apply_dotfiles(dry_run: bool = True,
#                   homedir: Optional[str] = None,
#                   keep_backup: bool = True,
#                   ):
#    matched_configs = map_dotfiles_to_paths(homedir=homedir)
#    for src_config_file, dest_config_file in matched_configs.items():
#        config_copy(src_config_file,
#                    dest_config_file,
#                    dry_run=dry_run,
#                    keep_backup=keep_backup,
#                    )


#if __name__ == "__main__":
#    apply_dotfiles()

#    print("\n\nDone!\n\n")
