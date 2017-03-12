import string
fhand = open('C:\\Users\\Anuja\\Desktop\\Python\\Exercise\\intro.txt')
counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
    print line
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# Sort the dictionary by value
lst = list()
for key, val in counts.items():
  lst.append( (val, key) )

lst.sort(reverse=True)
for key, val in lst[:3] :
  print key, val
