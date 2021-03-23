#!/usr/bin/python3

# std imports
import argparse
import sys

from jumpstart.utils import get_release_tags

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Return the latest version of a package"
    )

    parser.add_argument(
        "git_url",
        type=str,
        help=(
            "Which git repo's version to get "
            "(e.g. https://github.com/user/repo, github.com/user/repo, user/repo )"
        ),
    )

    args = parser.parse_args()
    [ver] = get_release_tags([args.git_url])
    sys.stdout.write(ver + "\n")
