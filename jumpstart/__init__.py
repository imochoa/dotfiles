#!/usr/bin/env python3

import pathlib
import tempfile

# Paths
PY_PKG = pathlib.Path(__file__).parent
REPO_DIR = PY_PKG.parent
DOTFILE_DIR = REPO_DIR / 'dotfiles'
TMP = tempfile.gettempdir()
