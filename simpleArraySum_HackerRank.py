def simpleArraySum(ar):
	sum=0
	for i in range(len(ar)):
		sum+=ar[i]
	return sum
n=int(input().strip())
ar=list(map(int,input().rstrip().split()))
print(simpleArraySum(ar))