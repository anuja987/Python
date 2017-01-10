def bubble_sort(myList):
    """The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order.
    Each pass through the list places the next largest value in its proper place. In essence, each item bubbles up to the location
    where it belongs."""
    moreswaps=True
    while moreswaps:
        moreswaps=False
        for i in range(len(myList)-1):
            if myList[i] > myList[i+1]:
                moreswaps=True
                temp = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = temp
    return  myList

myList=[32,21,67,90,29,10,34]
sortedlist= bubble_sort(myList)
print(sortedlist)
