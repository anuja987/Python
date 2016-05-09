import sys

def findrange():
    """
       Find the range of user inputs given by user
       
        Arg: None
        Returns: None
        
    """
    try:

        s= raw_input('Enter Score between 0.0 and 1.0: ')
        score=float(s)
        if score>=0.9:
            print 'A'
        elif score>=0.8:
            print 'B'
        elif score>=0.7:
            print 'C'
        elif score>=0.6:
            print 'D'
        elif score<0.6:
           print 'F' 
        else: 
            print'Score is out of range'
            quit()
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    findrange()
    