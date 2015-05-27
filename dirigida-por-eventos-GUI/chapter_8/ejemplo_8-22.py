"create a bar of check buttons that run dialog demos"

from tkinter import *             # get base widget set
from dialogTable import demos     # get canned dialogs
from quitter import Quitter       # attach a quitter object to "me"


class Demo(Frame):

    def __init__(self, parent=None, **options):

        Frame.__init__(self, parent, **options)

        self.pack()
        self.tools()

        Label(self, text="Check demos").pack()

        self.vars = []  # coleccion de variables tkinter

        for key in demos:
            var = IntVar()
            Checkbutton(self,
                        text=key,
                        variable=var,   # asociamos la IntVar() a variable => es un 0 o 1
                        command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')   # current toggle settings: 1 or 0
            # muestra el valor de todas las variables tkinter definidas por el checkbutton
        print()

    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        # al hacer clic sobre el botón State, se ejecuta el manejador report => 
        # muestra el valor de todas las variables tkinter definidas por el checkbutton
        Quitter(frm).pack(fill=X)

if __name__ == '__main__': 

        Demo().mainloop()

'''
The indicator is the part of the checkbutton that shows its state, 
and the label is the text that appears beside it:
 The graphic above shows how checkbuttons look in the off (0) and on (1) state

You will need to create a control variable, an instance of the IntVar class, 
so your program can query and set the state of the checkbutton. 
See Section 52, “Control variables: the values behind the widgets”, below.
'''