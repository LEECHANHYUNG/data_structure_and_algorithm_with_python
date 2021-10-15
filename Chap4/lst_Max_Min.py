# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:30:17 2021

@author: lch72

리스트에서 최대 최소 항목 찾는 함수 
"""
print("리스트 입력(정수)")
lst = list(map(int, input().split()))
    
print(list(lst))
    
def MAX_elem(lst):
    highest = lst[0]
    for i in range(len(lst)):
        if lst[i] > highest:
            highest = lst[i]
    return highest

def MIN_elem(lst):
    lowest = lst[0]
    for i in range(len(lst)):
        if lst[i] < lowest:
            lowest = lst[i]
    return lowest

print("리스트의 최대값 : ", MAX_elem(lst), "리스트의 최솟값 : ", MIN_elem(lst))

