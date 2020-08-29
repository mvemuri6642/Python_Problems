# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:43:30 2020

@author: tejav
"""


T=int(input())
for i in range(0,T):
    val=[]
    m=input().split()
    n=int(m[0])
    p=int(m[1])
    q=int(m[2])
    a='1'
    x=(n-1)+len(a)
    x1=x+1
    res=a.ljust(x,'0')
    res1=a.ljust(x1,'0')
    e=int(res)
    f=int(res1)
    for j in range(e,f):
        if(j%p==0 and j%q==0):
            val.append(j)
    print(len(val))
    for k in val:
        print(k,end=" ")
