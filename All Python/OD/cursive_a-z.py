import turtle as t
s = t.Screen()
s.tracer(False)
def calCor():
    global x,y
    if x>720 :
        x = -750
        y -= 200



def a():
    global x,y
    t.pu()
    t.goto(x+100,y+65)
    t.pd()
    t.goto(x+100,y+50)
    t.seth(270)
    t.circle(-50,180)
    t.goto(x,y+65)
    t.seth(90)
    t.circle(-50,180)
    t.seth(270)
    t.circle(50,70)
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    x+= 220
    calCor()

def b():
    global x,y
    t.pu()
    t.goto(x,y+50)
    t.pd()
    t.seth(270)
    t.circle(50,250)
    t.seth(180)
    t.circle(10,180)
    t.goto(x+120,y+80)
    t.pu()
    t.goto(x,y+50)
    t.pd()
    t.goto(x,y+150)
    t.pu()
    t.goto(x,y+50)
    t.pd()
    t.seth(270)
    t.circle(-50,90)
    t.pu()
    t.goto(x,y+50)
    t.pd()
    t.goto(x+20,y+150)
    t.seth(90)
    t.circle(10,180)
    x+=170
    calCor()

def c():
    global x,y
    t.pu()
    t.goto(x+50,y+100)
    t.pd()
    t.seth(180)
    t.circle(50,180)
    t.seth(0)
    t.circle(30,90)
    t.pu()
    t.goto(x-50,y)
    t.pd() 
    t.seth(0)
    t.circle(50,90)
    x+=150
    calCor()

def d():
    global x,y
    t.pu()
    t.goto(x+100,y+50)
    t.pd()
    t.seth(270)
    t.circle(-50,360)
    t.goto(x+100,y+150)
    t.seth(90)
    t.circle(10,180)
    t.goto(x+100,y+50)
    t.seth(270)
    t.circle(50,90)
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    x+=220

def e():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(100,45)
    t.goto(x+50,y+50)
    t.circle(20,180)
    t.circle(50,200)
    x+=170
    calCor()

def f():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.seth(0)
    t.pd()
    t.circle(50,90)
    t.goto(x+20,y+150)
    t.seth(90)
    t.circle(10,180)
    t.goto(x,y+20)
    t.seth(270)
    t.circle(20,200)
    t.goto(x,y+60)
    t.goto(x+50,y+60)
    x+=100
    calCor()

def g():
    global x,y
    t.pu()
    t.goto(x-30,y)
    t.seth(0)
    t.pd()
    t.circle(30,90)
    t.pu()
    t.goto(x+30,y+60)
    t.pd()
    t.seth(180)
    t.circle(30)
    t.pu()
    t.goto(x+60,y+30)
    t.pd()
    t.goto(x+60 , y -40)
    t.seth(270)
    t.circle(-20,180)
    t.circle(-10,30)
    t.goto(x+80,y+20)
    x += 150
    calCor()

def h():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.goto(x+20,y+150)
    t.seth(90)
    t.circle(10,180)
    t.goto(x,y)
    t.goto(x,y+25)
    t.seth(90)
    t.circle(-25,180)
    t.goto(x+50,y+10)
    t.seth(270)
    t.circle(10,180)
    x+=150
    calCor()

def i():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.pd()
    t.circle(50,90)
    t.seth(270)
    t.circle(50,90)
    t.pu()
    t.goto(x,y+70)
    t.seth(0)
    t.pd()
    t.circle(10)
    x+=150
    calCor()

def j():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(0)
    t.pd()
    t.circle(50,90)
    t.pd()
    t.goto(x +50 , y -40)
    t.seth(270)
    t.circle(-20,180)
    t.circle(-10,30)
    t.goto(x+70,y+20)
    t.pu()
    t.goto(x +50,y+70)
    t.seth(0)
    t.pd()
    t.circle(10)
    x+=150
    calCor()

def k():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.goto(x+20,y+130)
    t.seth(90)
    t.circle(10,180)
    t.goto(x,y)
    t.goto(x,y+25)
    t.goto(x+50,y+50)
    t.seth(45)
    t.circle(10,180)
    t.goto(x,y+25)
    t.goto(x+50,y)
    x+=150
    calCor()

def l():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.goto(x+20,y+130)
    t.seth(90)
    t.circle(15,180)
    t.goto(x,y+50)
    t.seth(270)
    t.circle(50,90)
    x+=150
    calCor()

