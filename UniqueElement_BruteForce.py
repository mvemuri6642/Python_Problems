def uniqueElementBruteForce(arr):
	unique=[]
	for i in range(len(arr)):
		found=False
		for j in range(len(arr)):
			if(arr[i]==arr[j] and i!=j):
				found=True
				break
		if not found:
			unique.append(arr[i])
	return unique
arr=list(map(int,input().rstrip().split()))
print(uniqueElementBruteForce(arr))