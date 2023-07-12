from tkinter import * 
import math
root=Tk() 
canvas_width=700 
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}") 
can_widgt=Canvas(root,width=canvas_width,height=canvas_height) 
can_widgt.pack()
#draw polygon 
can_widgt.create_line(350,50,250,200,width=3,fill="black") 
can_widgt.create_line(350,50,450,200,width=3,fill="black") 
can_widgt.create_line(250,200,450,200,width=3,fill="black")

angle=int(input("Enter the angular value:")) 
rad=angle*(math.pi/180)

x1=(450-250)*math.cos(rad)-(200-200)*math.sin(rad)+250
y1=(450-250)*math.sin(rad)+(200-200)*math.cos(rad)+200

x2=(350-250)*math.cos(rad)-(50-200)*math.sin(rad)+250 
y2=(350-250)*math.sin(rad)+(50-200)*math.cos(rad)+200 
can_widgt.create_line(250,200,x1,y1,width=3,fill="red") 
can_widgt.create_line(x1,y1,x2,y2,width=3,fill="red") 
can_widgt.create_line(x2,y2,250,200,width=3,fill="red") 
root.mainloop()

