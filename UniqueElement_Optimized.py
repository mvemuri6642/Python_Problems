def optimizedUniqueElement(arr):
	unique=[]
	for i in range(len(arr)):
		if(i==0 or arr[i]!=arr[i-1]) and (i==len(arr)-1 or arr[i]!=arr[i+1]):
			unique.append(arr[i])
	return unique

arr=list(map(int,input().rstrip().split()))
arr.sort()
print(optimizedUniqueElement(arr))