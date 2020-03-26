n=int(input())
for i in range(n):
	v='aeiouAEIOU'
	s=input()
	count=0
	for i in range(0,len(s)):
		if s[i] in v:
			count+=(len(s)-i)*(i+1)
	print(count)