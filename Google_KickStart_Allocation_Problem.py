
tc=0
T=int(input())
for i in range(1,T+1):
	tc+=1
	A=[]
	N,B=map(int,input().split())	
	A=(list(map(int,input().rstrip().split())))
	A.sort()
	ans=0
	for k in range(0,len(A)):
		if(B>=A[k]):
			ans+=1
			B-=A[k]
		else:
			break
	print('Case #{}: {}'.format(tc,ans))



		