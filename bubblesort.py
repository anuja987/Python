def bubble_sort(myList):
    """The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order.
    Each pass through the list places the next largest value in its proper place. In essence, each item bubbles up to the location
    where it belongs."""
    
    moreswaps=True
    
    try:
        
    while moreswaps:
        moreswaps=False
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                moreswaps=True
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp
    return  myList
    
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":   
    """       
    main function, starting point of program.   
    """   
    myList=[32,21,67,90,29,10,34]
    sortedlist= bubble_sort(myList)
    print(sortedlist)
