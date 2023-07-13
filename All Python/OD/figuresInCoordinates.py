import turtle
import random
def getInt(displayStr = ''):
    while True:
        try:
            n = int(input(displayStr))
            break
        except:
            print("Enter a valid number!")
    return n

def setScreen():
    sc = turtle.Screen()
    llx = -600
    lly = -600
    urx = 600
    ury = 600
    turtle.setworldcoordinates(llx,lly,urx,ury)
    point1 = (0,-urx)
    point2 = (0,urx)
    point3 = (urx,0)
    point4 = (llx,0)
    newpt1 = (0,-ury)
    newpt2 = (llx,0)
    turtle.speed(0)
    # turtle.penup()
    # turtle.goto(point1)
    # turtle.pendown()
    # changing
    turtle.penup()
    turtle.goto(newpt1)
    turtle.left(90)
    for i in range(20):
        turtle.pendown()
        turtle.forward(30)
        turtle.penup()
        turtle.forward(30)
    turtle.penup()
    turtle.goto(newpt2)
    turtle.right(90)
    for i in range(20):
        turtle.pendown()
        turtle.forward(30)
        turtle.penup()
        turtle.forward(30)

    # while True:
    #     c_num = getInt('Enter coordinate : ')
    #     lineInCordinate(c_num,turtle)
    # turtle.exitonclick()




def startDrawing():
    while True:
        c_num = getInt('Enter coordinate : ')
        turtle.clear()
        setScreen()
        lineInCordinate(c_num,turtle)
    turtle.exitonclick()   



def drawingOptions():
    print('==Drawing options==')
    print('1. Line')
    print('2. Circle')
    print('3. Square')
    print('4. Triangle')
    print('5. Rectangle')

def lineDrawOptions():
    print("==Line drawing options ==")
    print("1. 45 deg")
    print("2. Vertical")
    print("3. Horizontal")

def lineDrawing(p1,p2):
    turtle.penup()
    turtle.goto(p1)
    turtle.pendown()
    turtle.goto(p2)

def circleDrawing(p1,r):
    turtle.pu()
    turtle.goto(p1)
    turtle.pd()
    turtle.circle(r)

def squareDrawing(p1,r):
    turtle.penup()
    turtle.goto(p1)
    turtle.pd()
    for i in range(4):
        turtle.forward(r)
        turtle.right(90)

def triangleDrawing(p,r):
    turtle.penup()
    turtle.goto(p)
    turtle.pendown()
    for i in range(3):
        turtle.forward(r)
        turtle.left(120)


def rectangleDrawing(p,r):
    turtle.penup()
    turtle.goto(p)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(r)
        turtle.left(90)
        turtle.forward(r/2)
        turtle.left(90)

