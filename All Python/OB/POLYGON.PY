

import math
import turtle
th= turtle.Turtle()
turtle.setworldcoordinates(-360, -360, 360, 360)
def plot(m):
 th.pu()
 th.goto(m[0])
 th.pd()
 for i in range(len(m)):
    th.goto(m[i])
    th.write(f"{m[i]}")
    th.goto(m[0])
def printMatrix(m):
 for i in range(len(m)) :
    print(m[i])
def matrixMul(m1,m2):
 t = []
 for i in range (len(m1)) :
    t.append([0,0])
 for j in range (len(m2[0])):
    for k in range (len(m2)):
        t[i][j]+=m1[i][k]*m2[k][j]
 return t
def transform(m):
 t = []
 dx = int(input("Enter the transformation distance in x axis: "))
 dy = int(input("enter the transformation distance in y axis: "))
 for i in range (len(m)) :
    for j in range (len(m[i])):
        if j==0 :
            m[i][j] = int(m[i][j]) + dx
        elif j==1 :
            m[i][j] = int(m[i][j]) + dy
        else :
            m[i][j] = int(m[i][j]) + 0
 print("After Transltion: ")
 printMatrix(m)
 th.color('red')
 plot(m)
def rotation(m):
 T = []
 theta = int(input("Enter the angle of rotation in degree: "))
 r = [[math.cos(theta),math.sin(theta)],[(0-math.sin(theta)),math.cos(theta)]]
 print("Rotational matrix: ")
 printMatrix(r)
 T = matrixMul(m,r)
 print("After Rotation: ")
 th.color('red')
 plot(T)
 printMatrix(T)
def scale(m):
 t = []
 dx = int(input("Enter the scaling distance in x axis: "))
 dy = int(input("enter the scaling distance in y axis: "))
 s = [[dx,0],[0,dy]]
 t = matrixMul(m,s)
 print("After Scaling: ")
 th.color('red')
 plot(t)
 printMatrix(t)
def xgrids():
 th.speed(10000)
 th.pu()
 th.goto(-350, 350)
 th.color("lightgreen")
 i = 350
 x = -350
 while (i > -350):
    th.pd()
    th.goto(350, i)
    i = i - 10
    th.pu()
    th.goto(-350, i)
def ygrids():
 th.speed(10000)
 th.pu()
 th.goto(-350, 350)
 th.color("lightgreen")
 i = -350
 y = 350
 while (i < 350):
    th.pd()
    th.goto(i, -350)
    i = i + 10
    th.pu()
    th.goto(i, 350)
def x_y_axis():
 th.pu()
 th.goto(0, 350)
 th.pd()
 th.write("y", font=("Verdana", 12, "bold"))
 th.goto(0, -350)
 th.pu()
 th.goto(2,-350)
 th.pd()
 th.write("-y", font=("Verdana", 12, "bold"))
 th.pu()
 th.goto(-350, 0)
 th.pd()
 th.write("-x", font=("Verdana", 12, "bold"))
 th.goto(350, 0)
 th.write("x", font=("Verdana", 12, "bold"))
 th.goto(0, 0)
 th.write("O", font=("Verdana", 12, "bold"))
xgrids()
ygrids()
th.color("Black")
x_y_axis()
th.pu()
th.goto(0,0)
th.pd()
m = []
s = int(input("Enter the no.of sides of the polygon: "))
for i in range (s):
 x = int(input(f"Enter the x co-ordinate of point {i+1}: "))
 y = int(input(f"Enter the y co-ordinate point {i+1}: "))
 m.append([x,y])
print("1. Transltion\n2. Rotation\n3. Scaling")
ch = int(input("Enter choice: "))
if ch == 1:
 print("Before transltion: ")
 printMatrix(m)
 th.color('black')
 plot(m)
 transform(m)
elif ch == 2:
 print("Before Rotation: ")
 printMatrix(m)
 th.color('black')
 plot(m)
 rotation(m)
elif ch == 3:
 print("Before Scaling: ")
 printMatrix(m)
 th.color('black')
 plot(m)
 scale(m)
else :
 print("Wrong Input")
turtle.done()
