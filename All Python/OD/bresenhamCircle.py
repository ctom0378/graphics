import turtle

sougata = turtle.Turtle()
turtle.setworldcoordinates(-360, -360, 360, 360)


def plot(x,y):
    sougata.pd()
    sougata.goto(x, y)
    print(f"Next Point : {round(x,2),round(y,2)}")

def xgrids():
    sougata.speed(10000)
    sougata.pu()
    sougata.goto(-350, 350)
    sougata.color("lightgreen")
    i = 350
    x = -350
    while (i > -350):
        sougata.pd()
        sougata.goto(350, i)
        i = i - 10
        sougata.pu()
        sougata.goto(-350, i)


def ygrids():
    sougata.speed(10000)
    sougata.pu()
    sougata.goto(-350, 350)
    sougata.color("lightgreen")
    i = -350
    y = 350
    while (i < 350):
        sougata.pd()
        sougata.goto(i, -350)
        i = i + 10
        sougata.pu()
        sougata.goto(i, 350)


def x_y_axis():
    sougata.pu()
    sougata.goto(0, 350)
    sougata.pd()
    sougata.write("y", font=("Verdana", 12, "bold"))
    sougata.goto(0, -350)
    sougata.pu()
    sougata.goto(2,-350)
    sougata.pd()
    sougata.write("-y", font=("Verdana", 12, "bold"))
    sougata.pu()
    sougata.goto(-350, 0)
    sougata.pd()
    sougata.write("-x", font=("Verdana", 12, "bold"))
    sougata.goto(350, 0)
    sougata.write("x", font=("Verdana", 12, "bold"))
    sougata.goto(0, 0)
    sougata.write("O", font=("Verdana", 12, "bold"))


xgrids()
ygrids()
sougata.color("Black")
x_y_axis()
sougata.pu()
sougata.goto(0,0)
sougata.pd()


r = int(input("Enter the radius: "))
xi,x1 = 0,0
yi,y1 = r,r
sougata.pu()
sougata.goto(xi,yi)

d = 3 - (2*r)

# while xi!=yi :
#     if d >= 0:
#         x1 = xi+1
#         y1 = yi-1
#         plot(x1, y1)
#         d = d + (4 * (xi - yi)) + 10
#         xi,yi = x1,y1
#
#     else:
#         x1 = xi+1
#         y1 = yi
#         plot(x1, y1)
#         d = d + (4 * xi) + 6
#         xi, yi = x1, y1

# plot(xi,yi)
while xi <= yi:
    plot(x1,y1)
    if d<0:
        d = d + (4 * xi) + 6
    else:
        d = d + (4 * (xi - yi)) + 10
        y1 -= 1
    x1 += 1
    xi,yi = x1,y1

turtle.done()