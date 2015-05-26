
'''
Dialogs

Dialogs are windows popped up by a script to provide or request additional informa-
tion. They come in two flavors, modal and nonmodal:

Modal
These dialogs block the rest of the interface until the dialog window is dismissed;
users must reply to the dialog before the program continues.

Nonmodal
These dialogs can remain on-screen indefinitely without interfering with other
windows in the interface; they can usually accept inputs at any time.

Regardless of their modality, dialogs are generally implemented with the Toplevel win-
dow object we met in the prior section,

There are essentially three ways to present pop-up dialogs to users with tkinter
	by using common dialog calls, 
	by using the now-dated Dialog object, 
	and by creating custom dialog windows with Toplevel s and other kinds of widgets.

'''


# Standard (Common) Dialogs

from tkinter import *
from tkinter.messagebox import *

def callback():
	if askyesno('Verify', 'Do you really want to quit?'):
		showwarning('Yes', 'Quit not yet implemented')
	else:
		showinfo('No', 'Quit has been cancelled')


errmsg = 'Sorry, no Spam allowed!'

Button(text='Quit', command=callback).pack(fill=X)

# When you press this window’s Quit button, the dialog in Figure 8-6 is popped up by
# calling the standard askyesno function in the tkinter package’s messagebox module.

# The dialog in Figure 8-6 blocks the program until the user clicks one of its buttons; if
# the dialog’s Yes button is clicked (or the Enter key is pressed), the dialog call returns
# with a true value

Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)

# if the Spam button is clicked in the main window, the standard
# dialog is generated with the standard showerror call.

mainloop()


'''
tkinter comes with a
collection of precoded dialog windows that implement many of the most common pop
ups programs generate—file selection dialogs, error and warning pop ups, and question
and answer prompts. 
They are called standard dialogs (and sometimes common dialogs) because they are part of the tkinter library, and they use platform-specific library
calls to look like they should on each platform.

All standard dialog calls are modal (they don’t return until the dialog box is dismissed
by the user), and they block the program’s main window while they are displayed.

Scripts can customize these dialogs’ windows by passing message text, titles, and the
like.

you need to be careful not
to rely on these dialogs too much (it’s generally better to use input fields in long-lived
windows than to distract the user with pop ups).

'''

