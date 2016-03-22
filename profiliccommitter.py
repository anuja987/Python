
name = raw_input('Enter file name:')
handle=open(name)
counts=dict()
for line in handle :
    words = line.split() 
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    word=words[1]
    if word not in counts:  
            counts[word]= 1  
    else:  
            counts[word] = counts[word] + 1  
     
    bigcount=None
    bigword=None
    for word,count in counts.items():
        if bigcount == None or count > bigcount:
            bigword=word
            bigcount=count
print bigword,bigcount

