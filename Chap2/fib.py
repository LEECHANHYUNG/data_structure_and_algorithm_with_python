# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:38:42 2021

@author: lch72
"""

def fib_recursion(n):
    if n==0: return 0
    elif n==1: return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)
    
print(fib_recursion(6))

def fib_iter(n):
    if(n<2): return n
    
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

print(fib_iter(5))