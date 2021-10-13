# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:32:14 2021

@author: lch72
"""

class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed
   
    def speedUp(self):
        self.speed += 10
    
    def speedDown(self):
        self.speed -= 10
        
    def __eq__(self, CarB):
        return self.color == CarB.color
    
    def __str__(self):
        return "color = %s, speed = %d" %(self.color, self.speed)

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo
    
    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo
    
    def speedUp(self):
        if self.bTurbo:
            self.speed +=50
        else:
            super().speedUp()
    def __str__(self):
        if self.bTurbo:
            return "[%s][speed = %d] 터보모드" % (self.color, self.speed)
        else:
            return "[%s][speed = %d] 일반모드" % (self.color, self.speed)
            
car1 = Car('black',0)
car2 = Car('red', 120)
car3 = Car('yellow', 30)
car4 = Car('blue', 0)
car5 = Car('green')

car2.speedDown()
car4.speedUp()
car3.color = 'purple'
car5.speed = 100

print("[car3]", car3)

s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White", 0, False)
s1.speedUp()
s2.speedUp()
print("슈퍼카1:", s1)
print("슈퍼카2:", s2)