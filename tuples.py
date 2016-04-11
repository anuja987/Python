name = raw_input("Enter file:")
handle = open(name)
counts=dict()
for line in handle:
    words=line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    words= words[5]
    hour=words[:2]
    if hour not in counts:
        counts[hour] =1
    else:
        counts[hour] = counts[hour] +1
lst=list()
for k,v in counts.items():
    lst.append((k,v))
    lst.sort()
for k,v in lst[:12]:
    print k,v