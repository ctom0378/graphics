from tkinter import * 
root=Tk() 
canvas_width=700
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}") 
can_widgt=Canvas(root,width=canvas_width,height=canvas_height) 
can_widgt.pack() 
def bresenham(x0,y0,xn,yn): 
    x=x0
    y=y0
    dx = abs(xn - x0) 
    dy = abs(yn - y0) 
    p = 2 * dy - dx
    i=0
    while i < dx: 
        if p < 0: 
            x += 1
            p = p + 2 * dy
            can_widgt.create_oval(x,y,x+1,y+1,width=1) 
        else: 
            x += 1
            y += 1
            p = p + (2 * dy) - (2 * dx) 
            can_widgt.create_oval(x,y,x+1,y+1,width=1) 
        i += 1


x0 = int(input("enter x0 coordinate")) 
y0 = int(input("enter y0 coordinate")) 
xn = int(input("enter xn coordinate")) 
yn = int(input("enter yn coordinate")) 
bresenham(x0,y0,xn,yn) 



root.mainloop() 