import sys

def sortlists():
    """
        Creating a list of words in a file and sorting the list.
    
        Arg: None
        Returns: None
        
    """
    try:
        fh=open('C:\Users\Anuja\projects\python\Introduce_yourself.txt')
        tmpLst = list()
        lst = list()
        for line in fh:
            tmpLst = line.split()            #return list of words in the line
            for word in tmpLst:              
                if word not in lst:          #check for duplicate words, append unique words only
                    lst.append(word)

        lst.sort()
        print lst
    
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    sortlists()
    