"""
use StringVar variables
lay out by columns: this might not align horizontally everywhere (see entry2)
"""

from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())     # get from var

def makeform(root, fields):
    form = Frame(root)                              # make outer frame
    left = Frame(form)                              # make two columns
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)       # grow horizontal

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)      # add to columns
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)                  # grow horizontal
        var = StringVar()
        ent.config(textvariable=var)                # link field to var
        var.set('enter here')
        variables.append(var)
    return variables

if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()

'''
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/control-variables.html 

A Tkinter control variable is a special object that acts like a regular Python variable 
in that it is a container for a value, such as a number or string.

One special quality of a control variable is that it can be shared by a number of different widgets, 
and the control variable can remember all the widgets that are currently sharing it. 

This means, in particular, that if your program stores a value v into a control variable c with its c.set(v) 
method, any widgets that are linked to that control variable are automatically updated on the screen.

Checkbuttons use a control variable to hold the current state of the checkbutton (on or off) => ejemplo 8-22

A single control variable is shared by a group of radiobuttons 
and can be used to tell which one of them is currently set. => ejemplo 8-25

Control variables hold text string for several applications. 
Normally the text displayed in an Entry widget is linked to a control variable => este ejemplo 8-20

    v = tk.DoubleVar()   # Holds a float; default value 0.0
    v = tk.IntVar()      # Holds an int; default value 0
    v = tk.StringVar()   # Holds a string; default value ''
'''
