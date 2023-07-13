# Write a python program to draw a line using DDA and BRESENHAM's algorithm.





# Using Brasenham's Algorithm

import turtle as t;

s = t.Screen()
s.tracer(False)
def drawLine(x1,y1,x2,y2):
    t.pu()
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1 
    p = 2 * dy - dx
    t.goto(x,y)
    t.pd()
    while x < x2 :
        if p >= 0 :
            t.goto(x,y)
            y = y + 1
            p = p + 2*dy - 2*dx 
        else:
            t.goto(x,y)
            p = p + 2*dy 
            x = x+1
    t.done()


drawLine(10,100,200,100)
s.tracer(True)



# Using DDA 


import turtle as t 

def dda():
    x1 = int(input("x1 : ")) 
    y1 = int(input("y1 : "))
    x2 = int(input("x2 : "))
    y2 = int(input("y2 : "))
    s = 0
    t.penup()
    t.goto(x1,y1)
    t.pensize(2)
    t.pd()
    s = abs(y2-y1) if abs(y2-y1)>abs(x2-x1) else abs(x2-x1)
    yI = round(y2-y1)/s
    xI = round(x2-x1)/s
    for i in range(s):
        t.goto(x1,y1)
        x1 = x1 + xI
        y1 = y1 + yI
    t.exitonclick()
    

dda()

