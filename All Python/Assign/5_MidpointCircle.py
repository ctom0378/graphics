#  Write a python program to draw a midpoint circle algorithm and Bresenham's algorithm.



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


def symmetry_points(x,y,offset):
	drawpixel(x+offset,y+offset)
	drawpixel(-x+offset,y+offset)
	drawpixel(x+offset,-y+offset)
	drawpixel(-x+offset,-y+offset)
	drawpixel(y+offset,x+offset)
	drawpixel(-y+offset,x+offset)
	drawpixel(y+offset,-x+offset)
	drawpixel(-y+offset,-x+offset)



def plotCircle(x,y,radius,offset):
	d = 5/4.0 - radius
	symmetry_points(x,y,radius+offset)
	while x < y:
		if d < 0:
			x += 1
			d += 2*x + 1
		else:
			x += 1
			y -= 1
			d += 2*(x-y) + 1
		symmetry_points(x,y,radius+offset)


def circle(radius,offset):
	x,y = 0,radius
	plotCircle(x,y,radius,offset)

def setwindowsize(x=640, y=640):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)

setwindowsize(200, 400)
circle(20,40) 
turtle.done()
