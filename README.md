# dotfiles
collection of the setting that I like as well as some scripts to automate the post-install setup process


You can download and run it at the same time by running:

```
(GIT_DL=/tmp/git-$RANDOM; mkdir -p $GIT_DL; cd $GIT_DL; echo $GIT_DL; wget -c https://github.com/imochoa/dotfiles/archive/master.zip -O repo.zip ; unzip repo.zip;cd $(find . -maxdepth 1 -type d -name "dotfiles*" -print -quit); echo "Call script now";./auto-setup.sh; rm -rf $GIT_DL);
```
