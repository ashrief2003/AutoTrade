#meant for visual display from the software part && works as well as abstraction for this core

from tkinter import *

class Vector:
    def __init__(x,y):
        self.x = x
        self.y = y




##window related

def CreateWindow(title,x,y):
    op = Tk()
    op.title(title)
    op.geometry(f"{x}x{y}")
    return op

def LoopWindow(window):
    window.mainloop()




#create elements

def pack_element(element):
    element.pack()

def new_canves(parent,x,y):
    return Canvas(parent,width=x,height=y,bg="white")

def drawLine(parent,x1,y1,x2,y2,size):
    return parent.create_line(x1,y1,x2,y2,width=size,fill="black") #returns the element id

def new_button(parent,txt,x,y,fun):
    return Button(parent, text = txt, command = fun, bg = "yellow")  

#edit element

def edit_line(parent,id,x1,y1,x2,y2):
    parent.coords(id,x1,y1,x2,y2)
    parent.update()



#change canvas position

def change_position(canvas,x,y):
    canvas.place(x=x, y=y)
    #canvas.pack(padx=x, pady=y)
    


# def create

# our_canvas=Canvas(root,width=300,height=200,bg="white")
# our_canvas.pack()
# #creating rectangle
# our_canvas.create_line(15, 25, 200, 25)
# #our_canvas.create_rectangle(50,150,250,50,fill="blue")
# root.mainloop()