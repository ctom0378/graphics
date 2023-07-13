import turtle as t
tim=t.Turtle()
tim.pencolor("#0341fc")
tim.pensize(3)
tim.speed(10000)


def bresenham(x1,y1,x2, y2):
    
    x_coorinates = []
    y_coorinates = []
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)
 
    y=y1
    for x in range(x1,x2+1):
     
        print("(",x ,",",y ,")\n")
        x_coorinates.append(x)
        y_coorinates.append(y)
 
        slope_error_new =slope_error_new + m_new
 
        if (slope_error_new >= 0):
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)
    for i in range(len(x_coorinates)):
        tim.goto(x_coorinates[i],y_coorinates[i])
         
     


x1=int(input("enter the value of top left x:"))
y1=int(input("enter the value of top left y:"))
x2=int(input("enter the value of top rignt x:"))
y2=int(input("enter the value of top rignt y:"))
x3=int(input("enter the value of bottom left x:"))
y3=int(input("enter the value of bottom left y:"))
x4=int(input("enter the value of bottom rignt x:"))
y4=int(input("enter the value of bottom rignt y:"))
tim.pu()
tim.goto(x1,y1)
tim.pd()
# bresenham(x1,y1,x2,y2)
bresenham(x2,y2,x4,y4)
# bresenham(x4,y4,x3,y3)
# bresenham(x3,y3,x1,y1)
screen=t.Screen()
screen.exitonclick()















