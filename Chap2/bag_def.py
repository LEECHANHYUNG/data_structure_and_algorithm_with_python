# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:54:06 2021

@author: lch72
"""

def contains(bag, e):
    return e in bag

def insert(bag, e):
    return bag.append(e)

def remove(bag, e):
    return bag.remove(e)

def count(bag):
    return len(bag)

myBag = []
insert(myBag, "python")
insert(myBag, "C++")
insert(myBag, "Java")
insert(myBag, "C#")

print(contains(myBag, "python"))
remove(myBag, "python")
print("가방속의 물건:", myBag)
print("가방속의 물건의 개수 : ", count(myBag))
