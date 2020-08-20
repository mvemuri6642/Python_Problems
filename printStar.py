# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 00:46:25 2020

@author: tejav
"""


n=5
k=(2*n)-1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")