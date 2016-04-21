import urllib
import json

serviceurl='http://python-data.dr-chuck.net/comments_233283.json'

count=0
sum=0

url=serviceurl + urllib.urlencode({'sensor':'false'})
print 'Retrieving ', url

uh=urllib.urlopen(url)
data = uh.read()
print 'Retrieved ',len(data),' characters'
info = json.loads(data)

for i in range(0,len(info["comments"])):
    count=info["comments"][i]["count"]
    sum = sum + int(count)
print 'count:',len(info["comments"])
print 'sum=',sum



