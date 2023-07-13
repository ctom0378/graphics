# 13. Write a python program to draw a pixel(x,y) and display the color in which
# pixel(x,y) is illuminated on the screen.


import turtle as turtle
def drawpixel(x, y, pixelsize = 5 ):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x*pixelsize,y*pixelsize)
    turtle.color("red")
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()
    turtle.done()


if __name__ == '__main__':
    drawpixel(20,0)