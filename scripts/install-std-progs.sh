#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

################################################
PROGRAM="Git";

if [[ "$INSTALL_GIT" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y git;
else   
	echo "Not installing $PROGRAM";
fi;


################################################
PROGRAM="tree";

if [[ "$INSTALL_TREE" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y wget;
else   
	echo "Not installing $PROGRAM";
fi;

################################################
PROGRAM="wget";

if [[ "$INSTALL_WGET" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y wget;
else   
	echo "Not installing $PROGRAM";
fi;

################################################
PROGRAM="FreeCAD"

if [[ "$INSTALL_FREECAD" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y freecad;
else   
	echo "Not installing $PROGRAM";
fi;

################################################
PROGRAM="i3"

if [[ "$INSTALL_I3" ]]; 
then    
	echo "Installing $PROGRAM";
	sudo apt-get install -y i3;
else   
	echo "Not installing $PROGRAM";
fi;

################################################

#############
# cleanup! #
############

#function finish {
#	  # Your cleanup code here
#
#  }
#trap finish EXIT
