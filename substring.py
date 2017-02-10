def find_substring():
    '''
    This program is written using for loop to find out if the given substring is part of the list of strings provided in the program.
    '''
    try:
        
    small_str = "how"
    list_str = ["abc","hi how are you","fantastic, how about you?"]
    for value in list_str:
        if small_str in value:
            print 'string is substring of s'
        else:
            print 'string is not substring of s'
    return
    
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
        
if __name__=="__main__":
    """
        main function, starting point of program.
    """
    print(find_substring())
