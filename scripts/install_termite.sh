# https://computingforgeeks.com/install-termite-terminal-on-ubuntu-18-04-ubuntu-16-04-lts/
# Build and install VTE
# Build and install TERMITE
TMP=/tmp
( sudo apt-get update \
&& sudo apt-get install -y build-essential \
&& sudo apt-get install -y git g++ libgtk-3-dev gtk-doc-tools gnutls-bin valac intltool libpcre2-dev libglib3.0-cil-dev libgnutls28-dev libgirepository1.0-dev libxml2-utils gperf \
&& cd ${TMP} \
&& git clone https://github.com/thestinger/vte-ng.git \
&& echo export LIBRARY_PATH="/usr/include/gtk-3.0:$LIBRARY_PATH" \
&& cd vte-ng \
&& ./autogen.sh \
&& make \
&& sudo make install \
&& cd ${TMP} \
&& git clone --recursive https://github.com/thestinger/termite.git \
&& cd termite \
&& make \
&& sudo make install \
&& sudo ldconfig \
&& sudo mkdir -p /lib/terminfo/x \
&& sudo ln -s /usr/local/share/terminfo/x/xterm-termite /lib/terminfo/x/xterm-termite )

# Termite style
(cd ${TMP} \
&& git clone https://github.com/adi1090x/termite-style.git \
&& cd termite-style \
&& chmod +x setup \
&& ./setup
)


# # Set it as the default terminal:
# sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator /usr/local/bin/termite 60
