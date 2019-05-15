#!/usr/bin/env bash


export PRETTY_ECHO_SEP='=================================================================================';
pretty_echo () { 
	
	echo -e "\n${PRETTY_ECHO_SEP}\n${1}\n${PRETTY_ECHO_SEP}\n"; 

}



install_envvar () {

	VAL=$(echo $echo ${!1}); 
	
	if [[ "${VAL:-false}" == true ]] 
	then 
		pretty_echo "Flag set to true: [$1] > running [$2]"; 
		eval $2;
	else
		pretty_echo "Flag not true: [$1]"; 
	fi
}

