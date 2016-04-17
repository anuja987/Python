import urllib
import xml.etree.ElementTree as ET

serviceurl='http://python-data.dr-chuck.net/comments_233279.xml'

count=0
sum=0

url=serviceurl + urllib.urlencode({'sensor':'false'})
print 'Retrieving', url

uh=urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
 
counts = tree.findall('.//count')

for count in counts:
    sum = int(count.text)+ sum
print len(counts)
print sum