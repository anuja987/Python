# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib # read html data to retrieve it into the program
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_233282.html').read()

soup = BeautifulSoup(html) #parsed html data
count=0
t=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    print tag
    for line in tag:
        count=count+1
        t=t+int(line)
print 'count ',count
print 'sum ',t
    