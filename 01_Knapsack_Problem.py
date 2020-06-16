# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 02:21:39 2020

@author: saima
"""

import math
wt=[0,3,4,5,6]
val=[0,2,3,4,1]
n=4
w=8
a=[[0]*(w+1) for i in range(5)]
for i in range(n+1):
    for j  in range(w+1):
        if(i==0):
            a[i][j]=0
        elif(j==0):
            a[i][j]=0
        elif(wt[i]>j):
            a[i][j]=a[i-1][j]
        else:
            a[i][j]=max(a[i-1][j],a[i-1][j-wt[i]]+val[i])
        
print(a)
        
        

        
        