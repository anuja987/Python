# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Niome.html').read()
repeat_count=7
while (repeat_count>0):
    soup = BeautifulSoup(html)
    tags = soup('a')
    html = urllib.urlopen(tags[17].get('href',None)).read()
    repeat_count-=1

print tags[17].string
