# 14. Write a python program to draw a circle with center (150,150) pixel and radius 25


import turtle as t
s = t.Screen()
s.tracer(False)
def drawCircle():
    t.pu()
    t.goto(150,150)
    t.pd()
    t.circle(25)

drawCircle()
s.tracer(True)
t.done()
