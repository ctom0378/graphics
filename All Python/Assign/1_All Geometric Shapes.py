# 1. Draw the following geometric shapes using python:
# Triangle
# Circle
# Square
# Rectangle
# Rhombus
# Trapezium
# Oval
# Line



import turtle as t
s = t.Screen()
s.tracer(False)


def menu():
    print('==Choice==')
    print('1. Line')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Pentagon')
    print('6. Triangle')
    print('7. Rombhus')
    print('8. Oval')
    print('9. Trapezium')
    print('0. Exit')


def drawLine():
    t.pu()
    t.goto(-200, 0)
    t.pd()
    t.goto(200, 0)


def drawCircle():
    t.pu()
    t.goto(200, 0)
    t.pd()
    t.circle(200)


def drawRectangle():
    t.pu()
    t.goto(-300, 100)
    t.pd()
    t.goto(300, 100)
    t.goto(300, -100)
    t.goto(-300, -100)
    t.goto(-300, 100)


def drawSquare():
    t.pu()
    t.goto(-200, 200)
    t.pd()
    t.goto(200, 200)
    t.goto(200, -200)
    t.goto(-200, -200)
    t.goto(-200, 200)


def drawPentagon():
    t.pu()
    t.goto(0, 200)
    t.pd()
    t.goto(400, 0)
    t.goto(200, -200)
    t.goto(-200, -200)
    t.goto(-400, 0)
    t.goto(0, 200)


def drawTriangle():
    t.pu()
    t.goto(-200, -100)
    t.pd()
    t.goto(200, -100)
    t.goto(0, 300)
    t.goto(-200, -100)


def drawRhombus():
    x = [200,-400,-600,0]
    y = [300,300,-300,-300]
    t.pu()
    t.goto(x[0],y[0])
    t.pd()
    for i in range(1,4):
        t.goto(x[i],y[i])
    t.goto(x[0],y[0])

def drawOval():
    t.seth(-45)   
    for x in range(2):
        t.circle(100,90)
        t.circle(50,90)



def drawTrapezium():
    x = [100,-100,-300,300]
    y = [200,200,-200,-200]
    t.pu()
    t.goto(x[0],y[0])
    t.pd()
    for i in range(1,4):
        t.goto(x[i],y[i])
    t.goto(x[0],y[0])

if __name__ == '__main__':
    t.setworldcoordinates(-600, -600, 600, 600)
    t.pensize(3)
    while True:
        menu()
        c = input('Choice : ')
        t.reset()
        t.setworldcoordinates(-600, -600, 600, 600)
        t.speed(0)
        t.pensize(3)
        if c == '1':
            drawLine()
        elif c == '2':
            drawCircle()
        elif c == '3':
            drawRectangle()
        elif c == '4':
            drawSquare()
        elif c == '5':
            drawPentagon()
        elif c == '6':
            drawTriangle()
        elif c == '7':
            drawRhombus()
        elif c == '8':
            drawOval()
        elif c == '9':
            drawTrapezium()
        elif c == '0':
            break
        t.hideturtle()
        s.tracer(True)
