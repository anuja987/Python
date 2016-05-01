def maxprofit(arr):
    profit=0
    buy=0
    min=10001
    for i in range(0,len(arr)):
    	if (arr[i] < min):
	    min=arr[i]
	    buy=i
    for i in range(0,len(arr)):
    	if ((arr[i] -arr[buy]) > profit and buy < i):
    	    profit = max (arr[i] - arr[buy], profit)
    print profit


if __name__=="__main__":
    arr1=[1,2,3,7,2]
    maxprofit(arr1)
    arr2=[7,1,2,3,2]
    maxprofit(arr2)