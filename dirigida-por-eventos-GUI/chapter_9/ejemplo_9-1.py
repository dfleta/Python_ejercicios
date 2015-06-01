# Tk8.0 style top-level window menus

from tkinter import *                              # get widget classes
from tkinter.messagebox import *                   # get standard dialogs

def notdone():
    showerror('Not implemented', 'Not yet available')


def makemenu(win):      # recibe una referencia a la ventana Tk() o a una topLevel

    top = Menu(win)                                # win=top-level window

    # A menubutton is the part that always appears on the application.
    # A menu is the list of choices that appears only after the user clicks on the menubutton.


    win.config(menu=top)                           # set its menu option
    # To provide this window with a top-level menubar, supply a Menu widget as the value of this option


    # menu File => la etiqueta se especifica al final, en add_cascade()
    
    file = Menu(top)    # make a new Menu [1] as the child of the topmost Menu

    file.add_command(label='New...',  command=notdone,  underline=0) # Creamos un item en el menu
    # Add a new command as the next available choice in self
    # Use the label, bitmap, or image option to place text or an image on the menu; 
    # use the command option to connect this choice to a procedure that will be called when this choice is picked.

    file.add_command(label='Open...', command=notdone,  underline=0)
    file.add_command(label='Quit',    command=win.quit, underline=0)

    # add the child menu [1] as a cascade of the topmost Menu using add_cascade
    top.add_cascade(label='File',     menu=file,        underline=0)

        # menu=file => This option is used only for cascade choices. 
        # Set it to a Menu object that displays the next level of choices.


    # menu Edit

    edit = Menu(top, tearoff=False)
    # The Unix version of Tkinter (at least) supports “tear-off menus.” 
    # If you as the designer wish it, a dotted line will appear above the choices. 
    # The user can click on this line to “tear off” the menu: 
    # a new, separate, independent window appears containing the choices.

    # The first position (position 0) in the list of choices is occupied by the tear-off element, 
    # and the additional choices are added starting at position 1. 
    # If you set tearoff=0, the menu will not have a tear-off feature, 
    # and choices will be added starting at position 0.

    edit.add_command(label='Cut',     command=notdone,  underline=0)
    edit.add_command(label='Paste',   command=notdone,  underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit',     menu=edit,        underline=0)

    # submenu del menu edit
    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone,  underline=0)
    edit.add_cascade(label='Stuff',   menu=submenu,     underline=0)

if __name__ == '__main__':
    root = Tk()                                        # or Toplevel()
    root.title('menu_win')                             # set window-mgr info
    makemenu(root)                                     # associate a menu bar
    msg = Label(root, text='Window menu basics')       # add something below
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
