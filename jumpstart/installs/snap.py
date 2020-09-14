#!/usr/bin/env python3

# std imports
from typing import Union, Sequence, Optional, List, Dict, Tuple
import pdb

# local imports
from jumpstart.utils import echo, bcolors
from jumpstart.installs.cmd_builders import snap_install, snap_remove

TRIVIAL_PGKS = [
    'slack',
    'pycharm-community',
    'pycharm-professional',
]

PKG_CHANNELS = dict()

RENAMED_PKGs = dict()


def build_snap_pkg_maps(pkg_keys: Optional[Sequence[str]] = None, ) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Gets the commands for the packages with keys *pkg_keys* and returns the (*install_map*, *remove map*)
    """
    pkg_subset = set(TRIVIAL_PGKS).union(RENAMED_PKGs)

    if pkg_keys:
        pkg_subset = pkg_subset.intersection(pkg_keys)
        lost_inputs = set(pkg_keys).difference(pkg_subset)
        if lost_inputs:
            echo(([f'[{len(lost_inputs)}] UNKNOWN SNAP pkg(s)']
                  + [f'[{idx:> 3}] {p}' for idx, p in enumerate(sorted(lost_inputs), start=1)]),
                 color=bcolors.WARNING, sep='\n\t> ')

    if not pkg_subset:
        echo('No APT-GET pkgs will be installed!', color=bcolors.WARNING, sep='\n\t> ')
        return dict(), dict()

    if pkg_keys:
        echo(([f'[{len(pkg_subset)}] Filtered SNAP pkgs:']
              + [f'[{idx:> 3}] {p}' for idx, p in enumerate(sorted(pkg_subset), start=1)]),
             color=bcolors.DEBUG, sep='\n\t> ')
    install_map, remove_map = dict(), dict()

    for pkg in pkg_subset:
        # Explode each name into all of the subpackages it contains
        subpkgs_to_install = [pkg]
        channels = [PKG_CHANNELS.get(k) for k in subpkgs_to_install]

        # Get their "real-names" as opposed to our keys
        pkgs = [RENAMED_PKGs.get(p, p) for p in subpkgs_to_install]

        install_map[pkg] = snap_install(pkgs=pkgs, channels=channels)
        remove_map[pkg] = snap_remove(pkgs=pkgs, channels=channels)

    return install_map, remove_map


if __name__ == '__main__':
    full_install_map, full_remove_map = build_snap_pkg_maps()  # All commands:
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
