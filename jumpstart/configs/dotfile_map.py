# !/usr/bin/env python3

# std imports
import os
import pathlib
from typing import Dict, Optional, Union, Sequence

from jumpstart import DOTFILE_DIR, REPO_DIR
from jumpstart.utils import echo, bcolors

DOTFILE_MAP = {
    'bash/bashrc':                                       '~/.bashrc',
    'bash/bash_aliases':                                 '~/.bash_aliases',
    'bash/bash_functions':                               '~/.bash_functions',
    'bash/inputrc':                                      '~/.inputrc',
    'bash/bash_profile':                                 '~/.bash_profile',

    'debugging/pdbrc':                                   '~/.pdbrc',

    'i3/config':                                         '~/.config/i3/config',

    'i3/scripts/polybar.sh':                             '~/.config/i3/scripts/polybar.sh',
    'i3/scripts/lock.sh':                                '~/.config/i3/scripts/lock.sh',
    'i3/polybar/config.ini':                             '~/.config/polybar/config.ini',
    'i3/polybar/colors.ini':                             '~/.config/polybar/colors.ini',
    'i3/polybar/bars.ini':                               '~/.config/polybar/bars.ini',
    'i3/polybar/modules.ini':                            '~/.config/polybar/modules.ini',
    'i3/polybar/user_modules.ini':                       '~/.config/polybar/user_modules.ini',

    # 'i3/scripts/Lock_icon.png':         'path',
    # 'i3/i3blocks.conf':              'path',
    # 'rofi/config.rasi':              '~/.config/rasi/config.rasi',

    'regolith/i3/config':                                '~/.config/regolith/i3/config',
    'regolith/Xresources':                               '~/.config/regolith/Xresources',

    # 'vim/vimrc':                     '~/.vimrc',
    # 'vim/vimrc.local':               '~/.vimrc.local',
    'git/gitconfig':                                     '~/.config/git/config',

    'ImageMagick/policy.xml':                            '/etc/ImageMagick-6/policy.xml',

    'desktop_launchers/stretchly.desktop':               '~/.local/share/applications/stretchly.desktop',
    'desktop_launchers/neovim.desktop':                  '~/.local/share/applications/neovim.desktop',
    'desktop_launchers/scripts/nvim_desktop_wrapper.py': '/usr/local/bin/nvim_desktop_wrapper.py',

    # 'known_hosts':                   'path',

    # 'termite/config':                'path',
    # 'nvim/local_init.vim':           'path',
    # 'nvim/local_bundles.vim':        'path',

    'sxiv/key-handler':                                  '~/.config/sxiv/exec/key-handler',

    'nvim/init.vim':                                     '~/.config/nvim/init.vim',
    'nvim/coc-settings.json':                            '~/.config/nvim/coc-settings.json',
    'nvim/package-lock.json':                            '~/.config/nvim/package-lock.json',

    'nvim/UltiSnips/python.snippets':                    '~/.config/nvim/UltiSnips/python.snippets',
    'nvim/UltiSnips/markdown.snippets':                  '~/.config/nvim/UltiSnips/markdown.snippets',

    'nvim/after/autocommands.vim':                       '~/.config/nvim/after/autocommands.vim',
    'nvim/after/general-settings.vim':                   '~/.config/nvim/after/general-settings.vim',
    'nvim/after/mappings.vim':                           '~/.config/nvim/after/mappings.vim',
    'nvim/after/visual.vim':                             '~/.config/nvim/after/visual.vim',

    'nvim/after/plugin/plugin-config.vim':               '~/.config/nvim/after/plugin/plugin-config.vim',
    'nvim/after/plugin/plugin-overview.vim':             '~/.config/nvim/after/plugin/plugin-overview.vim',
    'nvim/after/plugin/coc.vim':                         '~/.config/nvim/after/plugin/coc.vim',

    'nvim/after/ftplugin/json.vim':               '~/.config/nvim/after/ftplugin/json.vim',
    'nvim/after/ftplugin/python.vim':             '~/.config/nvim/after/ftplugin/python.vim',
    'nvim/after/ftplugin/html.vim':               '~/.config/nvim/after/ftplugin/html.vim',
    'nvim/after/ftplugin/yaml.vim':               '~/.config/nvim/after/ftplugin/yaml.vim',

    'nvim/after/compiler/cpp.vim':                       '~/.config/nvim/after/compiler/cpp.vim',
    'nvim/after/compiler/dummy.vim':                     '~/.config/nvim/after/compiler/dummy.vim',
    'nvim/after/compiler/tardyscript.vim':               '~/.config/nvim/after/compiler/tardyscript.vim',
    'nvim/after/compiler/tsconfig.vim':                  '~/.config/nvim/after/compiler/tsconfig.vim',
    'nvim/after/compiler/tslint.vim':                    '~/.config/nvim/after/compiler/tslint.vim',
    'nvim/after/compiler/typescript.vim':                '~/.config/nvim/after/compiler/typescript.vim',

    'gtk-2.0/gtkrc-2.0':                                 '~/.gtkrc-2.0',
    'gtk-3.0/gtk.css':                                   '~/.config/gtk-3.0/gtk.css',
    'gtk-3.0/settings.ini':                              '~/.config/gtk-3.0/settings.ini',
    'gtk-4.0/settings.ini':                              '~/.config/gtk-4.0/settings.ini',

    'alacritty/alacritty.yml':                           '~/.config/alacritty/alacritty.yml'

    # 'plantuml_style.iuml': 'path',

    # 'X/Xresources':                  '~/.Xresources',
    # 'X/default_screenlayout.sh':     '~/.screenlayout/default_screenlayout.sh',
    # 'X/xprofile':                    '~/.xprofile',
}


