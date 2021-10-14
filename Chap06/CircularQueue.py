# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:27:51 2021

@author: lch72
"""

MAX_QSIZE = 10

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items=[0]*MAX_QSIZE
    
    def isEmpty(self):
        return self.front == self.rear
            
    def isFull(self):
        return self.front%MAX_QSIZE ==(self.rear+1)%MAX_QSIZE
    
    def claer(self):
        self.front == self.rear
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
        
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    
    def display(self):
        out = []
        if self.front<self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE]+self.items[0:self.rear+1]
        print("[f= %s, r = %d] ==> "%(self.front, self.rear), out)
'''      
q = CircularQueue()
for i in range(8):
    q.enqueue(i)
q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range(8,14):
    q.enqueue(i)
q.display()'''
        