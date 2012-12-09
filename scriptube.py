#################################################
#
#   author: radha krishna
#   name  : scriptube.py
#   desc  : give the url and it will open ur
#	    browser and plays it in full screen
#	note: set the browser path in the script
#	  once and use it! enjoy!!
# eg.: python scriptube.py <url>
#################################################

#!/bin/python

import re
import sys
import urllib2
import subprocess

browser_path = "/Applications/Safari.app/Contents/MacOS/Safari"

def get_code(url):
    response = urllib2.urlopen(url)
    page_source = response.read()
    #print page_source
    regexp = r"http:\/\/www.youtube.com\/v\/[a-zA-Z0-9_]+\?"
    #file = open("text.txt",'r')
    #for line in page_source:
    match = re.findall(regexp,page_source)
    tmp=[]
    if len(match) != 0:
        #print match
        seen = set()
        for i in match:
            if i not in seen:
                seen.add(i)
                regcode = r"[a-zA-Z0-9_]+\?"
                matchcode = re.findall(regcode,i)
                if len(matchcode) != 0:
                    print matchcode[0]
                    form_url(matchcode[0])


def form_url(string):
    removedques = re.sub(r'\?', '', string)
    final_url="http://youtube.googleapis.com/v/"+removedques
    print final_url
    open_process(final_url)

def open_process(url):
    process_one = subprocess.Popen([browser_path,url])
    print process_one.pid

if len(sys.argv) < 2:
	sys.exit("Usage :: python scriptube.py <url> \n python scriptube.py http://www.youtube.com/watch?v=1ufQ9OUosKE&feature=g-vrec")
else:
    print sys.argv
    get_code(sys.argv[1])
