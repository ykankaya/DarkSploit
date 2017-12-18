#!/bin/sh
#Termux
echo "installing..."
pkg update
echo "done..."
pkg upgrade
echo "done..."
pkg install git
echo "done..."
pkg install wget
echo "done..."
pkg install python2
echo "done..."
pkg install perl
echo "done..."
pkg install php
echo "done..."
echo "now u u need install the requirements with command \033[32mpip install -r requirements.txt\033[1;37m"
echo "Ok"
