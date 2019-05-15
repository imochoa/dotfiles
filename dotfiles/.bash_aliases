#!/usr/bin/env bash

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

goinside(){
    docker exec -it $1 bash -c "stty cols $COLUMNS rows $LINES && bash";
}
_goinside(){
    COMPREPLY=( $(docker ps --format "{{.Names}}" -f name=$2) );
}
complete -F _goinside goinside;
export -f goinside;
