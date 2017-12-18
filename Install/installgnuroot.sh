#!/bin/sh
#GNU
echo "installing..."
apt-get install git
echo "done..."
apt-get update
echo "done..."
apt-get upgrade
echo "done..."
apt-get install wget
echo "done..."
apt-get install python2-pip
echo "done..."
apt-get install perl
echo "done..."
apt-get install Build essential
echo "done..."
apt-get install libany-uri-escape-perl
echo "done..."
apt-get install libhtml-html5-entities-perl
echo "done..."
apt-get install libhtml-entities-numbered-perl
echo "done..."
apt-get install libhtml-parser-perl
echo "done..."
apt-get install libwww-perl
echo "done..."
apt-get install php
echo "done..."
echo "now u u need install the requirements with command \033[32mpip install -r requirements.txt\033[1;37m"
echo "Ok"
