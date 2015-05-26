
"""
pop up three new windows, with style
destroy() kills one window, quit() kills all windows and app (ends mainloop);
top-level windows have title, icon, iconify/deiconify and protocol for wm events;
there always is an application root window, whether by default or created as an
explicit Tk() object; all top-level windows are containers, but they are never
packed/gridded; Toplevel is like Frame, but a new window, and can have a menu;

This program adds widgets to the Tk root window, immediately pops up three
Toplevel windows with attached buttons, and uses special top-level protocols
"""



from tkinter import *

root = Tk()				# explicit root

trees = [('The Larch!', 'light blue'),
		 ('The Pine!',	'light green'),
		 ('The Giant Redwood!', 'red')]

for (tree, color) in trees:

	win = Toplevel(root)		# new window: TOPLEVEL
	win.title('Sing...')
	win.protocol('WM_DELETE_WINDOW', lambda:None)	# ignore close

	# win.iconbitmap('py-blue-trans-out.ico')			# not red Tk => la extension ico es para en windows
														# camabia el icono de la ventana

	msg = Button(win, text=tree, command=win.destroy)			# kills one win
	msg.pack(expand=YES, fill=BOTH)
	msg.config(padx=10, pady=10, bd=10, relief=RAISED)
	msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))


root.title('Lumberjack demo')

Label(root, text='Main window', width=30).pack()

Button(root, text='Quit All', command=root.quit).pack() 		# kills all app

root.mainloop()

'''

Most top-level window-manager-related methods can also be named with a “wm_” at
the front;

Intercepting closes: protocol
	Because the window manager close event has been intercepted by this script using
	the top-level widget protocol method, pressing the X in the top-right corner doesn’t
	do anything in the three Toplevel pop ups. The name string WM_DELETE_WINDOW
	identifies the close operation

Killing one window (and its children): destroy

	Pressing the big black buttons in any one of the three pop ups kills that pop up
only, because the pop up runs the widget destroy method. The other windows live
on, much as you would expect of a pop-up dialog window. Technically, this call
destroys the subject widget and any other widgets for which it is a parent. 
	For windows, this includes all their content. 
	For simpler widgets, the widget is erased.

	Since Tk root
windows have no parents, they are unaffected by destroys of other windows.
Moreover, destroying the last Tk root window remaining (or the only Tk root cre-
ated) effectively ends the program


	Toplevel windows, however, are always de-
stroyed with their parents, and their destruction doesn’t impact other windows to
which they are not ancestors. This makes them ideal for pop-up dialogs.

Killing all windows: quit
	To kill all the windows at once and end the GUI application (really, its active
mainloop call), the root window’s button runs the quit method instead.
	It can be called
through any tkinter widget, not just through the top-level window; it’s also avail-
able on frames, buttons, and so on.

Window titles: title
	As introduced in Chapter 7, top-level window widgets ( Tk and Toplevel ) have a
title method that lets you change the text displayed on the top border

Window icons: iconbitmap
	The iconbitmap method changes a top-level window’s icon. It accepts an icon or
bitmap file and uses it for the window’s icon graphic when it is both minimized
and open. On Windows, pass in the name of a .ico file On other platforms, you may need to use other icon file conventions
	icons tend to be a platform-specific feature that is dependent upon the underlying window manager.

Geometry management
	Top-level windows are containers for other widgets, much like a standalone
Frame . Unlike frames, though, top-level window widgets are never themselves
packed (or gridded, or placed). To embed widgets, this script passes its windows
as parent arguments to label and button constructors.
	It is generally easier and more user-friendly to let tkinter (or your users) work out
window size for you,

---------------------------
Chapter 9:
Menus
Each top-level window can have its own window menus too; both the Tk and the
Toplevel widgets have a menu option used to associate a horizontal menu bar of
pull-down option lists.

State

'''