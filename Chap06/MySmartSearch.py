# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:54:14 2021

@author: lch72
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:20:10 2021

@author: lch72
"""

from CircularQueue import CircularQueue
from PriorityQueue import PriorityQueue
map = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']
       ]

MAZE_SIZE = 6

import math		
(ox,oy) = (5, 4)	
def dist(x,y) :			 
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)

def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i][2]>self.items[highest][2]:
                    highest = i
            return highest

def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x] =="0" or map[y][x] =="x"



def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1, -dist(0,1)))
    print('PQueue:')
    
    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end="->")
        x,y,_ = here
        if(map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                q.enqueue((x,y-1, -dist(x,y-1)))
            if isValidPos(x, y+1):
                q.enqueue((x,y+1,-dist(x,y+1)))
            if isValidPos(x-1, y):
                q.enqueue((x-1,y, -dist(x-1,y)))
            if isValidPos(x+1, y):
                q.enqueue((x+1,y, -dist(x+1, y)))
        print("우선순위 큐:", q.items)
    return False
        

result = MySmartSearch()
if result :
    print("미로 탐색 성공")
else:
    print("미로 탐색 실패")