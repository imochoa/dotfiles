# dotfiles
collection of the setting that I like as well as some scripts to automate the post-install setup process


You can download and run it at the same time by copying the command in `pull-from-github.sh` 

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
