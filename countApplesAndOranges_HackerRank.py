def countApplesAndOranges(s,t,a,b,m,n,apples,oranges):
	acount=0
	ocount=0
	for i in range(m):
		if(s<=a+apples[i]<=t):
			acount=acount+1		
	for j in range(n):
		ores=0
		ores=b+oranges[j]
		if(s<=ores<=t):
			ocount=ocount+1
	print(acount)
	print(ocount)
		

s,t=map(int,input().rstrip().split())
a,b=map(int,input().rstrip().split())
m,n=map(int,input().rstrip().split())
apples=list(map(int,input().rstrip().split()))
oranges=list(map(int,input().rstrip().split()))
countApplesAndOranges(s,t,a,b,m,n,apples,oranges)
