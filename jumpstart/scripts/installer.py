#!/usr/bin/python3

# std imports
import argparse
import sys

# local imports
from jumpstart.utils import (
    bcolors,
    echo,
    run_shell_str,
)
from jumpstart.installs import build_pkg_maps

if __name__ == "__main__":
    full_install_map, full_remove_map = build_pkg_maps()
    possible_pkg_keys = set(full_install_map.keys())

    possible_pkg_report = '\n\t> '.join(["Possible keys:"] + sorted(possible_pkg_keys))
    parser = argparse.ArgumentParser(description=f'Choose what packages to install.')

    parser.add_argument("pkgs",
                        type=str,
                        nargs='*',
                        help=("Which packages to install, separated by spaces (e.g. 'ssh xclip sxiv')."
                              "Run the command without any inputs to see all possibilities, or with 'all' to install "
                              "everything.")
                        )

    parser.add_argument('-d', '--dry',
                        action='store_true',
                        help="For debugging. When set, the script won't actually install anything, just report back")

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help="More output")

    parser.add_argument('-y', '--yes',
                        action='store_true',
                        help="Don't ask for confirmation")

    args = parser.parse_args()
    pkgs = args.pkgs
    args.dry = True  # TODO DEBUG MODE

    if not pkgs:
        echo(["No inputs given, you can choose from these possible keys:"] + sorted(possible_pkg_keys),
             color=bcolors.INFO,
             sep='\n\t> ')
        sys.exit(0)

    if len(pkgs) == 1 and pkgs[0].lower() == 'all':
        echo("Warning, no pkgs specified... Install EVERYTHING?", color=bcolors.WARNING)
        confirmation = input('[Y]es/[N]o')
        if confirmation.upper()[:1] == 'Y':
            pkgs = possible_pkg_keys
        elif confirmation.upper()[:1] == 'N':
            echo("OK, stopping...", color=bcolors.WARNING)
            sys.exit(0)
        else:
            echo(f"Unknown selection: {confirmation}", color=bcolors.WARNING)
            sys.exit(1)

    pkgs = set(pkgs)
    invalid_keys = {k for k in pkgs if k not in possible_pkg_keys}

    if invalid_keys:
        echo(["Removing invalid install keys:"] + sorted(invalid_keys),
             color=bcolors.WARNING,
             sep='\n\t> ')
        pkgs = pkgs.difference(invalid_keys)

    echo('\n\t> '.join(["\n\nPreparing to install:"] + sorted(pkgs)) + '\n\n', color=bcolors.BOLD + bcolors.INFO)

    if not args.yes:
        confirmation = input('Is that correct?\n[Y]es/[N]o')
        if confirmation.upper()[:1] == 'Y':
            echo("OK!", color=bcolors.INFO)
            pkgs = possible_pkg_keys
        elif confirmation.upper()[:1] == 'N':
            echo("OK, stopping...", color=bcolors.WARNING)
            sys.exit(0)
        else:
            echo(f"Unknown selection: {confirmation}", color=bcolors.WARNING)
            sys.exit(1)

    total = len(pkgs)
    failed_ks = []
    for idx, k in enumerate(pkgs, start=1):

        echo(f"\n\t[{idx:>4}/{total}]: {k}\n\n", color=bcolors.INFO)

        if run_shell_str(
                shell_str=full_install_map[k],
                dry_run=args.dry,
                verbose=args.verbose,
        ):
            echo(f"\n\t\t[OK!] [{k}]\n\n", color=bcolors.INFO)
        else:
            failed_ks.append(k)
            echo(f"\n\t\t[FAILED!] [{k}]\n", color=bcolors.FAILED)

    if failed_ks:
        echo([f"There were {len(failed_ks)} failed installs:"] + sorted(failed_ks),
             color=bcolors.FAILED,
             sep='\n\t> ')

    echo("\n\nDone!\n\n", color=bcolors.BOLD + bcolors.INFO)
