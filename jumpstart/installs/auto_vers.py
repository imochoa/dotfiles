#!/usr/bin/env python3

# std imports
from typing import Union, Sequence, Dict, Optional
import pdb

# local imports
from jumpstart.utils import echo, bcolors
from jumpstart.utils import get_release_tags

NAME_TO_REPO_MAP = dict(
    stretchly='hovancik/stretchly',
    neovim='neovim/neovim',
    fontawesome='FortAwesome/Font-Awesome',
    nordic='EliverLara/Nordic',
    nerdfonts='ryanoasis/nerd-fonts',
)


def git_pkg_vers(pkg_keys: Union[None, str, Sequence[str]] = None, ) -> Dict[str, str]:
    pgk_subset = set(NAME_TO_REPO_MAP)
    if pkg_keys:
        pgk_subset = pgk_subset.intersection(pkg_keys)

        lost_inputs = set(pkg_keys).difference(pgk_subset)
        if lost_inputs:
            echo(([f'[{len(lost_inputs)}] UNKNOWN GIT pkg(s)']
                  + [f'[{idx:> 3}] {p}' for idx, p in enumerate(sorted(lost_inputs), start=1)]),
                 color=bcolors.WARNING, sep='\n\t> ')

    if not pgk_subset:
        echo('No GIT pkgs versions will be searched for!', color=bcolors.WARNING, sep='\n\t> ')
        return dict()

    echo(([f'[{len(pgk_subset)}] Filtered APT-GET pkgs:']
          + [f'[{idx:> 3}] {p}' for idx, p in enumerate(sorted(pgk_subset), start=1)]),
         color=bcolors.DEBUG, sep='\n\t> ')

    vers = get_release_tags([NAME_TO_REPO_MAP[k] for k in pgk_subset])
    return {k: v for k, v in zip(pgk_subset, vers)}


if __name__ == '__main__':
    # name_to_tag_map = git_pkg_vers() # All
    name_to_tag_map = git_pkg_vers(['neovim', 'nordic', 'noise'])  # subset

    print('\n'.join(
        ['PKGs WITH THEIR TAGS']
        + [f'{k:>50} -> {name_to_tag_map[k]}' for k in sorted(name_to_tag_map)])
    )
