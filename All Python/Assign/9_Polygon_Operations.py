# 9.Write a python program to draw a polygon and perform the following operations:
# Rotation
# Translation
# Scaling



import turtle as t
s = t.Screen()
s.tracer(False)
def translation(x,y,X,Y):
    for i in range(len(x)):
        x[i] += X 
        y[i] += Y 

def scaling(x,y,X,Y):
    for i in range(len(x)):
        x[i] = (int)(x[i]*X) 
        y[i] = (int)(y[i]*Y) 

if __name__ == '__main__':
    t.setworldcoordinates(-700,-400,400,700)
    x = [300, -300 , -300 , 300]
    y = [100 , 100 , -100 , -100]
    t.pu()
    t.goto(x[0],y[0])
    t.pd()
    for i in range(len(x)):
        t.goto(x[i],y[i])
    t.goto(x[0],y[0])
    t.pu()
    c = input("1. Translation \n2.Scaling \nChoice : ")
    if c == '1' :
        translation(x,y,100,50)
    elif c == '2':
        scaling(x,y,1.3,1.4)
    t.goto(x[0],y[0])
    t.pd()
    for i in range(len(x)):
        t.goto(x[i],y[i])
    t.goto(x[0],y[0])
    t.pu()
    s.tracer(True)
    t.done()
