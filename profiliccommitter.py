import sys

def profiliccommitter():
    """
    This program reads through the mbox-short.txt and figure out who has the sent 
    the greatest number of mail messages. The program looks for 'From ' lines and 
    takes the second word of those lines as the person who sent the mail. 
    The program creates a Python dictionary that maps the sender's mail address 
    to a count of the number of times they appear in the file. After the dictionary
    is produced, the program reads through the dictionary using a maximum loop to 
    find the most prolific committer.

        Arg: None
        Returns: None
        
    """
    try:
        handle = open('C:\Users\Anuja\projects\python\mbox-short.txt')
        counts=dict()
        for line in handle :
            words = line.split() 
            if len(words) == 0 : continue
            if words[0] != 'From' : continue
            word=words[1]
            if word not in counts:  
                    counts[word]= 1  
            else:  
                    counts[word] = counts[word] + 1  
             
            bigcount=None
            bigword=None
            for word,count in counts.items():
                if bigcount == None or count > bigcount:
                    bigword=word
                    bigcount=count
        print bigword,

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    profiliccommitter()
