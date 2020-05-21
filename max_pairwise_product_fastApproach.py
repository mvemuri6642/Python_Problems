def max_pairwise_product(numbers):
	p1=max(numbers)
	numbers.remove(p1)
	p2=max(numbers)
	print(p1*p2)



n=int(input())
numbers=[int(x) for x in input().split()]
max_pairwise_product(numbers)