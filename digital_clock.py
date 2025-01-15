#!/usr/bin/env python3

from tkinter import * 
from tkinter.ttk import *
from time import strftime 

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text = string.lower())
    lbl.after(1000, time)

root = Tk() 
w = 235 
h = 40 

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight() 

x = ws - (w + 50)
y = hs - (h + 10)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

lastClickX = 0
lastClickY = 0

lbl = Label(root, font = ('calibri', 25, 'bold'), background = 'black', foreground = 'white')
lbl.pack(anchor = 'nw')

time() 

root.resizable(0,0)
root.wait_visibility(root)
root.wm_attributes('-type', 'dock')
root.wm_attributes('-alpha',0.6)
root.attributes('-topmost', True)
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)

mainloop()
