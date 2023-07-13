import turtle as t
s = t.Screen()
s.tracer(False)


def drawCordinate():
    t.setworldcoordinates(-600, -600, 600, 600)
    t.speed(0)
    x = -600
    y1 = 600
    y2 = -600
    for i in range(60):
        if i==0:
            pass
        elif i == 30:
            t.pensize(5)
            t.color("#019267")
            t.pu()
            t.goto(x, y1)
            t.pd()
            t.goto(x, y2)
        elif i%10 ==0:
            t.color("#00C897")
            t.pensize(3)
            t.pu()
            t.goto(x, y1)
            t.pd()
            t.goto(x, y2)
        elif i%5 ==0:
            t.color("#65C18C")
            t.pensize(2)
            t.pu()
            t.goto(x, y1)
            t.pd()
            t.goto(x, y2)
        else:
            t.color("#C1F4C5")
            t.pensize(1)
            t.pu()
            t.goto(x, y1)
            t.pd()
            t.goto(x, y2)
        x += 20

    y = -600
    x1 = -600
    x2 = 600
    for i in range(60):
        if i==0:
            pass
        elif i==30:
            t.pensize(5)
            t.color("#019267")
            t.pu()
            t.goto(x1, y)
            t.pd()
            t.goto(x2, y)
            y += 20
        elif i %10 ==0:
            t.pensize(3)
            t.color("#00C897")
            t.pu()
            t.goto(x1, y)
            t.pd()
            t.goto(x2, y)
            y += 20
        elif i %5 ==0:
            t.pensize(2)
            t.color("#65C18C")
            t.pu()
            t.goto(x1, y)
            t.pd()
            t.goto(x2, y)
            y += 20
        else:
            t.pensize(1)
            t.color("#C1F4C5")
            t.pu()
            t.goto(x1, y)
            t.pd()
            t.goto(x2, y)
            y += 20


if __name__ == '__main__':
    drawCordinate()
    t.exitonclick()
    s.tracer(True)
