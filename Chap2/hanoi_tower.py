# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:45:52 2021

@author: lch72
"""

def hanoi_tower(n, fr, tmp, to):
    
    if(n==1):
        print("원판 1: %s -> %s"%(fr, to))
    
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s -> %s" % (n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)
    

hanoi_tower(4, 'A', 'B', 'C')