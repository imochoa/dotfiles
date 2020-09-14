#!/usr/bin/env python3

# std imports
from typing import Union, Sequence, Dict, Tuple, Optional

# local imports
from jumpstart.utils import echo, bcolors
from jumpstart.installs.aptget import build_aptget_pkg_maps

from jumpstart.installs.shell_scripts import *
from jumpstart.installs.snap import build_snap_pkg_maps
from jumpstart.installs.src import *


def build_pkg_maps(pkg_keys: Optional[Sequence[str]] = None) -> Tuple[Dict[str, str], Dict[str, str]]:
    full_install_map, full_remove_map = dict(), dict()

    for fcn in (build_aptget_pkg_maps, build_snap_pkg_maps):
        i_map, r_map = fcn()
        full_install_map.update(i_map)
        full_remove_map.update(r_map)

    return full_install_map, full_remove_map
