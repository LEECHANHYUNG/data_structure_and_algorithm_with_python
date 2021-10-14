# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:20:10 2021

@author: lch72
"""

from CircularQueue import CircularQueue

map = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']
       ]

MAZE_SIZE = 6

def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x] =="0" or map[y][x] =="x"

def BFS():
    que = CircularQueue()
    que.enqueue((0,1))
    print("BFS: ")
    
    while not que.isEmpty():
        here = que.dequeue()
        print(here, " => ", end = "")
        x,y = here
        if (map[y][x] == 'x'):
            return True
        
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                que.enqueue((x,y-1))
            if isValidPos(x, y+1):
                que.enqueue((x,y+1))
            if isValidPos(x-1, y):
                que.enqueue((x-1,y))
            if isValidPos(x+1, y):
                que.enqueue((x+1,y))
    return False

        
result = BFS()
if result :
    print("미로 탐색 성공")
else:
    print("미로 탐색 실패")