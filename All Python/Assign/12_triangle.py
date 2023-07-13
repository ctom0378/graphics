# 12. Write a python program to rotate a triangle

import turtle

t=turtle.Turtle() 
t.screen.bgcolor("yellow") 
t.color("blue") 
t.width(4)
t.speed(10)

#Right Triangle 
t.pu()
t.goto(-300,100) 
t.pd()
t.lt(90)
t.fd(100)
t.bk(100)
t.rt(90)
t.fd(100)
t.lt(135)
t.fd(140)
t.pu()

#Obtuse Triangle 
t.pu()
t.goto(-100,100) 
t.pd()
t.fd(150)
t.bk(150)
t.rt(135)
t.fd(150)
t.lt(157)
t.fd(277) 

#Acute Triangle 
t.pu() 
t.goto(95,100) 
t.pd()
t.rt(157)
t.fd(180)
t.lt(135)
t.fd(150)
t.lt(100)
t.fd(130)

t.ht() 
turtle.done()
