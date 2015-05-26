'''
Toplevel and Tk Widgets

A Toplevel is roughly like a Frame that is split off into its own window and has additional
methods that allow you to deal with top-level window properties. 

The Tk widget is roughly like a Toplevel , but it is used to represent the application root window.

Toplevel windows have parents, but Tk windows do not—they are the true roots of the
widget hierarchies we build when making tkinter GUIs.

We got a Tk root for free in Example 8-3 because the Label had a default parent, des-
ignated by not having a widget in the first argument of its constructor call:

	Label(text='Popups').pack()		# on default Tk() root window

Passing None to a widget constructor’s first argument (or to its master keyword argu-
ment) has the same default-parent effect:

	root = Tk()
	Label(root, text='Popups').pack()		# on explicit Tk() root window
	root.mainloop()

because tkinter GUIs are a hierarchy, by default you always get at least one Tk
root window,

there may be more than one Tk root if you make them manually, and a program ends if all
its Tk windows are closed

The first Tk top-level window created—whether explicitly
by your code, or automatically by Python when needed—is used as the default parent
window of widgets and other windows if no parent is provided.

'''

import tkinter

from tkinter import Tk, Button

tkinter.NoDefaultRoot()

win1 = Tk()		# two independent root windows
win2 = Tk()

Button(win1, text='Spam', command=win1.destroy).pack()
Button(win2, text='SPAM', command=win2.destroy).pack()
# use a window’s destroy method to close just one window, instead of sys.exit to shut down the entire program

win1.mainloop()


'''
it’s more common to use the Tk root
as a main window and create Toplevel widgets for an application’s pop-up windows.
'''