#!/bin/bash

# SETUP
BINDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
REPODIR=$(realpath "${BINDIR}/..");
DOTFILEDIR="${REPODIR}/dotfiles";


FILE="$(find ${DOTFILEDIR} -type f -iname 'cheat.bash')";
usr/bin/wget https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.bash \
-O "${FILE}" || notify-send -u "critical"  "Cheat autocompletion FAILED" && true;


FILE="$(find ${DOTFILEDIR} -type f -iname 'nvim_desktop_wrapper.py')";
wget https://raw.githubusercontent.com/fmoralesc/neovim-gnome-terminal-wrapper/master/nvim-wrapper \
-O "${FILE}" || notify-send -u "critical"  "neovim wrapper FAILED" && true;