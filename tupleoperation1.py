import string

def tuples():
    """
    From this file http://www.py4e.com/code3/intro-short.txt, calculate 3 most commonly used words
    
        Arg:  None
        Returns: None

    """
    try:
        fhand = open('C:\\Users\\Anuja\\Desktop\\Python\\Exercise\\intro.txt')
        counts = dict()
        for line in fhand:
            line = line.translate(None, string.punctuation)
            print line
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
        # Sort the dictionary by value
        lst = list()
        for key, val in counts.items():
          lst.append( (val, key) )

        lst.sort(reverse=True)
        for key, val in lst[:3] :
          print key, val


    except:
         exc_type, exc_obj, exc_tb = sys.exc_info()
         print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    tuples()

