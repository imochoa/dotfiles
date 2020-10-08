#!/usr/bin/env python3

# std imports
import pdb
import os
import sys
import pathlib
import datetime
import logging
import collections
from enum import Enum, auto
import subprocess
from typing import Tuple, Union, List, Iterable, Optional, Dict
import uuid
from io import BytesIO
from zipfile import ZipFile
import shutil
import tempfile
from urllib.request import urlopen
from urllib.parse import quote, urlparse

from concurrent.futures import ThreadPoolExecutor
import threading

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


def dryrun_echo(msg: str) -> None:
    echo(f"\t[DRY RUN]: {msg}", color=bcolors.DEBUG)


def cp(src: pathlib.Path, dest: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        dryrun_echo(f"Would CP:\n\t{src} -> {dest}")
    else:
        shutil.copy2(src=src, dst=dest)


def ln(src: pathlib.Path, dest: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        dryrun_echo(f"Would LINK:\n\t{src} -> {dest}")
    else:
        if dest.is_file():
            rm(dest, dry_run=dry_run)
        os.link(src=src.resolve(), dst=dest.resolve())
        # os.symlink(src=src.resolve(), dst=dest.resolve())


def is_symlink(linkfile: Union[str, pathlib.Path],
               src: Union[None, str, pathlib.Path] = None,
               ) -> bool:
    """
    Checks if *linkfile* is a symlink.
    If a *src* is provided, it also checks to make sure that *linkfile* links to *src*
    """
    linkfile = pathlib.Path(linkfile)
    if not linkfile.is_symlink():
        return False

    if src is None:
        return True

    return linkfile.resolve() == pathlib.Path(src).resolve()


def mkdirs(src: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        dryrun_echo(f"Would MKDIRS:\n\t{src}")
    else:
        os.makedirs(src)


def rm(src: pathlib.Path, dry_run: bool = True) -> None:
    if dry_run:
        dryrun_echo(f"Would RM {src}")
    else:
        os.remove(src)


def get_timestamp() -> str:
    return datetime.datetime.now().strftime('backup_%Y_%m_%d_T_%H_%M_%s')


def get_release_tag(user_and_repo: str) -> str:
    """
    >>> get_latest_release_tag('pdfminer/pdfminer.six')
    """

    # If the input was a URL, parse it
    user_and_repo = urlparse(user_and_repo).path
    user_and_repo = user_and_repo[:-1] if user_and_repo.endswith('/') else user_and_repo
    user_and_repo = user_and_repo[:-9] if user_and_repo.endswith('/releases') else user_and_repo

    # Make the query URL
    url = f"https://github.com/{quote(user_and_repo)}/releases/latest"

    with urlopen(url) as fp:
        # html = fp.read().decode('utf8')
        return fp.url.split('/')[-1]


def get_release_tags(user_and_repos: Union[str, List[str]], max_workers: int = 4) -> List[str]:
    """
    Same as *get_release_tag*, but multi-threaded
    """
    if isinstance(user_and_repos, str):
        user_and_repos = [user_and_repos]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future = executor.map(get_release_tag, user_and_repos)

        return list(future)


def tab(s: str) -> str:
    return '\n\t'.join(s.split('\n'))


# def find_files_with_exts(topdir: str,
#                          exts: Iterable[str],
#                          ) -> Iterable[str]:
#     if isinstance(exts, str):
#         exts = [exts]
#
#     paths = (e if e.startwith('.') else f'.{e}' for e in exts)
#     paths = (os.path.join(topdir, f'**/*{e}') for e in exts)
#
#     return itertools.chain(
#         *(glob.iglob(p, recursive=True)
#           for p in paths))


def decode(s: str) -> str:
    try:
        return s.decode('utf-8')
    except Exception:
        logging.exception("decoding error:", exc_info=True)
    return s


def run_shell_str(shell_str: str,
                  dry_run: bool = True,
                  verbose: bool = False,
                  ) -> Tuple[int, str]:
    returncode, stdout = 0, ''

    if dry_run:
        echo(f"Would have run:\n{shell_str}", color=bcolors.DEBUG)
        return (0, 'DRY RUN -> NO OUTPUT')

    # TODO Use fp_stream?
    with tempfile.TemporaryFile() as fp_stream:
        with subprocess.Popen(shell_str,
                              shell=True,
                              # stdout=fp_stream,
                              # stderr=fp_stream,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              # bufsize=1, # not supported in binary mode
                              ) as p:
            # fp_stream.seek(0)
            while True:
                line = decode(p.stdout.readline().rstrip())
                # line = decode(fp_stream.readline().rstrip())
                if not line:
                    break

                if verbose:
                    echo(f"\t\t{line}", color=bcolors.HEADER)
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
