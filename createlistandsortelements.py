fname = raw_input("Enter file name: ")
fh=open(fname)
tmpLst = list()
lst = list()
for line in fh:
    tmpLst = line.split()            #return list of words in the line
    for word in tmpLst:              
        if word not in lst:          #check for duplicate words, append unique words only
            lst.append(word)

lst.sort()
print lst