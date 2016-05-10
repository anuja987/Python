# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import sys
import urllib # read html data to retrieve it into the program
from BeautifulSoup import *

def parsinghtmldata():
    """
        The program will use urllib to read the HTML from the data files below, 
        counts the number of span tags and calculates the sum of the numbers in the span tag.
       
        Arg:  None
        Returns: None
        
    """
    try:
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
            
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """   
    parsinghtmldata()