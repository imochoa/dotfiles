#!/bin/bash

# This installs alacritty terminal on ubuntu (https://github.com/jwilm/alacritty)
# You have to have rust/cargo installed for this to work

# Cargo:
# Install rust might ask for confirmation... is that ok?
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

~/.cargo/bin/rustup override set stable
~/.cargo/bin/rustup update stable

# curl https://sh.rustup.rs -sSf | sh

# Install cargo
sudo apt install -y cargo


# Install required tools
sudo apt-get install -y cmake libfreetype6-dev libfontconfig1-dev xclip pkg-config libxcb-xfixes0-dev python3

# Download, compile and install Alacritty
sudo git clone https://github.com/jwilm/alacritty /opt/alacritty
sudo chown -R $USER:$USER /opt/alacritty 
cd /opt/alacritty

~/.cargo/bin/cargo build --release
# ~/.cargo/bin/cargo install

# Add Man-Page entries
sudo mkdir -p /usr/local/share/man/man1
gzip -c extra/alacritty.man | sudo tee /usr/local/share/man/man1/alacritty.1.gz > /dev/null

# Add shell completion for bash and zsh
mkdir -p ~/.bash_completion
cp extra/completions/alacritty.bash ~/.bash_completion/alacritty
echo "source ~/.bash_completion/alacritty" >> ~/.bashrc
# sudo cp alacritty-completions.zsh /usr/share/zsh/functions/Completion/X/_alacritty

# Copy default config into home dir
mkdir -p ~/.config/alacritty
cp alacritty.yml ~/.config/alacritty/alacritty.yml

# Create desktop file
cp extra/linux/Alacritty.desktop ~/.local/share/applications/

# Copy binary to path
sudo cp target/release/alacritty /usr/local/bin

# Use Alacritty as default terminal (Ctrl + Alt + T)
gsettings set org.gnome.desktop.default-applications.terminal exec 'alacritty'

# Remove temporary dir
cd ..
rm -r alacritty

