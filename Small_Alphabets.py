import turtle

alphabet = turtle.Turtle()
sc = turtle.Screen()
sc.tracer(False)
turtle.setworldcoordinates(-500, -500, 500, 500)
alphabet.pu()
alphabet.setpos(-500, 350)
alphabet.speed(1000)
x, y = -500, 400


# turtle.setworldcoordinates(-360, -360, 360, 360)

def putspace(d=50):
    global x
    alphabet.seth(0)
    alphabet.pu()
    alphabet.fd(d)
    # checkX()
    alphabet.pd()
    x += d + d



def checkX(d=150):
    global x, y
    if x >= 400:
        y -= d
    alphabet.pu()
    alphabet.goto(-500, y)
    x = -500


def drawa():
    putspace()
    alphabet.seth(0)
    for i in range(6):
        alphabet.fd(50)
        alphabet.lt(90)
    alphabet.seth(90)
    alphabet.fd(50)
    alphabet.seth(180)
    alphabet.fd(50)
    alphabet.bk(50)
    alphabet.seth(90)
    alphabet.bk(100)


def drawb():
    putspace()
    alphabet.seth(0)
    for i in range(4):
        alphabet.fd(50)
        alphabet.lt(90)
    alphabet.seth(90)
    alphabet.fd(120)
    alphabet.bk(120)
    alphabet.seth(0)
    alphabet.fd(50)


def drawc():
    putspace()
    alphabet.seth(0)
    alphabet.fd(50)
    alphabet.bk(50)
    alphabet.lt(90)
    alphabet.fd(70)
    alphabet.seth(0)
    alphabet.fd(50)
    alphabet.pu()
    alphabet.seth(90)
    alphabet.bk(70)


def drawd():
    putspace()
    alphabet.seth(0)
    for i in range(5):
        alphabet.fd(50)
        alphabet.lt(90)
    alphabet.seth(90)
    alphabet.fd(120)
    alphabet.bk(120)
    alphabet.seth(0)


def drawe():
    putspace()
    alphabet.seth(0)
    alphabet.fd(50)
    alphabet.bk(50)
    alphabet.lt(90)
    alphabet.fd(70)
    alphabet.seth(0)
    alphabet.fd(50)
    alphabet.seth(-90)
    alphabet.fd(30)
    alphabet.seth(180)
    alphabet.fd(50)
    alphabet.pu()
    alphabet.seth(90)
    alphabet.bk(40)
    putspace()


def drawf():
    putspace()
    alphabet.seth(90)
    alphabet.fd(50)
    alphabet.seth(0)
    alphabet.fd(20)
    alphabet.bk(40)
    alphabet.fd(20)
    alphabet.seth(90)
    alphabet.fd(50)
    alphabet.circle(-20, 190)
    alphabet.pu()
    alphabet.fd(100)


def drawg():
    putspace()
    alphabet.circle(25, 450)
    alphabet.bk(100)
    alphabet.seth(-90)
    alphabet.circle(-30, 220)
    alphabet.seth(45)
    alphabet.fd(100)
    alphabet.bk(20)

def drawh():
    putspace()
    alphabet.seth(90)
    alphabet.fd(120)
    alphabet.bk(80)
    alphabet.circle(-30,180)
    alphabet.seth(-90)
    alphabet.fd(40)

def drawi():
    putspace()
    alphabet.seth(90)
    alphabet.fd(60)
    alphabet.pu()
    alphabet.fd(20)
    alphabet.pd()
    alphabet.circle(2)
    alphabet.pu()
    alphabet.seth(-90)
    alphabet.fd(80)

def drawj():
    drawi()
    alphabet.pd()
    alphabet.fd(80)
    alphabet.circle(-20,210)
    alphabet.pu()
    alphabet.fd(70)

def drawk():
    putspace()
    alphabet.seth(90)
    alphabet.fd(120)
    alphabet.bk(80)
    alphabet.seth(45)
    alphabet.fd(52)
    alphabet.bk(52)
    alphabet.seth(-45)
    alphabet.fd(52)

def drawl():
    putspace()
    alphabet.seth(90)
    alphabet.fd(100)
    alphabet.bk(100)
    alphabet.seth(-90)
    alphabet.circle(20,200)

def drawm():
    putspace(10)
    alphabet.seth(90)
    alphabet.pu()
    alphabet.fd(60)
    alphabet.pd()
    for i in range(3):
        alphabet.circle(-20,180)
        alphabet.seth(-90)
        alphabet.fd(60)
        alphabet.bk(60)
        alphabet.seth(90)
    alphabet.bk(60)

