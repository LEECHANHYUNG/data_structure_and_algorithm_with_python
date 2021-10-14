# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:40:47 2021

@author: lch72
"""

class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) ==0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i]>self.items[highest]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)
print("PQueue: ", q.items)
while not q.isEmpty() :
    print("MAX Priority: ", q.dequeue())