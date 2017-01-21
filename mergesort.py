def mergeSort(nlist):  
    """
    We now turn our attention to using a divide and conquer strategy as a way to improve the performance of sorting algorithms. The first algorithm we will study is the merge sort. Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list. Figure 10 shows our familiar example list as it is being split by mergeSort. Figure 11 shows the simple lists, now sorted, as they are merged back together.
    """
    print("Splitting ",nlist)  
    if len(nlist)>1:  
        mid = len(nlist)//2  
        lefthalf = nlist[:mid]  
        righthalf = nlist[mid:]  
        
        mergeSort(lefthalf)  
        mergeSort(righthalf)  
        i=j=k=0    
        
        try:
            
        while i < len(lefthalf) and j < len(righthalf):  
            if lefthalf[i] < righthalf[j]:  
                nlist[k]=lefthalf[i]  
                i=i+1  
            else:  
                nlist[k]=righthalf[j]  
                j=j+1  
            k=k+1  

        while i < len(lefthalf):  
            nlist[k]=lefthalf[i]  
            i=i+1  
            k=k+1  

        while j < len(righthalf):  
            nlist[k]=righthalf[j]  
            j=j+1  
            k=k+1  
    print("Merging ",nlist)
    
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

  
nlist = [14,46,43,27,57,41,45,21,70]  
mergeSort(nlist)  
print(nlist) 
