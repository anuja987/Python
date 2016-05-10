import sys

def tuples():
    """
    This program reads through the mbox-short.txt and finds out the distribution by hour of the day
    for each of the messages.The hours can be pulled out from the 'From ' line by finding the time 
    and then splitting the string a second time using a colon.
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    Once counts are accumulated for each hour, counts are printed out, sorted by hour as shown below.

    Desired Output
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1

        Arg:  None
        Returns: None
        
    """
    try:
        handle = open('C:\Users\Anuja\projects\python\mbox-short.txt')
        counts=dict()
        for line in handle:
            words=line.split()
            if len(words) == 0 : continue
            if words[0] != 'From' : continue
            words=words[5]
            hour=words[:2]
            if hour not in counts:
                counts[hour] =1
            else:
                counts[hour] = counts[hour] +1
        lst=list()
        for k,v in counts.items():
            lst.append((k,v))
            lst.sort()
        for k,v in lst[:12]:
            print k,v
            
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    tuples()