
#  Write a python program to draw a bezier curve

import turtle as t

tim=t.Turtle()

tim.speed(10)

tim.pu()
tim.setpos(-340,280)
tim.pencolor('lightgreen')
tim.pd()
tim.fd(680)
for _ in range(28):
    tim.rt(90)
    tim.fd(10)
    tim.rt(90)
    tim.fd(680)
    tim.lt(90)
    tim.fd(10)
    tim.lt(90)
    tim.fd(680)
tim.lt(90)
tim.fd(560)

for _ in range(34):
    tim.lt(90)
    tim.fd(10)
    tim.lt(90)
    tim.fd(560)
    tim.rt(90)
    tim.fd(10)
    tim.rt(90)
    tim.fd(560)

tim.pu()
tim.home()
tim.pencolor('black')
tim.pd()
tim.fd(340)
tim.bk(10)
tim.pu()
tim.rt(90)
tim.fd(10)
tim.pd()
tim.write("x")
tim.pu()
tim.home()
tim.pd()
tim.bk(340)
tim.home()
tim.lt(90)
tim.fd(280)
tim.bk(10)
tim.pu()
tim.rt(90)
tim.fd(10)
tim.pd()
tim.write("y")
tim.pu()
tim.home()
tim.pd()
tim.lt(90)
tim.bk(280)







# t.penup()
# #reposition
# t.home()
# t.pendown()
# #change the pen color
# t.pencolor('black')
# t.backward(200)
# t.forward(400)
# t.backward(200)
# t.left(90)
# t.forward(200)
# t.backward(400)
# t.penup()
# t.setpos(5,5)
# t.pendown()
# t.write(0)
# t.penup()
# t.setpos(190,5)
# t.pendown()
# t.write("x")
# t.penup()
# t.setpos(5,190)
# t.pendown()
# t.write("y")
# t.penup()
# t.setpos(0,-180)
# t.pendown()
# t.write("https://artificialintelligencestechnology.com/")
# t.ht()

screen=t.Screen()
screen.exitonclick()