# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:10:34 2020

@author: saima
"""


coins=[2,3,5,10]
w=15
a=[[0 for x in range(w+1)] for x in range(len(coins))]
for i in range(0,len(coins)):
    a[i][0]=1
    for j in range(1,w+1):
        if(coins[i]>j):
            a[i][j]=a[i-1][j]
        else:
            a[i][j]=a[i-1][j]+a[i][j-coins[i]]
print(a[i][j])