#!/usr/bin/env bash

# This script is there to get and save the absolute paths to all useful directories and 
# avoid having to work with relative paths constantly
double_check_path () {
    if [ ! -d "${2:-/}" ]; then
        echo "WARNING: Could not find the ${1} directory at ${2}!";
    else
        export ${1}=${2};
    fi;

}


# Starting points
double_check_path SRC_DIR "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )";
double_check_path REPO_DIR "${SRC_DIR}/..";
double_check_path DOTFILE_DIR "${REPO_DIR}/dotfiles";
double_check_path FONT_DIR "${REPO_DIR}/fonts";


# Configuration directories
double_check_path VIM_CONF_DIR "${DOTFILE_DIR}/vim";
double_check_path BASH_CONF_DIR "${DOTFILE_DIR}/bash";
double_check_path I3_CONF_DIR "${DOTFILE_DIR}/i3";

