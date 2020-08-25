#!/usr/bin/env python3

# std imports
import pdb
import os
import sys
import pathlib
import logging
import collections
from enum import Enum, auto
import subprocess
from typing import Tuple, Union, List, Iterable
import uuid
from io import BytesIO
from zipfile import ZipFile
import shutil
import tempfile
from urllib.request import urlopen

# local imports
from jumpstart import TMP

class bcolors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    DEBUG = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def echo(msg: collections.Iterable,
         color: bcolors = bcolors.INFO,
         sep: str = '',
         ) -> None:
    if not isinstance(msg, str):
        msg = sep.join(msg)
    print(f"{color}{msg}{bcolors.ENDC}", sep=sep)


def cp(src: pathlib.Path, dest: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would CP:\n\t{src} -> {dest}", color=bcolors.DEBUG)
    else:
        shutil.copy2(src=src, dst=dest)


def ln(src: pathlib.Path, dest: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would LINK:\n\t{src} -> {dest}", color=bcolors.DEBUG)
    else:
        if dest.is_file():
            rm(dest, dry_run=dry_run)
        os.link(src=src.resolve(), dst=dest.resolve())


def mkdirs(src: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would MKDIRS:\n\t{src}", color=bcolors.DEBUG)
    else:
        os.makedirs(src)


def rm(src: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        echo(f"Would RM {src}", color=bcolors.DEBUG)
    else:
        os.remove(src)


def get_timestamp() -> str:
    return datetime.datetime.now().strftime('backup_%Y_%m_%d_T_%H_%M_%s')


class TempDir:
    def __init__(self, dirname: Union[None, str] = None):
        self.tmpdir = \
            os.path.join(TMP,
                         dirname or f'{uuid.uuid4()}')

    def __enter__(self):
        # os.makedirs(self.tmpdir, exist_ok=True)
        os.makedirs(self.tmpdir)
        return self.tmpdir

    def __exit__(self, type, value, traceback):
        shutil.rmtree(self.tmpdir)


def tab(s: str) -> str:
    return '\n\t'.join(s.split('\n'))


def find_files_with_exts(topdir: str,
                         exts: Iterable[str],
                         ) -> Iterable[str]:

    if isinstance(exts, str):
        exts = [exts]

    paths = (e if e.startwith('.') else f'.{e}' for e in exts)
    paths = (os.path.join(topdir, f'**/*{e}') for e in exts)

    return itertools.chain(
        *(glob.iglob(p, recursive=True)
          for p in paths))


# def cp(src: str, dst: str, verbose: bool = True) -> str:

#     new_dst = shutil.copy(src, dst)

#     if verbose:
#         print(f"\t> cp {os.path.basename(src)} -> {new_dst}")

#     return new_dst


def decode(s: str) -> str:
    try:
        return s.decode('utf-8')
    except Exception:
        logging.exception("decoding error:", exc_info=True)
    return s


def run_shell_str(shell_str: str,
                    dry_run:bool=True,
                  verbose: bool = False,
                  ) -> Tuple[int, str]:

    returncode, stdout = 0, ''

    if dry_run:
        echo(f"Would have run:\n\t{shell_str}", color=bcolors.DEBUG)
        return (0, 'DRY RUN -> NO OUTPUT')

    # TODO

    with tempfile.TemporaryFile() as fp_stream:
        with subprocess.Popen(shell_str,
                              shell=True,
                              stdout=fp_stream,
                              stderr=fp_stream,
                              # stdout=subprocess.PIPE,
                              # stderr=subprocess.STDOUT,
                              bufsize=1,
                              ) as p:
            while True:
                line = decode(p.stdout.readline().rstrip())
                if not line:
                    break
                
                if verbose:
                    sys.stdout.write(line)
                stdout += line
            returncode = p.returncode

    return returncode, stdout


def download_and_unzip(zip_url: str,
                       outdir: str,
                       ) -> List[str]:

    resp = urlopen(zip_url)
    zipped = ZipFile(BytesIO(resp.read()))
    # for line in zipped.open(filepath).readlines():
    #     print(line.decode('utf-8'))
    #

    os.makedirs(outdir, exist_ok=True)
    zipped.extractall(outdir)

    # Returns the names of the files
    return zipped.namelist()


# def run_shell_str_old(shell_str: str) -> Tuple[int, str]:
#     p = subprocess.run(
#         shell_str,
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.STDOUT,
#     )
#     return p.returncode, p.stdout.decode('ascii')

if __name__ == '__main__':
    pass
