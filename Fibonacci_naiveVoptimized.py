import timeit

code0="""n=int(input())
arr=[]
arr.append(0)
arr.append(1)
for i in range(2,n+1):
	arr.append(arr[i-1]+arr[i-2])
print(arr[n])
"""
elapsed_time = timeit.timeit(code0, number=1)
print('Efficient Method',elapsed_time)



code1="""
def fib(n):
	if(n<2):
		return n
	else:
		return(fib(n-1)+fib(n-2))
n=int(input())
print(fib(n))
"""
elapsed_time = timeit.timeit(code1, number=1)
print('Naive Method Time Elapsed',elapsed_time)