import re

x=open('C:\\Users\\Anuja\\Desktop\\Learn\\Course3\\RegularExp\\regex_sum_233277.txt')
hand=x.read()
y=re.findall('[0-9]+',hand)
total=0
for word in y:
    total=total+int(word)
print total
