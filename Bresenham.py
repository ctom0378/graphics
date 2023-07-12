Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
... t=turtle.Turtle()
... turtle.setworldcoordinates(-360, -360, 360, 360)
... t.pu()
... def xgrids():
...  t.speed(10000)
...  t.pu()
...  t.goto(-350, 350)
...  t.color("lightgreen")
...  i=350
...  x=-350
...  while (i>-350):
...  t.pd()
...  t.goto(350, i)
...  i=i-10
...  t.pu()
...  t.goto(-350, i)
... def ygrids():
...  t.speed(10000)
...  t.pu()
...  t.goto(-350, 350)
...  t.color("lightgreen")
...  i=-350
...  y=350
...  while (i < 350):
...  t.pd()
...  t.goto(i, -350)
...  i=i+10
...  t.pu()
...  t.goto(i, 350)
... def x_y_axis():
...  t.pu()
...  t.goto(0, 350)
...  t.pd()
...  t.write("y", font=("Verdana", 12, "bold"))
...  t.goto(0, -350)
...  t.pu()
 t.goto(2,-350)
 t.pd()
 t.write("-y", font=("Verdana", 12, "bold"))
 t.pu()
 t.goto(-350, 0)
 t.pd()
 t.write("-x", font=("Verdana", 12, "bold"))
 t.goto(350, 0)
 t.write("x", font=("Verdana", 12, "bold"))
 t.goto(0, 0)
 t.write("O", font=("Verdana", 12, "bold"))
def plot(x,y):
 t.pd()
 t.goto(round(x,2),round(y,2))
 print(f"Next Point : {round(x,2),round(y,2)}")
xgrids()
ygrids()
t.color("Black")
x_y_axis()
t.pu()
t.goto(0,0)
t.pd()
x0 = int(input("Enter the starting x value: "))
y0 = int(input("Enter the starting y value: "))
x_end = int(input("Enter the ending x value: "))
y_end = int(input("Enter the ending y value: "))
xi,yi = x0,y0
dx = x_end - x0
dy = y_end - y0
m = dy/dx
p = (2*dy) - dx
t.write(f"{x0,y0}")
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
t.write(f"{x_end,y_end}")
