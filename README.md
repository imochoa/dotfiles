# dotfiles
collection of the setting that I like as well as some scripts to automate the post-install setup process


You can download and run it at the same time by running:

```
(GIT_DL=/tmp/git-$RANDOM; mkdir -p $GIT_DL; cd $GIT_DL; echo $GIT_DL; wget -c https://github.com/imochoa/dotfiles/archive/master.zip -O repo.zip ; unzip repo.zip ; cd $(find . -maxdepth 1 -type d -name "dotfiles*" -print -quit); echo "Call script now";./auto-setup.sh; rm -rf $GIT_DL);
```


# Testing
TODO -> Not currently working
You can test the output of the setup script by running the following command, substituting "development.sh" with any one of the configs in *configs/*:

```
docker build . --tag dotfile-test --build-arg CONFIG="development.sh"
```

You can test out the new environment by running:
```
docker run --rm -it dotfile-test
```
