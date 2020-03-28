def aVeryBigSum(ar):
	sum=0
	for i in range(len(ar)):
		sum+=ar[i]
	return sum
n=int(input())
ar=list(map(int,input().rstrip().split()))
print(aVeryBigSum(ar))