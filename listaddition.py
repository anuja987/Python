def listaddition():
    """
       Given 2 lists create 3rd list which will represent addition of first 2 lists.
       for eg. [1,2,3] + [4,7,9] = [6,0,2]
       Extend your program to have lists of different lengths.

        Arg:  None
        Returns: None
    """

    a = [1,9,5,7]
    b = [1,2,1]
    result= []
    i= len(a)-1
    j= len(b)-1
    k = min(i, j)
    d = 0
    try:

        while k >= 0:
            temp = (a[i] + b[j]) + d
            if temp > 9:
                result.append(temp % 10)
                print result
                d = 1
            else:
                d = 0
                result.append(temp)
                print result
            k = k - 1
            i = i - 1
            j = j - 1
        if i == 0:
            result.append(a[0] + d)
        else:
            result.append(b[0] + d)

        result.reverse()
        print result

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)

if __name__ == "__main__":
    """
    main function, starting point of program.
    """
    listaddition()
