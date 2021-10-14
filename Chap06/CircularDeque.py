# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:17:57 2021

@author: lch72
"""

from CircularQueue import CircularQueue
MAX_QSIZE = 10
class Circulardeque(CircularQueue):
    def _init__(self):
        super.__init__()    
    def addRear(self, item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front-1
            if self.front<0:
                self.front = MAX_QSIZE-1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear-1
            if self.rear<0:
                self.rear = MAX_QSIZE-1
            return item
        
    def getRear(self):
        return self.items[self.rear]
    
dq = Circulardeque()
for i in range(9):
    if i%2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display()
for i in range(2): 
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
dq.display()
for i in range(9,14):
    dq.addFront(i)
dq.display()