n=int(input())
first=second=0
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if(arr[i]>first):
        second=first
        first=arr[i]
    elif(arr[i]>second and arr[i]!=first):
        second=arr[i]
print(second)