# Attaching Class Components

from sys import exit
from tkinter import *		# get Tk widget classes
from gui6 import Hello		# get the subframe class

parent = Frame(None)		# make a container widget

parent.pack()

Hello(parent).pack(side=RIGHT)		# attach Hello instead of running it


Button(parent, text='Attach', command=exit).pack(side=LEFT)

parent.mainloop()

'''
This script just adds Hello ’s button to the right side of parent —a container Frame . In
fact, the button on the right in this window represents an embedded component: its
button really represents an attached Python class object.

In more complex GUIs, we might instead attach large Frame subclasses to other con-
tainer components and develop each independently.
'''
