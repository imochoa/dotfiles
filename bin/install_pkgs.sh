#!/usr/bin/env bash

# Wrapper so that you don't have to worry about the PYTHONPATH while calling the scripts
BINDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
REPODIR=$(realpath "${BINDIR}/..");
PYTHONPATH="${REPODIR}" python3 ${REPODIR}/jumpstart/scripts/installer.py ${@}