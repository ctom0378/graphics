from tkinter import * 
root=Tk() 
canvas_width=700
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}") 
can_widgt=Canvas(root,width=canvas_width,height=canvas_height) 
can_widgt.pack() 
x1=int(input("Enter the X-coordinate:")) 
y1=int(input("Enter the Y-coordinate:")) 
r=int(input("Enter the radius:")) 
def putpixel(a,b): 
    can_widgt.create_oval((x1+a),(y1+b),(x1+a+0.1),(y1+b+0.1),fill="black") 
def CirclePoints(x,y): 
    putpixel((x),(y)) 
    putpixel((x),(-y)) 
    putpixel((-x),(y)) 
    putpixel((-x),(-y)) 
    putpixel((y),(x)) 
    putpixel((y),(-x)) 
    putpixel((-y),(x)) 
    putpixel((-y),(-x)) 
def Midpoint_Circle(): 
    x=0
    y=r
    d=1-r
    CirclePoints(x,y) 
    while(y>x): 
        if(d<0): 
            d=d+2*x+3
    else: 
            d=d+2*(x-y)+5
    y=y-1
    x=x+1
    CirclePoints(x,y) 
Midpoint_Circle() 
root.mainloop() 
