"""
use Entry widgets directly
lay out by rows with fixed-width labels: this and grid are best for forms
"""

from tkinter import *
from quitter import Quitter


def fetch(entries):                                 # recibe los entry y mueestra su valor
    for entry in entries:
        print('Input => "%s"' % entry.get())        # get text

def makeform(root, fields):
    entries = []
    for field in fields:
        # ponemos cada entry en una frame llamado row: el formulario está compuesto de filas = frames
        row = Frame(root)                           # make a new row
        # A frame is basically just a container for other widgets.
        # Este contiene una label con field y un entry
        lab = Label(row, width=5, text=field)       # add label, entry
        ent = Entry(row)
        row.pack(side=TOP, fill=X)                  # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
        entries.append(ent)
    return entries



if __name__ == '__main__':

    fields = 'Name', 'Job', 'Pay'

    root = Tk()

    ents = makeform(root, fields)   # lista con todos los entry

    root.bind('<Return>', (lambda event: fetch(ents)))  
    # cada vez que pulsamos return en el formulario, en consola se muestra el valor de los entry(s) 

    Button(root, text='Fetch',
                 command= (lambda: fetch(ents))).pack(side=LEFT)    # mostrar todos los entries

    # reutilizamos nuestro botón con cuadro de diálogo para abandonar el programa
    Quitter(root).pack(side=RIGHT)

    root.mainloop()

'''
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/frame.html 

A frame is basically just a container for other widgets.

Your application's root window is basically a frame.

Each frame has its own grid layout, so the gridding of widgets within each frame works independently.

Frame widgets are a valuable tool in making your application modular. 
You can group a set of related widgets into a compound widget by putting them into a frame. 
'''