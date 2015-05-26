
'''
Top-Level Windows

tkinter GUIs always have an application root window, whether you get it by default or
create it explicitly by calling the Tk object constructor. This main root window is the
one that opens when your program runs, and it is where you generally pack your most
important and long-lived widgets. In addition, tkinter scripts can create any number
of independent windows, generated and popped up on demand, by creating Toplevel
widget objects.

Each Toplevel object created produces a new window on the display and automatically
adds it to the program’s GUI event-loop processing stream (you don’t need to call the
mainloop method of new windows to activate them).
'''

import sys
from tkinter import Toplevel, Button, Label

win1 = Toplevel()	# two independent windows
win2 = Toplevel()	# but part of same process

Button(win1, text='Spam', command=sys.exit).pack() 	# en la ventana win1
Button(win2, text='SPAM', command=sys.exit).pack()	# en la ventana win2

Label(text='Popups').pack()		# on default Tk() root window: gets a root window by default

# We got a Tk root for free because the Label had a default parent, 
# designated by not having a widget in the first argument of its constructor call
# Passing None to a widget constructor’s first argument (or to its master keyword argu-
# ment) has the same default-parent effect.

win1.mainloop()

'''
The toplevel0 script gets a root window by default (that’s what the Label is attached to,
since it doesn’t specify a real parent), but it also creates two standalone Toplevel win-
dows that appear and function independently of the root window,

The two Toplevel windows on the right are full-fledged windows; they can be inde-
pendently iconified, maximized, and so on.
	They stay up until they are explicitly destroyed or until the appli-
cation that created them exits => In fact, as coded here, pressing the X in the upper right corner of either of the
Toplevel windows kills that window only.

	It’s important to know that although Toplevel s are independently active windows, they
are not separate processes; if your program exits, all of its windows are erased, including
all Toplevel windows it may have created.

'''
