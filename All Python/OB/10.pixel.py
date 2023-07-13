from tkinter import * 
root=Tk() 
canvas_width=700 
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}") 
can_widgt=Canvas(root,width=canvas_width,height=canvas_height) 
can_widgt.pack()
x=int(input("Enter pixel X-coordinate:")) 
y=int(input("Enter pixel Y-coordinate:"))

can_widgt.create_oval(x,y,(x+20),(y+20),fill="blue")
root.mainloop()

