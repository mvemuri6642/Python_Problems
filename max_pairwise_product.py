def max_pairwise_product(numbers):
	prod=0
	for i in range(len(numbers)):
		for j in range(i+1,len(numbers)):
			prod=max(prod,numbers[i]*numbers[j])
	print(prod)
		
		
		
n=int(input())
numbers=[int(x) for x in input().split()]
max_pairwise_product(numbers)