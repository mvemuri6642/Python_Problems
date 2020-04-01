def birthdayCakeCandles(ar):
	height=max(ar)
	sum=0
	for i in range(len(ar)):
		if ar[i]>=height:
			sum+=1
	print(sum)

n=int(input())	
ar=[int(i) for i in input().split()]
birthdayCakeCandles(ar)