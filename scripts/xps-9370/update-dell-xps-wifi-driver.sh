#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# Just automates the steps in :
# https://www.dell.com/support/article/ba/en/babsdt1/sln306440/killer-n1535-wireless-firmware-manual-update-guide-for-ubuntu-systems?lang=en
pretty_echo 'Updating the Killer card..QA ';


#TODO  Make sure that sudo lspci | grep –i qca6174 is there...
wget 'https://codeload.github.com/kvalo/ath10k-firmware/zip/master' -O /tmp/ath10k.zip && unzip /tmp/ath10k.zip 



# Remove the previous ver
sudo rm -rf '/lib/firmware/ath10k/QCA6174';

sudo cp -r 'ath10k-firmware-master/QCA6174/' '/lib/firmware/ath10k/';

(cd '/lib/firmware/ath10k/QCA6174/hw3.0/' && sudo mv 'firmware-4.bin_WLAN.RM.2.0-00180-QCARMSWPZ-1' 'firmware-4.bin' )


# TODO disable wifi power saving

# TODO set REGDOMAIN at /etc/default/crda

#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
