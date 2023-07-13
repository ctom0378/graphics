# 15.  Write a python program to draw a hexagon on the screen.


import turtle as t
s = t.Screen()
s.tracer(False)
def drawHexagon():
    t.pu()
    t.goto(-100,200)
    t.pd()
    x = [200,300,200,-100,-200,-100]
    y = [200,0,-200,-200,0,200]
    for i in range(len(x)):
        t.goto(x[i],y[i])


drawHexagon()
s.tracer(True)
t.done()

