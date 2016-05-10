import urllib
import json
import sys

def parsingjsondata():
    """
        In this program the parsingjsondata function will read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data.Also computes the sum of the numbers in the file
        
        Arg:  None
        Returns: None
        
    """
    try:
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

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """   
    parsingjsondata()

