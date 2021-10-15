# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:40:15 2021

@author: lch72

리스트의 동일항목 찾는 함수
"""

lst1 = list(map(int, input("리스트 1 입력:").split()))
lst2 = list(map(int, input("리스트 2 입력:").split()))

def same_elem(lst1, lst2):
    result = 0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                result += 1
                break
    if result !=0:
        return True
    else:
        return False
print(same_elem(lst1, lst2))


