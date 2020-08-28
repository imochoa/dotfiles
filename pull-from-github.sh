#!/usr/bin/env bash

GIT_URL=https://github.com/imochoa/dotfiles/archive/master.zip
GIT_TMP_DIR=/tmp/gitpull-$RANDOM;

# TODO use tempdir!
# TEMPDIR=$(mktemp -d -t nordic-XXXXXXXXXX)

mkdir -p ${GIT_TMP_DIR};
cd ${GIT_TMP_DIR};
echo ${GIT_TMP_DIR};

sudo apt-get update && sudo apt-get install -y wget zip unzip;

wget -c ${GIT_URL} -O repo.zip; unzip repo.zip;
cd $(find . -maxdepth 1 -type d -name "dotfiles*" -print -quit);

# Since the download finished successfully, start the setup process
source auto-setup.sh
