import sys

def findsmallestandlargestnumber():
    """
       Finds smallest and largest number out of the numbers entered by user
       
        Arg: 
        largest = -1
        smallest = None
      
      Returns: None
        
    """
    largest = -1
    smallest = None
    n=5
    try:
        while (n>0):
            n=n-1
            num = raw_input("Enter a number: ")
            inp=int(num)
            if inp > largest:
                largest=inp
            if smallest is None:
                smallest=inp
            elif inp < smallest:
                smallest=inp
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
        
    print "Maximum is",largest
    print "Minimum is",smallest
      
if __name__ == "__main__":
    """
        main function, starting point of program. User will be prompted to 
        enter numbers 5 times.
    """
    findsmallestandlargestnumber()