import sys

def averagenumbersinfile(num,count):
    """
        Computes Average of given numbers in a file. Assumes 
        
        Args: 
            num: numbers in a file
            count: counts the occurance of numbers in a file
            
        Returns:
            Positive float value of Average.
    """
   
    running_total=  (float(num)+float(line[20:28])) / count 
    return running_total

if __name__ == "__main__":
    """
        main function, starting point of program. User will be prompted to 
        enter name of the file.
    """
    try:
        fname = open('C:\Users\Anuja\projects\python\mbox-short.txt')
        count= 0
        num=0
        running_total= 0
        for line in fname:
            if line.startswith("X-DSPAM-Confidence:") : 
                count=count+1
                running_total= averagenumbersinfile(num,count)
                print 'Average spam confidence:',running_total
        
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)