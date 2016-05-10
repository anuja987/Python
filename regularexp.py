import re
import sys

def regularexp():
    """
    This program reads through and parses a file with text and numbers. 
    To extract all the numbers in the file and compute the sum of the numbers.

        Arg:  
        Total= 0
        Returns: None
        
    """
    try:
        x=open('C:\\Users\\Anuja\\Desktop\\Learn\\Course3\\RegularExp\\regex_sum_233277.txt')
        hand=x.read()
        y=re.findall('[0-9]+',hand)
        total=0
        for word in y:
            total=total+int(word)
        print total
    
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    regularexp()