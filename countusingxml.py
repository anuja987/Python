import urllib
import xml.etree.ElementTree as ET

def readxmldata():
    """
    Reads xml file from the web and calculates 
    the sum of number of 'count' words in the xml file.
        
    Args: None
    Returns: None
    """
    try:
        count=0
        sum=0
        uh=urllib.urlopen('http://python-data.dr-chuck.net/comments_233279.xml')
        data = uh.read()
        print 'Retrieved',len(data),'characters'
        tree = ET.fromstring(data)
        counts = tree.findall('.//count')
        
        for count in counts:
            sum = int(count.text)+ sum
        print len(counts)
        print sum
        
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    readxmldata()
    