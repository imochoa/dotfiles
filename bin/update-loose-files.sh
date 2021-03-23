#!/usr/bin/env bash

# SETUP
BINDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
REPODIR=$(realpath "${BINDIR}/..");
DOTFILEDIR="${REPODIR}/dotfiles";

echo "Cheat autocompletions file...";
wget https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.bash -O "${DOTFILEDIR}/bash/completions/cheat.bash" || notify-send -u "critical"  "FAILED" && true;