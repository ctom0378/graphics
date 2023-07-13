# . Write the program in python to draw the Capital alphabets A to Z


import turtle as t
s = t.Screen()
s.tracer(False)
x = -1100
y = 700
def calC():
    global x,y
    if x>900:
        x = -1100
        y -= 500
    else :
        x +=200
def A():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x+200,y+400)
    t.goto(x+400,y)
    t.pu()
    t.goto(x+100,y+200)
    t.pd()
    t.goto(x+300,y+200)
    x = x + 400



def B():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x+70,y)
    for _ in range(2):
        t.circle(100,180)
        t.right(180)
    t.goto(x,y+400)
    t.goto(x,y)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+70,y+200)
    t.seth(0)
    x = x + 170

def C():
    global x,y
    t.pu()
    t.goto(x+200,y)
    t.circle(200,180)
    t.pd()
    t.circle(200,180)
    x+= 200

def D():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.circle(200,180)
    t.goto(x,y)
    x+= 200

def E():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.goto(x+200,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+200,y+200)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x+200,y)
    x+=200

def F():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.goto(x+200,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+200,y+200)
    x+=200 

def G():
    global x,y
    t.seth(0)
    t.pu()
    t.goto(x+200,y)
    t.circle(200,180)
    t.pd()
    t.circle(200,150)
    t.circle(100,180)
    t.goto(x+350,y+200)
    t.goto(x+350,y)
    x+= 350

def H():
    t.pu()
    global x,y
    t.seth(0)
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+200,y+200)
    t.pu()
    t.goto(x+200,y+400)
    t.pd()
    t.goto(x+200,y)
    x+= 200

def I():
    t.pu()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x+200,y)
    t.pu()
    t.goto(x+100,y)
    t.pu()
    t.goto(x+100,y)
    t.pd()
    t.goto(x+100,y+400)
    t.pu()
    t.goto(x,y+400)
    t.pd()
    t.goto(x+200,y+400)
    x+= 200

def J():
    t.pu()
    global x,y
    t.goto(x,y+400)
    t.pd()
    t.goto(x+200,y+400)
    t.goto(x+200,y)
    t.pu()
    t.circle(200,280)
    t.pd()
    t.circle(200,80)
    x+= 200

def K():
    t.pu()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+200,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+200,y)
    x+=200

def L():
    t.pu()
    global x,y
    t.goto(x,y+400)
    t.pd()
    t.goto(x,y)
    t.goto(x+200,y)
    x+=200

def M():
    t.pu()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.goto(x+100,y+200)
    t.goto(x+200,y+400)
    t.goto(x+200,y)
    x+= 200


def N():
    t.pu()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.goto(x+200,y)
    t.goto(x+200,y+400)
    x+= 200

def O():
    t.pu()
    global x,y
    t.goto(x+200,y)
    t.pd()
    t.circle(200)
    x+= 400

def P():
    t.pu()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+70,y+200)
    t.circle(100,180)
    t.goto(x,y+400)
    x+= 170

def Q():
    t.pu()
    global x,y
    t.seth(0)
    t.goto(x+200,y)
    t.pd()
    t.circle(200)
    t.pu()
    t.goto(x+250,y+150)
    t.pd()
    t.goto(x+400,y)
    x+= 400


def R():
    t.pu()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+70,y+200)
    t.circle(100,180)
    t.goto(x,y+400)
    t.pu()
    t.goto(x,y+200)
    t.pd()
    t.goto(x+170,y)
    x+= 170

def S():
    t.pu()
    global x,y
    t.goto(x+200,y+400)
    t.pd()
    t.goto(x+100,y+400)
    t.seth(180)
    t.circle(100,180)
    t.goto(x+120,y+200)
    t.seth(0)
    t.pu()
    t.goto(x+150,y)
    t.pd()
    t.circle(100,180)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.goto(x+150,y)
    x+= 200



def T():
    t.pu()
    global x,y
    t.goto(x+100,y)
    t.pu()
    t.goto(x+100,y)
    t.pd()
    t.goto(x+100,y+400)
    t.pu()
    t.goto(x,y+400)
    t.pd()
    t.goto(x+200,y+400)
    x+= 200    

def U():
    t.pu()
    global x,y
    t.goto(x,y+400)
    t.pd()
    t.goto(x,y+100)
    t.seth(270)
    t.circle(100,180)
    t.goto(x+200,y+400)
    t.seth(0)
    x+= 200

def V():
    t.up()
    global x,y
    t.goto(x,y+400)
    t.pd()
    t.goto(x+100,y)
    t.goto(x+200,y+400)
    x+= 200


def W():
    t.up()
    global x,y
    t.goto(x,y+400)
    t.pd()
    t.goto(x+100,y)
    t.goto(x+200,y+200)
    t.goto(x+300,y)
    t.goto(x+400,y+400)
    x+= 400

def X():
    t.up()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x+200,y+400)
    t.pu()
    t.goto(x,y+400)
    t.pd()
    t.goto(x+200,y)
    x+=200

def Y():
    t.up()
    global x,y
    t.goto(x,y)
    t.pd()
    t.goto(x+200,y+400)
    t.pu()
    t.goto(x,y+400)
    t.pd()
    t.goto(x+100,y+200)
    x+=200

def Z():
    t.up()
    t.goto(x,y+400)
    t.pd()
    t.goto(x+200,y+400)
    t.goto(x,y)
    t.goto(x+200,y)

t.setworldcoordinates(-1200,-1200,1200,1200)
t.pensize(20)
t.bgcolor("#2666CF")
t.color("#F5F2E7")
A()
calC()
B()
calC()
C()
calC()
D()
calC()
E()
calC()
F()
calC()
G()
calC()
H()
calC()
I()
calC()
J()
calC()
K()
calC()
L()
calC()
M()
calC()
N()
calC()
O()
calC()
P()
calC()
Q()
calC()
R()
calC()
S()
calC()
T()
calC()
U()
calC()
V()
calC()
W()
calC()
X()
calC()
Y()
calC()
Z()
t.tracer(True)
t.exitonclick()
