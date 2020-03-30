import math
def plusMinus(arr):
	z=l=g=0
	for i in range(len(arr)):
		if(arr[i]==0):
			z+=1
		elif(arr[i]>0):
			g+=1
		else:
			l+=1
	print(g/len(arr))
	print(l/len(arr))
	print(z/len(arr))
	
n=int(input())
arr=list(map(int,input().split()))
plusMinus(arr)