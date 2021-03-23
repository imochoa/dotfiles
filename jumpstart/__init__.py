#!/usr/bin/env python3

# std imports
import os
import pathlib
import tempfile

# Local paths
PY_PKG = pathlib.Path(__file__).parent
REPO_DIR = PY_PKG.parent
DOTFILE_DIR = REPO_DIR / "dotfiles"
DOCS_DIR = REPO_DIR / "docs"
TESTS_DIR = REPO_DIR / "tests"
PRIVATE_DIR = REPO_DIR / "private"
TMP = tempfile.gettempdir()

# Constants
USER = os.environ.get("USER")
DISPLAY = os.environ.get("DISPLAY")

HOME = os.environ.get("HOME")
XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME")

HOME = pathlib.Path(HOME) if HOME else None
XDG_CONFIG_HOME = pathlib.Path(XDG_CONFIG_HOME) if XDG_CONFIG_HOME else None

HOME = pathlib.Path(os.environ.get("HOME")) if "HOME" in os.environ else None
XDG_CONFIG_HOME = (
    pathlib.Path(os.environ.get("XDG_CONFIG_HOME"))
    if "XDG_CONFIG_HOME" in os.environ
    else None
)

if not XDG_CONFIG_HOME and HOME:
    XDG_CONFIG_HOME = XDG_CONFIG_HOME = HOME / ".config"
