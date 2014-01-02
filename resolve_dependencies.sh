#!/usr/bin/env bash

[[ $UID != 0 ]] && { echo "Please run this script as root or use sudo"; exit 1; }

issue_net="/etc/issue"
pkgs='pip install requests docopt'

ostype=$( { 
		grep -iq "ubuntu" $issue_net && echo "ubuntu" || {
		grep -iEq "centos|redhat" $issue_net && echo "redhat";}; 
	   }    || echo "unknown"
	)

ubuntu(){
	apt-get update
	apt-get install python-pip -y
	$pkgs
}

rhel(){
	yum install python-pip
	$pkgs
}

case $ostype in
	ubuntu) ubuntu ;;
	redhat) rhel   ;;
	*) echo "unknown os please do it manually" ;;
esac
