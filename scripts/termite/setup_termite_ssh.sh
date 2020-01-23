# https://github.com/thestinger/termite/issues/229

TMP=/tmp


echo -e "What's the SSH address to set up?  [username@your.server.com]";
read SSH_URI

echo -e "\n\nGenerating termite.terminfo...";
infocmp > ${TMP}/termite.terminfo;

echo -e "\n\nMoving it to the SSH server...";
scp ${TMP}/termite.terminfo ${SSH_URI}:termite.terminfo;

echo -e "\n\nSetting termite up";
ssh -t ${SSH_URI} 'tic -x termite.terminfo';

echo -e "\n\nCleaning up...";
rm ${TMP}/termite.terminfo;
ssh -t ${SSH_URI} 'rm termite.terminfo';


