
def multiplication(arr1):
    total=1
    temp=[0,0,0,0]
    for i in range(0, (len(arr1))):
       # if arr1[i] != 0:	
	    total=total*arr1[i]
           
   
   
    for i in range(0, (len(arr1))):
       # if arr1[i] == 0:
	    temp[i]= total//arr1[i]
       # else:
          #  temp[i]=0
    print "arr2=",temp
    
if __name__ == "__main__":
    arr1=[1,2,5,7]
    multiplication(arr1) 	

