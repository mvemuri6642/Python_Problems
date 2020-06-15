# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:00:55 2020

@author: saima
"""
import sys
import math

def tsp(mask,pos):
    
    newAns=0
    visited=(1<<n)-1
    ans=sys.maxsize
    dp=[[-1]*(4) for x in range(1<<4)]
    if(mask==visited):
        return dist[pos][0]
    if(dp[mask][pos]!=-1):
        return dp[mask][pos]
    for i in range(0,n):
        if((mask &(1<<i))==0):
            newAns=dist[pos][i]+tsp(mask|(1<<i),i)
            ans=min(ans,newAns)
    dp[mask][pos]=ans
    return dp[mask][pos]

n=int(input('Enter n Value:'))
dist=[[int(x) for x in input('Enter Matrix Values: ').split()] for x in range(n)]
print(tsp(1,0))
    
    
    
    
    
    
    
    
