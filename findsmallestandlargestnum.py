largest = -1
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        inp=int(num)
        if inp > largest:
           largest=inp
        if smallest is None:
            smallest=inp
        elif inp < smallest:
                smallest=inp
    except:
        print "Invalid input"
        continue
        
print "Maximum is",largest
print "Minimum is",smallest