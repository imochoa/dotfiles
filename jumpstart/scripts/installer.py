#!/usr/bin/python3

# std imports
import collections
import argparse
import os
import sys
import pathlib
import pdb
import shutil
from enum import Enum, auto
import subprocess
import datetime
from typing import Optional, Dict, Tuple, Set

# local imports
from jumpstart import DOTFILE_DIR, REPO_DIR
from jumpstart.utils import (
    bcolors,
    echo,
    rm,
    cp,
    ln,
    rm,
    mkdirs,
    decode,
    run_shell_str,
    tab,
)
from jumpstart.install_map import INSTALL_CMDS


def apply_installs(
        input_installs: Set[str],
        dry_run: bool = True,
        verbose: bool = False,
        homedir: Optional[str] = None,
        # keep_backup: bool = True,
) -> None:
    if not input_installs:
        echo("Empty install input, skipping!", color=bcolors.WARNING)

    if not isinstance(input_installs, set):
        input_installs = set(input_installs)

    invalid_keys = {k for k in input_installs
                    if k not in INSTALL_CMDS}

    if invalid_keys:
        echo(["Removing invalid install keys:"] + sorted(invalid_keys),
             color=bcolors.WARNING,
             sep='\n\t> ')
        input_installs = input_installs.difference(invalid_keys)

    total = len(input_installs)
    failed_ks = []
    for idx, k in enumerate(input_installs, start=1):

        echo(f"\n\t[{idx:>4}/{total}]: {k}\n\n", color=bcolors.INFO)

        if run_shell_str(
                shell_str=INSTALL_CMDS[k],
                dry_run=dry_run,
                verbose=verbose,
        ):
            echo(f"\n\t\t[OK!] [{k}]\n\n", color=bcolors.INFO)
        else:
            failed_ks.append(k)
            echo(f"\n\t\t[FAILED!] [{k}]\n", color=bcolors.FAILED)

    if failed_ks:
        echo([f"There were {len(failed_ks)} failed installs:"] + sorted(failed_ks),
             color=bcolors.FAILED,
             sep='\n\t> ')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("square",
                        help="display a square of a given number")
    args = parser.parse_args()

    install_keys = {
        'ssh',
        'trash_cli',
        'exfat',
        'slack',
        'git',
        'tree',
        'firewall_gui',
        'docker',
        'docker_compose',
        'pavucontrol',
        'vlc',
        'entr',
        'i3',
        'shutter',
        'wrong_key_remove_this',
    }

    echo("\n\nPreparing to install...\n\n", color=bcolors.BOLD + bcolors.INFO)
    apply_installs(install_keys, dry_run=True, verbose=True)
    echo("\n\nDone!\n\n", color=bcolors.BOLD + bcolors.INFO)
