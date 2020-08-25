#!/usr/bin/env python3

# std imports
import pdb

# local imports
from jumpstart.install_pkg import INSTALL_PKGS
from jumpstart.install_ui import INSTALL_UI


#TODO Check for collisions!
INSTALL_CMDS = dict()

INSTALL_CMDS.update(INSTALL_PKGS)
INSTALL_CMDS.update(INSTALL_UI)


if __name__ == '__main__':
    # TODO REPORT
    pass
