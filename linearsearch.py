def linear_search(mylist,item):

    """
    The linear search is used to find an item in a list. The items do not have to be in order. To search for an item, start at the beginning of the list and continue searching until either the end of the list is reached or the item is found.

    The algorithm is as follows (given a list called 'mylist' and looking for an item called 'item'):
    """
    try:
    found=False
    position=0
    while position < len(mylist) and not found:
    	if mylist[position]==item:
            found=True
        position=position+1
    return found
    
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
        
if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    mylist=[2,4,3,6,5,9]
    print linear_search(mylist,2)
    print linear_search(mylist,11)
