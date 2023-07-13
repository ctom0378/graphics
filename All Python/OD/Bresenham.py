import turtle

bre = turtle.Turtle()
turtle.setworldcoordinates(-360, -360, 360, 360)
bre.pu()

def xgrids():
    bre.speed(10000)
    bre.pu()
    bre.goto(-350, 350)
    bre.color("lightgreen")
    i = 350
    x = -350
    while (i > -350):
        bre.pd()
        bre.goto(350, i)
        i = i - 10
        bre.pu()
        bre.goto(-350, i)


def ygrids():
    bre.speed(10000)
    bre.pu()
    bre.goto(-350, 350)
    bre.color("lightgreen")
    i = -350
    y = 350
    while (i < 350):
        bre.pd()
        bre.goto(i, -350)
        i = i + 10
        bre.pu()
        bre.goto(i, 350)


def x_y_axis():
    bre.pu()
    bre.goto(0, 350)
    bre.pd()
    bre.write("y", font=("Arial", 12, "bold"))
    bre.goto(0, -350)
    bre.pu()
    bre.goto(2,-350)
    bre.pd()
    bre.write("-y", font=("Arial", 12, "bold"))
    bre.pu()
    bre.goto(-350, 0)
    bre.pd()
    bre.write("-x", font=("Arial", 12, "bold"))
    bre.goto(350, 0)
    bre.write("x", font=("Arial", 12, "bold"))
    bre.goto(0, 0)
    bre.write("O", font=("Arial", 12, "bold"))


def plot(x,y):
    bre.pd()
    bre.goto(round(x,2),round(y,2))
    print(f"Next Point : {round(x,2),round(y,2)}")

xgrids()
ygrids()
bre.color("Black")
x_y_axis()
bre.pu()
bre.goto(0,0)
bre.pd()

x0 = int(input("Enter the starting x value: "))
y0 = int(input("Enter the starting y value: "))
x_end = int(input("Enter the ending x value: "))
y_end = int(input("Enter the ending y value: "))

xi,yi = x0,y0

dx = x_end - x0
dy = y_end - y0
m = dy/dx

p = (2*dy) - dx
bre.write(f"{x0,y0}")
while xi < x_end or yi < y_end:
    if m < 1 :
        if p < 0:
            x1 = xi + 1
            y1 = yi
            plot(x1,y1)
            xi,yi = x1,y1
            p += (2*dy)

        else :
            x1 = xi + 1
            y1 = yi + 1
            plot(x1, y1)
            xi, yi = x1, y1
            p = p + (2 * dy) - (2 * dx)

    else:
        if p < 0:
            x1 = xi
            y1 = yi + 1
            plot(x1, y1)
            xi, yi = x1, y1
            p += (2 * dx)

        else:
            x1 = xi + 1
            y1 = yi + 1
            plot(x1, y1)
            xi, yi = x1, y1
            p = p + (2 * dx) - dy

bre.write(f"{x_end,y_end}")
turtle.done()


