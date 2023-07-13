import turtle as t



def qu(c):
    if c==1:
        tim.goto(85,20)
    elif c==2:
        tim.goto(-200,20)
    elif c==4:
        tim.goto(-200,-250)
    elif c==3:
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
tim.pu()
tim.home()
tim.pd()



print("Select the shape you want to make:")
print("1.Circle")
print("2.Triangle")
print("3.Rectangle")
print("4.Pentagon")
print("5.Hexagon")
print("6.Heptagon")
print("7.Octatagon")
print("8.Nonagon")
print("9.Decagon")
try:
    n=int(input())
    if n>10 or n<1:
        print("Invalid input!!! \n\nYour input should be between 1 to 9")
        exit()
    c=int(input("select the quardent\n1.first\n2.second\n3.third\n4.forth\n"))
except:
    print("Invalid input!!! \n\nYour input should be between 1 to 9")
    exit()




if n==1:
    tim.pu()
    qu(c)
    tim.pd()
    tim.circle(75)
else:
    tim.pu()
    qu(c)
    tim.pd()
    for _ in range(n+1):
        angle=360/(n+1)
        tim.forward(75)
        tim.left(angle)
screen=t.Screen()
screen.exitonclick()
