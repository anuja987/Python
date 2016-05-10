# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import sys
import urllib
from BeautifulSoup import *

def parsinghtmldata():
    """
        The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
        scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat 
        the process a number of times and reports the last name it finds.
       
        Arg:  None
        Returns: None
        
    """
    try:
        html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Niome.html')
        repeat_count=7
        while (repeat_count>0):
            soup = BeautifulSoup(html)
            tags = soup('a')
            html = urllib.urlopen(tags[17].get('href',None)).read()
            repeat_count-=1

        print tags[17].string

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """   
    parsinghtmldata()