def lineInCordinate(cor,turtle):
    r1 = random.randint(0,50)
    r2 = random.randint(100,600)
    if cor == 1:

        drawingOptions()
        dc = getInt('Option : ')
        if dc == 1:
            lineDrawOptions()
            lineDrawChoice = getInt('Choice : ')
            if lineDrawChoice == 1:
                p1 = (r1,r1)
                p2 = (r2,r2)
                turtle.penup()
                turtle.goto(p1)
                turtle.pendown()
                turtle.goto(p2)
            if lineDrawChoice == 2:
                rx1 = random.randint(50,200)
                ry1 = random.randint(10,40)
                ry2 = random.randint(500,600)
                p1 = (rx1,ry1)
                p2 = (rx1,ry2)
                lineDrawing(p1,p2)
            if lineDrawChoice == 3:
                ry1 = random.randint(10,400)
                rx1 = random.randint(50,200)
                rx2 = random.randint(500,600)
                p1 = (rx1,ry1)
                p2 = (rx2,ry1)
                lineDrawing(p1,p2)
        elif dc == 2:
            p1 = (500,250)
            r = 200
            circleDrawing(p1,r)
        elif dc == 3:
            p1 = (100,500)
            r = random.randint(100,300)
            squareDrawing(p1,r)
        elif dc == 4:
            p1 = (100,100)
            r = random.randint(100,300)
            triangleDrawing(p1,r)
        elif dc == 5:
            p1 = (100,100)
            r = random.randint(400,500)
            rectangleDrawing(p1,r)

    if cor == 2:
        drawingOptions()
        dc = getInt('Option : ')
        if dc == 1:
            lineDrawOptions()
            lineDrawChoice = getInt('Choice : ')
            if lineDrawChoice == 1:
                p1 = (-r1,r1)
                p2 = (-r2,r2)
                turtle.penup()
                turtle.goto(p1)
                turtle.pendown()
                turtle.goto(p2)
            if lineDrawChoice == 2:
                rx1 = random.randint(50,200)
                ry1 = random.randint(10,40)
                ry2 = random.randint(500,600)
                p1 = (-rx1,ry1)
                p2 = (-rx1,ry2)
                lineDrawing(p1,p2)
            if lineDrawChoice == 3:
                ry1 = random.randint(10,400)
                rx1 = random.randint(50,200)
                rx2 = random.randint(500,600)
                p1 = (-rx1,ry1)
                p2 = (-rx2,ry1)
                lineDrawing(p1,p2)
        elif dc == 2:
            p1 = (-500,250)
            r = 200
            circleDrawing(p1,r)
        elif dc == 3:
            p1 = (-500,500)
            r = random.randint(100,300)
            squareDrawing(p1,r)
        elif dc == 4:
            p1 = (-500,100)
            r = random.randint(100,300)
            triangleDrawing(p1,r)
        elif dc == 5:
            p1 = (-500,100)
            r = random.randint(400,500)
            rectangleDrawing(p1,r)

    if cor == 3:
        drawingOptions()
        dc = getInt('Option : ')
        if dc == 1:
            lineDrawOptions()
            lineDrawChoice = getInt('Choice : ')
            if lineDrawChoice == 1:
                p1 = (-r1,-r1)
                p2 = (-r2,-r2)
                turtle.penup()
                turtle.goto(p1)
                turtle.pendown()
                turtle.goto(p2)
            if lineDrawChoice == 2:
                rx1 = random.randint(50,200)
                ry1 = random.randint(10,40)
                ry2 = random.randint(500,600)
                p1 = (-rx1,-ry1)
                p2 = (-rx1,-ry2)
                lineDrawing(p1,p2)
            if lineDrawChoice == 3:
                ry1 = random.randint(10,400)
                rx1 = random.randint(50,200)
                rx2 = random.randint(500,600)
                p1 = (-rx1,-ry1)
                p2 = (-rx2,-ry1)
                lineDrawing(p1,p2)
        elif dc == 2:
            p1 = (-250,-500)
            r = 200
            circleDrawing(p1,r)
        elif dc == 3:
            p1 = (-500,-100)
            r = random.randint(100,300)
            squareDrawing(p1,r)
        elif dc == 4:
            p1 = (-500,-500)
            r = random.randint(100,300)
            triangleDrawing(p1,r)
        elif dc == 5:
            p1 = (-500,-500)
            r = random.randint(400,500)
            rectangleDrawing(p1,r)
    if cor == 4:
        drawingOptions()
        dc = getInt('Option : ')
        if dc == 1:
            lineDrawOptions()
            lineDrawChoice = getInt('Choice : ')
            if lineDrawChoice == 1:
                p1 = (r1,-r1)
                p2 = (r2,-r2)
                turtle.penup()
                turtle.goto(p1)
                turtle.pendown()
                turtle.goto(p2)
            if lineDrawChoice == 2:
                rx1 = random.randint(50,200)
                ry1 = random.randint(10,40)
                ry2 = random.randint(500,600)
                p1 = (rx1,-ry1)
                p2 = (rx1,-ry2)
                lineDrawing(p1,p2)
            if lineDrawChoice == 3:
                ry1 = random.randint(10,400)
                rx1 = random.randint(50,200)
                rx2 = random.randint(500,600)
                p1 = (rx1,-ry1)
                p2 = (rx2,-ry1)
                lineDrawing(p1,p2)
        elif dc == 2:
            p1 = (250,-500)
            r = 200
            circleDrawing(p1,r)
        elif dc == 3:
            p1 = (100,-100)
            r = random.randint(100,300)
            squareDrawing(p1,r)
        elif dc == 4:
            p1 = (100,-500)
            r = random.randint(100,300)
            triangleDrawing(p1,r)
        elif dc == 5:
            p1 = (100,-500)
            r = random.randint(400,500)
            rectangleDrawing(p1,r)
    if cor == 0:
        exit()

        # p1 = (r1,-r1)
        # p2 = (r2,-r2)
        # turtle.penup()
        # turtle.goto(p1)
        # turtle.pendown()
        # turtle.goto(p2)
        


def drawline(llx,lly,urx,ury,cor=1):
    point1 = (urx,ury)
    point2 = (urx,-ury)
    point3 = (llx,lly)
    point4 = (llx,-lly)
    top1y = (0,lly-5)
    if cor == 1 :
        turtle.penup()
        turtle.goto(point2)
        turtle.pendown()
        turtle.goto(top1y)
        turtle.done()
   

    


# setScreen()
startDrawing()

