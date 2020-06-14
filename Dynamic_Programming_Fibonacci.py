# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 01:29:48 2020

@author: saima
"""

'''Dynamic Programming Fibonacci Series'''

'''Top Down Approach'''
def fib(n):
    mem=[0]*(n+1)
    if n<=1:
        return n 
    else:
        if(mem[n-1]==0):
            mem[n-1]=fib(n-1)
        if(mem[n-2]==0):
            mem[n-2]=fib(n-2)
    
    '''memorization'''
    mem[n]=fib(n-1)+fib(n-2)
    return mem[n]
print(fib(8))








'''Bottom Up Approach'''

def fib(n):
    a=[0,1]
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]
n=int(input())
print(fib(n))

