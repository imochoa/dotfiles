# !/usr/bin/env python3

DOTFILE_MAP = {
    'bash/bashrc':                   '~/.bashrc',
    'bash/bash_aliases':             '~/.bash_aliases',
    'bash/bash_functions':           '~/.bash_functions',
    'bash/inputrc':                  '~/.inputrc',
    'bash/bash_profile':             '~/.bash_profile',

    'debugging/pdbrc': '~/.pdbrc',

    'i3/config':                  '~/.config/i3/config',

    'i3/scripts/polybar.sh':            '~/.config/i3/scripts/polybar.sh',
    'i3/scripts/lock.sh':               '~/.config/i3/scripts/lock.sh',
    'i3/polybar/config.ini':            '~/.config/polybar/config.ini',
    'i3/polybar/colors.ini':            '~/.config/polybar/colors.ini',
    'i3/polybar/bars.ini':              '~/.config/polybar/bars.ini',
    'i3/polybar/modules.ini':           '~/.config/polybar/modules.ini',
    'i3/polybar/user_modules.ini':      '~/.config/polybar/user_modules.ini',

    # 'i3/scripts/Lock_icon.png':         'path',
    # 'i3/i3blocks.conf':              'path',
    # 'rofi/config.rasi':              '~/.config/rasi/config.rasi',

    # 'vim/vimrc':                     '~/.vimrc',
    # 'vim/vimrc.local':               '~/.vimrc.local',

    'ImageMagick/policy.xml':           '/etc/ImageMagick-6/policy.xml',

    'desktop_launchers/stretchly.desktop': '~/.local/share/applications/stretchly.desktop',

    # 'known_hosts':                   'path',

    # 'termite/config':                'path',
    # 'nvim/local_init.vim':           'path',
    # 'nvim/local_bundles.vim':        'path',

    'nvim/init.vim':                    '~/.config/nvim/init.vim',
    'nvim/coc-settings.json':           '~/.config/nvim/coc-settings.json',
    'nvim/package-lock.json':           '~/.config/nvim/package-lock.json',
    'nvim/after/autocommands.vim':           '~/.config/nvim/after/autocommands.vim',
    'nvim/after/general-settings.vim':           '~/.config/nvim/after/general-settings.vim',
    'nvim/after/mappings.vim':           '~/.config/nvim/after/mappings.vim',
    'nvim/after/visual.vim':           '~/.config/nvim/after/visual.vim',

    'nvim/after/plugin/plugin-config.vim':           '~/.config/nvim/after/plugin/plugin-config.vim',
    'nvim/after/plugin/plugin-overview.vim':           '~/.config/nvim/after/plugin/plugin-overview.vim',
    'nvim/after/plugin/coc.vim':           '~/.config/nvim/after/plugin/coc.vim',

    'nvim/after/compiler/cpp.vim':  '~/.config/nvim/after/compiler/cpp.vim',
    'nvim/after/compiler/dummy.vim':  '~/.config/nvim/after/compiler/dummy.vim',
    'nvim/after/compiler/tardyscript.vim':  '~/.config/nvim/after/compiler/tardyscript.vim',
    'nvim/after/compiler/tsconfig.vim':  '~/.config/nvim/after/compiler/tsconfig.vim',
    'nvim/after/compiler/tslint.vim':  '~/.config/nvim/after/compiler/tslint.vim',
    'nvim/after/compiler/typescript.vim':  '~/.config/nvim/after/compiler/typescript.vim',

    'gtk-2.0/gtkrc-2.0':             '~/.gtkrc-2.0',
    'gtk-3.0/gtk.css':               '~/.config/gtk-3.0/gtk.css',
    'gtk-3.0/settings.ini':          '~/.config/gtk-3.0/settings.ini',
    'gtk-4.0/settings.ini':          '~/.config/gtk-4.0/settings.ini',

    # 'plantuml_style.iuml': 'path',

    # 'X/Xresources':                  '~/.Xresources',
    # 'X/default_screenlayout.sh':     '~/.screenlayout/default_screenlayout.sh',
    # 'X/xprofile':                    '~/.xprofile',
}


if __name__ == "__main__":
    pass
