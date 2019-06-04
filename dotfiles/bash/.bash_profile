#!/usr/bin/env bash

export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/
# Otherwise the set wallpaper command (gsettings) fails, see:
# https://stackoverflow.com/questions/44934641/glib-gio-message-using-the-memory-gsettings-backend-your-settings-will-not-b
# https://github.com/conda-forge/glib-feedstock/issues/19

# For going inside running docker containers
goinside(){
    docker exec -it $1 bash -c "stty cols $COLUMNS rows $LINES && bash";
}
_goinside(){
    COMPREPLY=( $(docker ps --format "{{.Names}}" -f name=$2) );
}
complete -F _goinside goinside;
export -f goinside;
