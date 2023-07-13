from tkinter import * 
root=Tk() 
canvas_width=700
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}") 
can_widgt=Canvas(root,width=canvas_width,height=canvas_height) 
def DDA(x1,y1,x2,y2): 
    x=x1
    y=y1
    length=(x2-x1) if (x2-x1)> (y2-y1) else(y2-y1) 
    dx=(x2-x1) / float(length) 
    dy=(y2-y1) / float(length) 
    for i in range (length): 
        x+=dx
        y+=dy
        can_widgt.create_oval(x,y,x+1,y+1) 
x1 = int(input("ENTER X1 : ")) 
y1 = int(input("ENTER Y1 : ")) 
x2 = int(input("ENTER X2 : ")) 
y2 = int(input("ENTER Y2 : ")) 
DDA(x1,y1,x2,y2) 
can_widgt.pack() 
root.mainloop() 