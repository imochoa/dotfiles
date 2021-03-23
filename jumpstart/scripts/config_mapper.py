#!/usr/bin/python3

# std imports
import os
import sys
import pathlib
import argparse
import typing as T

# local imports
from jumpstart import DOTFILE_DIR, REPO_DIR, utils
from jumpstart.configs.dotfile_map import (
    DOTFILE_MAP,
    map_dotfiles_to_paths,
    report_dotmap,
)


# def map_dotfiles_to_paths(
#         dotfile_map: Dict[str, str],
#         homedir: Optional[str] = None,
# ) -> Dict[str, pathlib.Path]:
#     """
#     Returns a mapping between each dotfile and its destination
#     """
#
#     # -------------------------------------------------------------------------- #
#     # Clean up the dotfile map
#     # -------------------------------------------------------------------------- #
#     missing_fs = {k for k in dotfile_map
#                   if not (DOTFILE_DIR / k).is_file()}
#
#     if missing_fs:
#         echo(["Removing dotfile mappings with missing src files:"] + sorted(missing_fs),
#              color=utils.bcolors.WARNING,
#              sep='\n\t> ')
#         dotfile_map = {k: v for k, v in dotfile_map.items()
#                        if k not in missing_fs}
#
#     if not homedir:
#         homedir = os.path.expanduser('~')
#         echo(f"Expanding '~' to '{homedir}'\n", color=utils.bcolors.INFO)
#         dotfile_map = {k: pathlib.Path(v).expanduser().resolve()
#                        for k, v in dotfile_map.items()}
#     elif os.path.isdir(homedir):
#         echo(f"Using input home directory: {homedir}\n")
#         dotfile_map = {k: pathlib.Path(v.replace('~', str(homedir))).resolve()
#                        for k, v in dotfile_map.items()}
#     elif (pathlib.Path('~') / homedir).is_dir():
#         homedir = pathlib.Path('~') / homedir
#         echo(f"Using input home directory: {homedir}\n")
#         dotfile_map = {k: pathlib.Path(v.replace('~', str(homedir))).resolve()
#                        for k, v in dotfile_map.items()}
#     else:
#         raise OSError(f"Invalid home directory: {homedir}")
#
#     # -------------------------------------------------------------------------- #
#     # Match them
#     # -------------------------------------------------------------------------- #
#     repo_files = {str(f.relative_to(DOTFILE_DIR)): f.resolve()
#                   for f in DOTFILE_DIR.rglob('*')}
#
#     matched_ks = set(repo_files).intersection(dotfile_map)
#     missed_ks = set(repo_files).difference(repo_files)
#
#     if missed_ks:
#         echo(["files without mappings:"] + sorted(missed_ks),
#              sep='\n\t> ',
#              color=utils.bcolors.WARNING,
#              )
#
#     bad_map_ks = {k for k in matched_ks if REPO_DIR in dotfile_map[k].parents}
#
#     if bad_map_ks:
#         echo(["invalid dest mappings:"] + sorted(bad_map_ks),
#              sep='\n\t> ',
#              color=utils.bcolors.WARNING,
#              )
#         matched_ks = matched_ks.difference(bad_map_ks)
#
#     if not matched_ks:
#         echo(f"No known dotfiles were found!", color=utils.bcolors.FAIL)
#         raise ValueError(f"No matched_ks found!")
#
#     return {DOTFILE_DIR / k: dotfile_map[k] for k in repo_files if k in matched_ks}


def soft_config_copy(
    src: pathlib.Path,
    dest: pathlib.Path,
    dry_run: bool = True,
    keep_backup: bool = True,
) -> bool:
    """
    returns: True if it worked, False otherwise
    """
    if not src.is_file():
        utils.echo(f"{src} NOT FOUND!", color=utils.bcolors.DEBUG)
        return False

    if dest.is_file() and utils.is_symlink(dest, src):
        utils.echo(f"Already soft-linked: {dest}\n", color=utils.bcolors.DEBUG)
        return False

    if not dest.parent.is_dir():
        utils.mkdirs(dest.parent, dry_run=dry_run)

    if dest.is_file() and keep_backup:
        backup_path = dest.parent / f"{dest.name}_{utils.get_timestamp()}"
        utils.cp(src=dest, dest=backup_path, dry_run=dry_run)

    utils.soft_ln(src=src, dest=dest, dry_run=dry_run)
    return True