def m():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.seth(90)
    t.circle(-25,180)
    t.goto(x+50,y)
    t.goto(x+50,y+50)
    t.seth(90)
    t.circle(-25,180)
    t.goto(x+100,y)
    t.goto(x+100,y+50)
    t.seth(90)
    t.circle(-25,180)
    t.goto(x+150,y+10)
    t.seth(270)
    t.circle(10,180)
    x+=250
    calCor()

def n():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.seth(90)
    t.circle(-25,180)
    t.goto(x+50,y)
    t.goto(x+50,y+50)
    t.seth(90)
    t.circle(-25,180)
    t.goto(x+100,y+10)
    t.seth(270)
    t.circle(10,180)
    x+=150
    calCor()

def o():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(0)
    t.circle(50,80)
    t.circle(-40)
    x+=150
    calCor()
    

def p():
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(0)
    t.circle(50,80)
    t.circle(-40)
    t.goto(x+50,y-70)
    x+=160
    calCor()


def q():
    global x,y
    t.pu()
    t.goto(x+140,y)
    t.pd()
    t.seth(180)
    t.circle(-50,80)
    t.circle(40)
    t.goto(x+90,y-60)
    t.seth(270)
    t.circle(15,180)
    t.goto(x+90,y+20)
    x+=160
    calCor()


def r():   
    global x,y
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(0)
    t.circle(50,80)
    t.goto(x+50,y+50)
    t.goto(x+80,y+50)
    t.goto(x+80,y+10)
    t.seth(270)
    t.circle(10,180)
    x+=200
    calCor()

def sA():
    global x,y
    t.pu()
    t.goto(x-30,y)
    t.pd()
    t.seth(0)
    t.circle(30,50)
    t.goto(x+30,y+50)
    t.circle(10,310)
    t.goto(x+55,y+25)
    t.seth(270)
    t.circle(-20,180)
    x+=150
    calCor()

def tA():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.goto(x+20,y+130)
    t.seth(90)
    t.circle(15,180)
    t.goto(x,y+50)
    t.seth(270)
    t.circle(50,90)
    t.pu()
    t.goto(x+30,y+70)
    t.pd()
    t.goto(x-30,y+70)
    x+=150
    calCor() 

def u():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.goto(x,y+20)
    t.seth(270)
    t.circle(20,180)
    t.goto(x+40,y+50)
    t.goto(x+40,y+30)
    t.seth(270)
    t.circle(30,60)
    x+=150

def v():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.seth(90)
    t.circle(-5,150)
    t.goto(x+35,y)
    t.goto(x+65,y+50)
    t.seth(45)
    t.circle(5,300)
    t.goto(x+75,y+35)
    x+=150
    calCor()

def w():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.seth(90)
    t.circle(-5,150)
    t.goto(x+35,y)
    t.goto(x+65,y+25)
    t.seth(45)
    t.circle(5,300)
    t.goto(x+85,y)
    t.goto(x+100,y+50)
    t.seth(45)
    t.circle(5,300)
    t.goto(x+110,y+40)
    x+= 200
    calCor()

def xA():
    global x,y
    t.pu()
    t.goto(x-50,y+5)
    t.pd()
    t.seth(270)
    t.circle(5,150)
    t.goto(x,y+50)
    t.seth(45)
    t.circle(5,300)
    t.goto(x+50,y)
    t.seth(-45)
    t.circle(5,300)
    t.goto(x+40,y)
    t.pu()
    t.goto(x+50,y+50)
    t.pd()
    t.goto(x,y)
    x+=150



def yA():
    global x,y
    t.pu()
    t.goto(x-50,y)
    t.pd()
    t.seth(0)
    t.circle(50,90)
    t.goto(x,y+20)
    t.seth(270)
    t.circle(20,180)
    t.goto(x+40,y+50)
    t.goto(x+40,y+30)
    t.goto(x+40,y-70)
    t.seth(270)
    t.circle(-15,190)
    t.goto(x+40,y+30)
    x+=150
    calCor()

def z():
    global x,y
    t.pu()
    t.goto(x-50,y+30)
    t.pd()
    t.seth(180)
    t.circle(-10,180)
    t.goto(x+30,y+50)
    t.goto(x-50,y)
    t.goto(x+30,y)
    t.seth(0)
    t.circle(10,180)




if __name__ == '__main__':
    t.setworldcoordinates(-800,-450,600,450)
    t.pensize(3)
    global x,y
    x = -750
    y = 350
    a()
    b()
    c()
    d()
    e()
    f()
    g()
    h()
    i()
    j()
    k()
    l()
    m()
    n()
    o()
    p()
    q()
    r()
    sA()
    tA()
    u()
    v()
    w()
    xA()
    yA()
    z()
    t.hideturtle()
    s.tracer(True)
    t.done()

