#!/usr/bin/env python3

# https://gist.github.com/fmoralesc/bd46e97b39ee284af641

from sys import argv
from subprocess import Popen
from time import time
import dbus

session_bus = dbus.SessionBus()

# launch the terminal server with a custom app-id and window class (so the .desktop file gets associated)
Popen("/usr/lib/gnome-terminal/gnome-terminal-server --app-id org.neovim --class=neovim".split())
# wait until the name is registered
timeout = time() + 1
while not session_bus.name_has_owner('org.neovim') and time() <= timeout:
    pass
# launch nvim in a gnome-terminal instance
if session_bus.name_has_owner('org.neovim'):
    Popen("gnome-terminal --app-id org.neovim -x nvim".split() + argv[1:])
