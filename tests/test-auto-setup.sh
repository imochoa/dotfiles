#!/usr/bin/env bash

# Look for the dotfiles repository localy and pull it if it's not there
if [ -d "/dotfiles" ];  
then 
  # Control will enter here if /repo exists 
  echo "existed"!; 
  source /dotfiles/auto-setup.sh;
else 
  echo "not there! Pull from github and run!...";
  source /pull-from-github.sh;
fi;
