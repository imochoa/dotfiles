#!/usr/bin/env python3

import pdb
import os
import shutil
import itertools
import glob
import pathlib
import sys
import logging
from enum import Enum, auto
import subprocess
from typing import Tuple, Union, Iterable

import zipfile

from . import Fonts
from .utils import (decode,
                    run_shell_str,
                    tab,
                    download_and_unzip,
                    TempDir,
                    cp,
                    find_files_with_exts,
                    )


FONTDIR = '/usr/local/share/fonts/'

FONT_URLS = dict()

FONT_URLS[Fonts.fontawesome] = 'https://github.com/FortAwesome/Font-Awesome/archive/5.12.1.zip'


def install_font(key):
    install_zip_font(FONT_URLS[key])

#
#
# TODO Add multithreading here...
# TODO Retry if html err?


def install_zip_font(zip_url: str,
                     verbose: bool = True,
                     ) -> None:

    # Make sure the font dir exists...
    os.makedirs(FONTDIR, exist_ok=True)

    with TempDir() as tmpdir:

        download_and_unzip(zip_url,
                           outdir=tmpdir)
        font_files = find_files_with_exts(tmpdir,
                                          exts=['ttf', 'otf'])
        for font_src in font_files:
            cp(src=font_src,
               dst=FONTDIR,
               verbose=verbose,
               )


# REbuild font cache
#
def rebuild_font_cache() -> None:
    # TODO
    return subprocess.run('fc-cache -f -v')


def check_font_install(fontname: str) -> bool:

    subprocess.run('fc-list | grep "<name-of-font>"')
    # Check if fontname is in there
    #
    return True


if __name__ == '__main__':
    pass