def drawn():
    putspace()
    alphabet.seth(90)
    alphabet.pu()
    alphabet.fd(60)
    alphabet.pd()
    for i in range(2):
        alphabet.circle(-20, 180)
        alphabet.seth(-90)
        alphabet.fd(60)
        alphabet.bk(60)
        alphabet.seth(90)
    alphabet.bk(60)

def drawo():
    putspace(80)
    alphabet.seth(0)
    alphabet.circle(40)

def drawp():
    putspace(80)
    alphabet.seth(0)
    alphabet.fd(20)
    alphabet.circle(30,180)
    alphabet.fd(20)
    alphabet.seth(-90)
    alphabet.fd(120)
    alphabet.pu()
    alphabet.bk(120)
    alphabet.seth(0)
    putspace()

def drawq():
    putspace(80)
    alphabet.seth(180)
    alphabet.fd(20)
    alphabet.circle(30, 180)
    alphabet.fd(20)
    alphabet.seth(-90)
    alphabet.bk(60)
    alphabet.fd(120)
    alphabet.seth(60)
    alphabet.fd(69)

def drawr():
    putspace(40)
    alphabet.seth(90)
    alphabet.fd(60)
    alphabet.bk(20)
    alphabet.circle(-20,200)
    alphabet.circle(-2)

def draws():
    putspace()
    alphabet.seth(20)
    alphabet.pu()
    alphabet.fd(50)
    alphabet.seth(90)
    alphabet.pd()
    alphabet.circle(20,220)
    alphabet.seth(-15)
    alphabet.fd(42)
    alphabet.seth(-90)
    alphabet.fd(10)
    alphabet.circle(-20,180)
    alphabet.seth(0)
    putspace(40)
    # sougata.seth(-90)
    # sougata.pu()
    # sougata.fd(20)


def drawt():
    putspace()
    alphabet.seth(90)
    alphabet.fd(100)
    alphabet.bk(50)
    alphabet.seth(0)
    alphabet.bk(20)
    alphabet.fd(40)
    alphabet.bk(20)
    alphabet.seth(-90)
    alphabet.fd(50)
    alphabet.circle(15, 160)

def drawu():
    putspace()
    alphabet.seth(90)
    alphabet.fd(60)
    alphabet.bk(50)
    alphabet.seth(-90)
    alphabet.circle(20,180)
    alphabet.fd(50)
    alphabet.bk(50)
    alphabet.seth(-90)
    alphabet.circle(16,120)
    alphabet.pu()
    alphabet.seth(90)
    alphabet.fd(70)
    alphabet.pd()
    putspace()

def drawv():
    # putspace()
    # sougata.seth(110)
    # sougata.fd(75)
    # sougata.bk(75)
    # sougata.seth(70)
    # sougata.fd(75)
    # sougata.bk(75)
    # putspace()
    alphabet.seth(-70)
    alphabet.fd(75)
    alphabet.seth(70)
    alphabet.fd(75)

def draww():
    putspace()
    drawv()
    drawv()

def drawx():
    putspace()
    alphabet.seth(-70)
    alphabet.fd(75)
    alphabet.bk(37.5)
    alphabet.seth(70)
    alphabet.fd(37.5)
    alphabet.bk(70)

def drawy():
    putspace(80)
    alphabet.seth(90)
    alphabet.fd(60)
    alphabet.bk(50)
    alphabet.seth(-90)
    alphabet.circle(20, 180)
    alphabet.fd(50)
    alphabet.bk(150)
    alphabet.seth(-90)
    alphabet.circle(-30, 220)
    alphabet.seth(45)
    alphabet.fd(100)
    alphabet.bk(20)

def drawz():
    putspace()
    alphabet.seth(0)
    alphabet.fd(35)
    alphabet.bk(35)
    alphabet.seth(60)
    alphabet.fd(80)
    alphabet.seth(180)
    alphabet.fd(35)
    alphabet.pu()
    alphabet.seth(-90)
    alphabet.fd(70)
    alphabet.seth(0)
    alphabet.fd(35)
    alphabet.pd()
    # sougata.seth(-60)
    # sougata.circle(-60,100)


sc.bgcolor("white")
alphabet.color("blue")
alphabet.shape("turtle")
alphabet.pensize(10)
alphabet.pd()

drawa()
drawb()
drawc()
drawd()
drawe()
drawf()
drawg()
drawh()
drawi()
drawj()
drawk()
checkX(250)
drawl()
drawm()
drawn()
drawo()
drawp()
drawq()
drawr()
draws()
drawt()
checkX()
drawu()
drawv()
draww()
drawx()
drawy()
drawz()

alphabet.ht()
sc.tracer(True)
turtle.done()