def hard_config_copy(
    src: pathlib.Path,
    dest: pathlib.Path,
    dry_run: bool = True,
    keep_backup: bool = True,
) -> bool:
    """
    returns: True if it worked, False otherwise
    """
    if not src.is_file():
        utils.echo(f"{src} NOT FOUND!", color=utils.bcolors.DEBUG)
        return False

    if dest.is_file() and os.path.samefile(src, dest):
        utils.echo(f"Already hard-linked: {dest}\n", color=utils.bcolors.DEBUG)
        # resolved dest hard-link points back to the source!
        return False

    if not dest.parent.is_dir():
        utils.mkdirs(dest.parent, dry_run=dry_run)

    if dest.is_file() and keep_backup:
        backup_path = dest.parent / f"{dest.name}_{utils.get_timestamp()}"
        utils.cp(src=dest, dest=backup_path, dry_run=dry_run)

    utils.hard_ln(src=src, dest=dest, dry_run=dry_run)
    return True


def apply_dotfiles(
    input_dotfiles: T.Set,
    dry_run: bool = True,
    homedir: T.Optional[str] = None,
    keep_backup: bool = True,
) -> None:
    if not input_dotfiles:
        utils.echo("Empty dotfile input, skipping!", color=utils.bcolors.WARNING)
        utils.echo(
            f"Possible keys:\n{report_dotmap(DOTFILE_MAP)}", color=utils.bcolors.INFO
        )
        return None

    if not isinstance(input_dotfiles, set):
        input_dotfiles = set(input_dotfiles)

    # Case-insensitive matching
    l_map = {k.lower(): k for k in DOTFILE_MAP}
    unkown_keys = {k for k in input_dotfiles if k.lower() not in l_map}
    known_keys = {l_map[k.lower()] for k in input_dotfiles if k.lower() in l_map}

    # give unkown keys the chance to expand
    expanded_keys = set()
    invalid_keys = set()
    for unmatched_key in unkown_keys:
        matched_keys = [
            known_k
            for l_k, known_k in l_map.items()
            if l_k.startswith(unmatched_key.lower())
        ]
        if not matched_keys:
            invalid_keys.add(unmatched_key)
        else:
            expanded_keys.update(matched_keys)

    # match_keys
    if invalid_keys:
        utils.echo(
            ["Removing invalid install keys:"] + sorted(invalid_keys),
            color=utils.bcolors.WARNING,
            sep="\n\t> ",
        )
    input_dotfiles = known_keys.union(expanded_keys)

    # Filter the dotfile map
    dotfile_map = {k: DOTFILE_MAP[k] for k in input_dotfiles}

    dotabsfilepath_map = map_dotfiles_to_paths(dotfile_map, homedir=homedir)
    for src_config_file, dest_config_file in dotabsfilepath_map.items():
        if soft_config_copy(
            src_config_file,
            dest_config_file,
            dry_run=dry_run,
            keep_backup=keep_backup,
        ):
            utils.echo(
                f"{src_config_file} -> {dest_config_file}", color=utils.bcolors.INFO
            )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=f"Choose what config files to link")

    parser.add_argument(
        "dotfiles",
        type=str,
        nargs="*",
        help=(
            "Which dotfiles to link, separated by spaces (e.g. 'ssh xclip sxiv') or a file with one "
            "dotfile per line. Run the command without any inputs to see all possibilities, "
            "or with 'all' to configure everything. If you just specify the beginning of a dotfile "
            "path, it will be expanded to all matches"
        ),
    )

    parser.add_argument(
        "-d",
        "--dry",
        action="store_true",
        help="For debugging. When set, the script won't actually install anything, just report back",
    )

    parser.add_argument(
        "-c",
        "--copy",
        action="store_true",
        help=(
            "Copy the config files instead of linking to them (by default)."
            " That way, you can delete the repo and keep the dotfiles"
        ),
    )

    parser.add_argument("-v", "--verbose", action="store_true", help="More output")

    parser.add_argument(
        "-y", "--yes", action="store_true", help="Don't ask for confirmation"
    )

    args = parser.parse_args()
    input_dotfiles = args.dotfiles
    dry_run = args.dry
    # dry_run = True  # TODO DEBUGGING

    parser = argparse.ArgumentParser()

    input_paths = [f for f in input_dotfiles if os.path.isfile(f)]
    input_dotfiles = [f for f in input_dotfiles if f not in input_paths]

    for f in input_paths:
        # TODO DOES THIS WORK?
        with open(f, "r") as fp:
            input_dotfiles.extend(fp.readlines())

    # No inputs?
    if not input_dotfiles:
        utils.echo(f"No inputs given!", color=utils.bcolors.INFO)
        utils.echo(
            f"Possible keys:\n{report_dotmap(DOTFILE_MAP)}", color=utils.bcolors.INFO
        )
        sys.exit(0)

    # Valid inputs?
    apply_dotfiles(input_dotfiles, dry_run=dry_run)
    utils.echo("\n\nDone!\n\n", color=utils.bcolors.BOLD + utils.bcolors.DEBUG)
