#!/usr/bin/env bash

# Look for the dotfiles repository localy and pull it if it's not there
if [ -d "/dotfiles" ];  
then 
  # Control will enter here if /repo exists 
  echo -e "\nThe '/dotfiles/' directory existed! Testing the locally mounted version\n"; 
  source /dotfiles/auto-setup.sh;
else 
  echo -e "\nNo local info. Pulling from github\n";
  source /pull-from-github.sh;
fi;
