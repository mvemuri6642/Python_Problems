def compareTriplets(a,b):
	alice=bob=0
	for i in range(len(a)):
		if(a[i]>b[i]):
			alice+=1
		elif(a[i]<b[i]):
			bob+=1
		else:
			pass
	return(alice,bob)
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=(compareTriplets(a,b))
print(' '.join(map(str,res)))
