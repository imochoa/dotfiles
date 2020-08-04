VER=8.1.1

wget "https://github.com/sharkdp/fd/releases/download/v${VER}/fd-musl_${VER}_amd64.deb" --continue -O /tmp/fd-find.deb
sudo dpkg -i /tmp/fd-find.deb
