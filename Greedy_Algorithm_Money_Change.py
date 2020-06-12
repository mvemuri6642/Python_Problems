def change(v):
    deno=[1,2,5,10,20,50,100,200,500,2000]
    n=len(deno)
    i=n-1
    ans=[]
    while(i>=0):
        while(v>=deno[i]):
            v-=deno[i]
            ans.append(deno[i])
        i-=1
    for i in range(len(ans)):
        print(ans[i],end=' ')
        
v=int(input())
change(v)
        
        
        