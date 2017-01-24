def binary_search(mylist, item):
    """
    The binary search is used to find an item in an ORDERED list.

    For example, we want to find a number in the list: 1, 2, 5, 7, 12, 14, 21, 28, 31, 36
    To search for an item, look in the middle of the list and see if the number you want is in the middle, above the middle or below the middle. If it is in the middle, you have found the item. If it is higher than the middle value, then adjust the bottom of the list so that you search in a smaller list starting one above the middle of the list. If the number is lower than the middle value, then adjust the top of the list so that you search in a smaller list which has its highest position one less than the middle position.

    The algorithm is as follows (given a list called 'List' and looking for an item called 'item'):
    """
    first=0
    last=len(mylist)-1
    found=False
    
    try:
        
    while(first<=last and not found):
        mid= (first+last)//2
        if mylist[mid] == item:
            found= True
        elif item < mylist[mid]:
            last= mid-1
        else:
            first= mid+1
    return found

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    print binary_search([3,4,5,6,7],4)
    print binary_search([5,6,7,8,9],1)
    print binary_search([5,6,7,8,9],10)
