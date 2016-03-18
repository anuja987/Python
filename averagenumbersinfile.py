fname = raw_input("Enter file name: ")
count= 0
num=0
running_total= 0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
       count=count+1
       num=float(num)+float(line[20:28])
       running_total= num / count 
       continue
print 'Average spam confidence:',running_total