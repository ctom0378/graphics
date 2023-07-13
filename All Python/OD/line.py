import turtle as t
import random

def qu(c):
    if c==2:
        tim.goto(85,20)
    elif c==1:
        tim.goto(-200,20)
    elif c==3:
        tim.goto(-200,-250)
    elif c==4:
        tim.goto(150,-250)


tim=t.Turtle()

tim.speed(10000)

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


def drawLine(ang,len):
    tim.pu()
    qu(c)
    tim.pd()
    tim.lt(ang)
    tim.fd(len)
    screen=t.Screen()
    screen.exitonclick()


try:
    print("ENTER YOUR CHOICE")
    print("1.Horizontal line")
    print("2.Vertical line")
    print("3.coustom angle")
    print("4.Random line")
    lineT=int(input())
    c=int(input("select the quardent\n1.first\n2.second\n3.third\n4.forth\n"))

    if lineT>4 or lineT<1:
        print("Invalid input!!!\nChoose between 1,2,3 and 4")
        exit()

    if lineT==1:
            len=int(input("enter the length you want:"))
            drawLine(0,len)
    elif lineT==2:
            len=int(input("enter the length you want:"))
            drawLine(90,len)
    elif lineT==4:
            len=int(input("enter the length you want:"))
            drawLine(random.randint(1, 180),len)
    elif lineT==3:
            len=int(input("enter the length you want:"))
            angle=int(input("enter the angle:"))
            drawLine(angle,len)
except:
    print("Invalid input!!!")
    exit()

