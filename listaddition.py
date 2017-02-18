a = [1,9,5,7]
b = [1,2,1]
result= []
i= len(a)-1
j= len(b)-1
k = min(i, j)
d = 0
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
