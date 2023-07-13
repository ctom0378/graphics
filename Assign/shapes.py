import turtle as t



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
except:
    print("Invalid input!!! \n\nYour input should be between 1 to 9")
    exit()


tim=t.Turtle()
tim.ht()
tim.speed("fastest")
tim.pencolor("#696969")
tim.forward(1000)
tim.home()
tim.right(180)
tim.forward(1000)
tim.home()
tim.right(90)
tim.forward(1000)
tim.home()
tim.left(90)
tim.forward(1000)
tim.home()
tim.pencolor("#000000")
tim.pensize(1)
tim.pu()
tim.setpos(50,50)
tim.pd()

if n==1:
    tim.pu()
    tim.setpos(75,75)
    tim.pd()
    tim.circle(75)
else:
    for _ in range(n+1):
        angle=360/(n+1)
        tim.forward(75)
        tim.left(angle)
screen=t.Screen()
screen.exitonclick()