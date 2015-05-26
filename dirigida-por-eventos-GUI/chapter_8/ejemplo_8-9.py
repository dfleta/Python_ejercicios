"create a bar of simple buttons that launch dialog demos"

from tkinter import *              # get base widget set
from dialogTable import demos      # button callback handlers
from quitter import Quitter        # attach a quit object to me


class Demo(Frame):

    def __init__(self, parent=None, **options):

        Frame.__init__(self, parent, **options)

        self.pack()

        Label(self, text="Basic demos").pack()

        for (key, value) in demos.items(): # es un diccionario => los botones apareceran no siempre en e mismo orden aleatorio
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        
        # a la coleccion de botones anterior añade el boton quitter del ejemplo 8-7
        Quitter(self).pack(side=TOP, fill=BOTH)

if __name__ == '__main__': Demo().mainloop()
