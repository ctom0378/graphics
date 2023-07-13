# . Write the program in python to draw the small alphabets a to z


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

def a():
    global x,y
    t.pu(); t.goto(x,y+400); t.pd(); t.goto(x+100,y+400); t.circle(-100,100);
    t.goto(x+200,y); t.goto(x+100,y); t.pu(); t.goto(x+200,y+200); t.pd();
    t.goto(x+100,y+200); t.seth(180); t.circle(100,180);
    x+= 200

def b():
    global x,y
    t.pu(); t.goto(x,y+400); t.pd(); t.goto(x,y); t.goto(x+100,y);
    t.seth(0); t.circle(100,180); t.goto(x,y+200);
    x+=200

def c():
    global x,y 
    t.pu(); t.goto(x+100,y+200); t.pd(); t.seth(180); t.circle(100,180);
    x+= 100

def d():
    global x,y
    t.pu(); t.goto(x+200,y+400); t.pd(); 
    t.goto(x+200,y); t.goto(x+100,y); t.pu(); t.goto(x+200,y+200); t.pd();
    t.goto(x+100,y+200); t.seth(180); t.circle(100,180);
    x+= 200

def e():
    global x,y
    t.pu(); t.goto(x+200,y+150); t.pd(); t.seth(90); t.circle(100,180);
    t.pu(); t.goto(x+200,y+150); t.pd(); t.goto(x,y+150); t.goto(x,y+120);
    t.seth(270); t.circle(100,90)
    x+= 200

def f():
    global x,y
    t.pu(); t.goto(x+200,y+400); t.pd(); t.goto(x+100,y+400); t.seth(180); t.circle(100,100);
    t.goto(x,y); t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+100,y+200)
    x+= 200  

def g():
    global x,y
    t.pu(); t.goto(x+200,y+300); t.pd(); 
    t.goto(x+100,y+300); t.seth(180); t.circle(100,180); t.goto(x+200,y+100); t.pu(); t.goto(x+200,y+300);
    t.pd(); t.goto(x+200,y-50); t.seth(270); t.circle(-100,100)
    x+= 200


def h():
    global x,y 
    t.pu(); t.goto(x,y+400); t.pd(); t.goto(x,y); 
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+100,y+200); 
    t.seth(0)
    t.circle(-100,100);t.goto(x+200,y)
    x+= 200

def i():
    global x,y
    t.pu(); t.goto(x+50,y); t.pd(); t.goto(x+50,y+200); t.pu(); t.goto(x+40,y+300); t.pd(); t.circle(10);
    x+= 50

def j():
    global x,y
    t.pu(); t.goto(x+50,y+200); t.pd(); t.goto(x+50,y-30); t.seth(270); t.circle(-100,100) 
    t.pu(); t.goto(x+40,y+300); t.pd(); t.circle(10);
    x+= 50

def k():
    global x,y
    t.pu(); t.goto(x,y); t.pd(); t.goto(x,y+400); t.pu(); t.goto(x,y+150); t.pd(); t.goto(x+100,y+250); t.pu();
    t.goto(x,y+150); t.pd(); t.goto(x+100,y+50);
    x+= 150
    
def l():
    global x,y
    t.pu(); t.goto(x,y); t.pd(); t.goto(x,y+400);
    x+=50

def m():
    global x,y
    t.pu(); t.goto(x,y); t.pd(); t.goto(x,y+300); t.pu(); t.goto(x+150,y); t.pd(); t.goto(x+150,y+200);
    t.pu(); t.goto(x+300,y); t.pd(); t.goto(x+300,y+200); t.seth(90); t.circle(75,180); t.seth(90); t.circle(75,180);
    x+= 300

def n():
    global x,y
    t.pu()
    t.goto(x+150,y); t.pd(); t.goto(x+150,y+200);
    t.pu(); t.goto(x+300,y); t.pd(); t.goto(x+300,y+200); t.seth(90); t.circle(75,180); t.seth(90); t.circle(75,90);
    x+= 300

def o():
    global x,y
    t.pu()
    t.goto(x+100,y); t.pd(); t.seth(0); t.circle(90);
    x+= 120

def p():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x,y); t.goto(x+100,y);
    t.seth(0); t.circle(100,180); t.goto(x,y+200); t.pu(); t.goto(x,y); t.pd(); t.goto(x,y-200)
    x+=180   

def q():
    global x,y
    t.pu(); t.goto(x+200,y); t.pd(); t.goto(x+100,y); t.seth(180); t.circle(-100,180); t.goto(x+200,y+200); t.goto(x+200,y-200);
    x+= 150


def r():
    global x,y
    t.pu()
    t.goto(x+150,y); t.pd(); t.goto(x+150,y+100);
    t.pu()
    t.goto(x+150,y+100); t.pd();
    t.seth(90); t.circle(-75,100); t.pu(); t.goto(x+150,y+100); t.pd()
    t.seth(90); t.circle(75,90);
    x+= 180

def sSmall():
    global x,y
    t.pu()
    t.goto(x+200,y+200); t.pd(); t.goto(x+50,y+200); t.seth(180); t.circle(50,180); t.pu(); t.goto(x,y); t.pd(); t.goto(x+150,y);
    t.seth(0); t.circle(50,180);t.goto(x+50,y+100)
    x+=200


def tSmall():
    global x,y
    t.pu(); t.goto(x,y+300); t.pd(); t.goto(x,y+50); t.seth(270); t.circle(80,135); t.pu(); t.goto(x,y+150); t.pd(); t.goto(x+90,y+150)
    x+= 100

def u():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x,y+50); t.seth(270); t.circle(100,180); t.goto(x+200,y+200);
    x+=200

def v():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+100,y); t.goto(x+200,y+200);
    x+= 150


def w():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+70,y); t.goto(x+140,y+100); t.goto(x+210,y); t.goto(x+280,y+200);
    x+= 200


def xSmall():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+200,y); t.pu(); t.goto(x+200,y+200); t.pd(); t.goto(x,y);
    x+= 200

def ySmall():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+100,y+100); t.pu(); t.goto(x+200,y+200); t.pd(); t.goto(x,y);
    x+= 200


def z():
    global x,y
    t.pu(); t.goto(x,y+200); t.pd(); t.goto(x+200,y+200); t.goto(x,y); t.goto(x+200,y);

t.setworldcoordinates(-1200,-1200,1200,1200)
t.pensize(20)
t.pensize(20)
t.bgcolor("#2666CF")
t.color("#F5F2E7")
a()
calC()
b()
calC()
c()
calC()
d()
calC()
e()
calC()
f()
calC()
g()
calC()
h()
calC()
i()
calC()
j()
calC()
k()
calC()
l()
calC()
m()
calC()
n()
calC()
o()
calC()
p()
calC()
q()
calC()
r()
calC()
sSmall()
calC()
tSmall()
calC()
u()
calC()
v()
calC()
w()
calC()
xSmall()
calC()
ySmall()
calC()
z()
s.tracer(True)
t.exitonclick()