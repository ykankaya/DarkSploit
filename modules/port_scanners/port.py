#!/usr/bin/env python
# -*- coding: utf-8 -*-
#CODED BY DERAY
#Iseng ngoding aja ea :v nyontek dikit dah :v
from threading import Thread
import socket
import sys
import time
# Set Color
R = '\033[31m' # Red
N = '\033[1;37m' # White
B = '\033[1;34m' #Blue
print ""+N+""+R+"set target for example "+N+"=>"+R+" target.com"
host = raw_input(''+N+'DrXp > : ')
print ""+R+"target "+N+"=> "+R+"",host
print ""+R+"enter number scan"
from_port = input(''+N+'DrXp > ')
print ""+R+"enter finish scan"
to_port = input(''+N+'DrXp > ')   
re = raw_input("DrXp > ")
if re == "run":
	print ""+B+"[*]"+N+" Starting attacks..."
counting_open = []
counting_close = []
threads = []

def scan(port):
	s = socket.socket()
	result = s.connect_ex((host,port))
	print(' [OK] > '+(str(port)))      
	if result == 0:
		counting_open.append(port)
		#print((str(port))+' -> open') 
		s.close()
	else:
		counting_close.append(port)
		#print((str(port))+' -> close') 
		s.close()

for i in range(from_port, to_port+1):
	t = Thread(target=scan, args=(i,))
	threads.append(t)
	t.start()

[x.join() for x in threads]

print(counting_open)
