import turtle

sougata = turtle.Turtle()
turtle.setworldcoordinates(-360, -360, 360, 360)
sougata.pu()


def plot(x,y):
    sougata.pd()
    sougata.goto(round(x,2),round(y,2))
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
sougata.goto(0,0)   # starting at the origin

# Read line end points
x0 = int(input("Enter the starting x value: "))
y0 = int(input("Enter the starting y value: "))
x_end = int(input("Enter the ending x value: "))
y_end = int(input("Enter the ending y value: "))
sougata.goto(x0,y0)         # starting point
sougata.pd()
sougata.write(f"{x0,y0}")   # marking the current points


xi, yi = x0, y0

# calculating the slope and dx, dy
dx = x_end - x0
dy = y_end - y0
m = dy/dx

# #As per algorithm
# if dx>=dy:
#     length = dx
# else:
#     length  = dy
#
# # select raster unit, doing this will make either dx=1, or dy=1
# dx = (x_end - x0) / length
# dy = (y_end - y0) / length
#
# while (xi < x_end or yi < y_end):
#     x_i = xi + 0.5 * dx
#     y_i = yi + 0.5 * dy
#     plot(x_i,y_i)
#     xi ,yi = x_i, y_i

while xi < x_end or yi < y_end:
    # we will plot until the end point is reached
    if dx >= dy:
        x_i = xi + 1
        y_i = yi + m
        plot(x_i, y_i)
        xi, yi = x_i, y_i

    elif dx < dy:
        x_i = xi + (1/m)
        y_i = yi + 1
        plot(x_i, y_i)
        xi, yi = x_i, y_i

sougata.write(f"{x_end,y_end}")
turtle.done()