# TODO fcn to substitute home dir!
# def resolve_homedir(homedir: Union[str, pathlib.Path] = None) -> str:
#     if not homedir:
#         return os.path.expanduser('~')
#     elif os.path.isdir(homedir):
#         return str(homedir)
#     elif (pathlib.Path('~') / homedir).is_dir():
#         # Relative dir from the default dir?
#         return str(pathlib.Path('~') / homedir)
#     else:
#         raise OSError(f"Invalid home directory: {homedir}")


def map_dotfiles_to_paths(
        dotfile_map: Dict[str, str] = None,
        dotfile_keys: Sequence[str] = None,
        homedir: Optional[str] = None,
        dotfile_dir: Union[str, pathlib.Path] = DOTFILE_DIR,
) -> Dict[str, pathlib.Path]:
    """
    Returns a mapping between each dotfile in *dotfile_map* and its destination, based on the *homedir*
    """
    if dotfile_map is None:
        dotfile_map = DOTFILE_MAP

    if dotfile_keys:
        echo(["Filtering selected dotfile keys:"] + sorted(dotfile_keys),
             color=bcolors.INFO,
             sep='\n\t> ')
        dotfile_map = {k: v for k, v in dotfile_map.items() if k in dotfile_keys}

    if not dotfile_map:
        echo("No dotfiles to map!", color=bcolors.WARNING, sep='\n\t> ')
        return dict()

    if not isinstance(dotfile_dir, pathlib.Path):
        dotfile_dir = pathlib.Path(dotfile_dir)

    # -------------------------------------------------------------------------- #
    # Clean up the dotfile map
    # -------------------------------------------------------------------------- #
    missing_fs = {k for k in dotfile_map if not (dotfile_dir / k).is_file()}

    if missing_fs:
        echo(["Ignoring dotfile mappings with missing src files:"] + sorted(missing_fs),
             color=bcolors.WARNING,
             sep='\n\t> ')
        dotfile_map = {k: v for k, v in dotfile_map.items()
                       if k not in missing_fs}

    # Better logic
    if not homedir:
        homedir = os.path.expanduser('~')
        echo(f"Expanding '~' to '{homedir}'\n", color=bcolors.INFO)
        dotfile_map = {k: pathlib.Path(v).expanduser().absolute()
                       for k, v in dotfile_map.items()}
    elif os.path.isdir(homedir):
        echo(f"Using input home directory: {homedir}\n")
        dotfile_map = {k: pathlib.Path(v.replace('~', str(homedir))).absolute()
                       for k, v in dotfile_map.items()}
    elif (pathlib.Path('~') / homedir).is_dir():
        homedir = pathlib.Path('~') / homedir
        echo(f"Using input home directory: {homedir}\n")
        dotfile_map = {k: pathlib.Path(v.replace('~', str(homedir))).absolute()
                       for k, v in dotfile_map.items()}
    else:
        raise OSError(f"Invalid home directory: {homedir}")

    # -------------------------------------------------------------------------- #
    # Match them
    # -------------------------------------------------------------------------- #
    repo_files = {str(f.relative_to(dotfile_dir)): f.absolute() for f in dotfile_dir.rglob('*')}

    matched_ks = set(repo_files).intersection(dotfile_map)
    missed_ks = set(repo_files).difference(repo_files)

    if missed_ks:
        echo(["files without mappings:"] + sorted(missed_ks),
             sep='\n\t> ',
             color=bcolors.WARNING,
             )

    bad_map_ks = {k for k in matched_ks if REPO_DIR in dotfile_map[k].parents}

    if bad_map_ks:
        echo(["invalid dest mappings:"] + sorted(bad_map_ks),
             sep='\n\t> ',
             color=bcolors.WARNING,
             )
        matched_ks = matched_ks.difference(bad_map_ks)

    if not matched_ks:
        echo(f"No known dotfiles were found!", color=bcolors.FAIL)
        raise ValueError(f"No matched_ks found!")

    return {dotfile_dir / k: dotfile_map[k] for k in repo_files if k in matched_ks}


def report_dotmap(m: Dict[Union[str, pathlib.Path], Union[str, pathlib.Path]]) -> str:
    report = '\n'.join(['DOTFILES WITH THEIR MAPPINGS'] + [f'{str(k):>50} -> {str(m[k])}' for k in sorted(m)])
    return f"\n{report}\n"


if __name__ == "__main__":
    # # TESTING
    d1 = map_dotfiles_to_paths(homedir=None, dotfile_keys=["poop"])
    # d1 = map_dotfiles_to_paths(homedir=None)
    # d2 = map_dotfiles_to_paths(homedir='/root')
    # d2 = map_dotfiles_to_paths(homedir='/root')
    # report_dotmap(d2)

    print(report_dotmap(DOTFILE_MAP))
