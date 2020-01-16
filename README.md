# dotfiles
collection of the setting that I like as well as some scripts to automate the post-install setup process

You can download and run it at the same time by copying the command in `pull-from-github.sh` 

TODO Add symlinks everywhere!

# Components
Here is what the repo structure looks like, along with short explanations:

```
dotfiles
├── auto-setup.sh # starts everything
├── configs
│   └── These files will tell the *auto-setup.sh* script what to set up
├── Dockerfile
├── dotfiles
│   └── The dotfiles to use (e.g. for bash, vim, i3 etc.)
├── private
│   └── similar to "dotfiles", but these config files should not be shared! (e.g. private/public ssh keys)
├── fonts
│   ├── Some useful fonts
│   └── update-fonts.sh # Look online for new versions of these fonts
├── LICENSE
├── pull-from-github.sh
├── README.md
├── scripts
│   └── these scripts are the ones that do the actual work
├── src
│   └── a compilation of some nice-to-have functions
├── tests
│   └── for debugging 
└── update.sh # Looks for updates (e.g. runs the update-fonts.sh script) 
```
# Config file lookup
program  |  config
---      |  ---
termite  |  ~/.config/gtk-3.0/gtk.css

# Testing
Build the base docker image with:
```
docker build . --tag dotfile-test
```

Afterwards, you can test the output of the `auto-setup.sh` script by running the following command (substituting "development.sh" with any one of the configs in *configs/*: 
```
docker run --rm -it --env CONFIG_TO_TEST=development.sh dotfile-test
```

For development, it's easiert to copy over the local files instead of pulling them from github every time. You can do that by mounting the repo like so:
```
docker run --rm -it --env CONFIG_TO_TEST=development.sh --mount type=bind,source=$(pwd),destination=/dotfiles/,readonly dotfile-test
```

You can also just start an interactive bash shell directly:
```
docker run --rm -it --mount type=bind,source=$(pwd),destination=/dotfiles/,readonly dotfile-test /bin/bash
```
