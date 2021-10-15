# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:13:41 2021

@author: lch72
라인 편집기
"""
from list_class import ArrayList

def myLineEditor():
    list = ArrayList()
    while True:
        command = input("[메뉴선택] i - 입력, d - 삭제, r - 변경, p - 출력, l - 파일 읽기, s - 저장, q - 종료 =>")
        
        if command == "i":
            pos = int(input("입력행 번호:"))
            elem = input("입력행 내용:")
            list.insert(pos, elem)
        
        elif command == "d":
            pos = int(input("삭제행 번호:"))
            list.delete(pos)
        elif command == "r":
            pos = int(input("변경행 번호:"))
            elem = input("변경행 내용:")
            list.replace(pos, elem)
        elif command == "p":
            pos = int(input("출력행 번호:"))
            return list.getEntry(pos)
        elif command =="q":
            break;
myLineEditor()

            