def diagonalDifference(arr):
	d1=d2=0
	for i in range(0,len(arr)):
		for j in range(0,len(arr)):
			if(i==j):
				d1+=arr[i][j]
			if(i==n-j-1):
				d2+=arr[i][j]
	return abs(d1-d2)
arr=[]
n=int(input())
for _ in range(n):
	arr.append(list(map(int,input().split())))
res=diagonalDifference(arr)
print(res)