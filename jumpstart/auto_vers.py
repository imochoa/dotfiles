#!/usr/bin/env python3

# std imports
from typing import Union, Sequence
import pdb

# local imports
from jumpstart.utils import get_release_tags

NAME_TO_REPO_MAP = dict(
    stretchly='hovancik/stretchly',
    neovim='neovim/neovim'
)

# AUTO
ks = sorted(NAME_TO_REPO_MAP)
vs = get_release_tags([NAME_TO_REPO_MAP[k] for k in ks])
NAME_TO_TAG_MAP = {k: t for k, t in zip(ks, vs)}

if __name__ == '__main__':
    print('\n'.join(
        ['PKGs WITH THEIR TAGS']
        + [f'{k:>50} -> {NAME_TO_TAG_MAP[k]}' for k in sorted(NAME_TO_TAG_MAP)])
    )
