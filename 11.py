# -*- coding: utf-8 -*-
# File: 11.py
# Author: XiaoQi
# Time: 2018/7/10 16:50
"""
Do have a faith in what you're doing,
Make your life a story worth telling.
"""


a = range(1,10)
print(a)

a = xrange(10)
print(a)



f = open('a.txt')
b = f.read()
print(b)
print(type(b))
f.close()

f = open('a.txt')
b = f.readline()
print(type(b))
while b:
    print(b)
    b = f.readline()
f.close()

f = open('a.txt')
b = f.readlines()
print(type(b))
print(b)
f.close()

except: # 捕捉所有异常
except:<异常> # 捕捉指定异常
except:<异常1， 异常2，...> # 捕捉多个异常


a = [1,3,4,5,5,6,3]
import random
b = random.shuffle(a)
print(b)

d = {'a':24, 'g':54, 'l':12, 'k':9}
print(sorted(d.items(), key=lambda x:x[1]))

def num(n):
    for m in range(1,n+1):
        if m % 3 == 0:
            print (m)
num(n=100)



a = 10
b = 20
c = [a]
a = 15
print(a)










import graphics
win = graphics.GraphWin()
win.close()
win=graphics.GraphWin()

from graphics import *
win = GraphWin()



from graphics import *
win=GraphWin()
leftEye=Circle(Point(80,80),5)
leftEye.setFill("yellow")
leftEye.setOutline("red")
rightEye=leftEye
rightEye.move(40,0)

leftEye.draw(win)
rightEye.draw(win)








