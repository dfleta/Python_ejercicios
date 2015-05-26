import sys
from tkinter import *

makemodal = (len(sys.argv) > 1)

# parametros en linea de comandos al invocar el programa

# If it is run with no command-line arguments, it picks nonmodal style,

def dialog():
	
	win = Toplevel()										# make a new window
	
	Label(win, text='Hard drive reformatted!').pack()		# add a few widgets
	
	Button(win, text='OK', command=win.destroy).pack()		# set destroy callback
	
	if makemodal:
		win.focus_set()					# take over input focus,
		win.grab_set()					# disable other windows while I'm open,
		win.wait_window()				# and wait here until win destroyed

	print('dialog exit')				# else returns right away


root = Tk()

Button(root, text='popup', command=dialog).pack()

root.mainloop()

'''
nonmodal:
Because dialogs are nonmodal in this mode, the
root window remains active after a dialog is popped up. In fact, nonmodal dialogs never
block other windows, so you can keep pressing the root’s button to generate as many
copies of the pop-up window as will fit on your screen.

Making custom dialogs modal:

The secret
to locking other windows and waiting for a reply boils down to three lines of code,
which are a general pattern repeated in most custom modal dialogs:

win.focus_set()
	Makes the window take over the application’s input focus, as if it had been clicked
with the mouse to make it the active window. This method is also known by the
synonym focus

win.grab_set()
	Disables all other windows in the application until this one is destroyed. The user
cannot interact with other windows in the program while a grab is set.

win.wait_window()
	Pauses the caller until the win widget is destroyed, but keeps the main event-
processing loop ( mainloop ) active during the pause. 
	That means that the GUI at large remains active during the wait; its windows redraw themselves if covered and
uncovered, for example. 
	When the window is destroyed with the destroy method,
it is erased from the screen, the application grab is automatically released, and this
method call finally returns. ====>>>>>>
	
		Because the script waits for a window destroy event, it must also arrange for a callback
handler to destroy the window in response to interaction with widgets in the dialog
window (the only window active).
'''