
# mas propiedades de config de los widgets

from tkinter import *

widget = Button(text='Spam', padx=10, pady=10)

widget.pack(padx=20, pady=20)

widget.config(cursor='hand2')
widget.config(bd=8, relief=SUNKEN)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))

mainloop()

''' 
Padding
	Extra space can be added around many widgets (e.g., buttons, labels, and text)
with the padx= N and pady= N options. Interestingly, you can set these options both
in pack calls (where it adds empty space around the widget in general) and in a
widget object itself (where it makes the widget larger).

Cursor
	A cursor option can be given to change the appearance of the mouse pointer when
it moves over the widget. For instance, cursor='gumby' changes the pointer to a
Gumby figure (the green kind). Other common cursor names used in this book
include watch , pencil , cross , and hand2.

Border and relief
	A bd= N widget option can be used to set border width, and a relief= S option can
specify a border style; S can be FLAT , SUNKEN , RAISED , GROOVE , SOLID , or RIDGE

State  (avtivar o desactivar)
	Some widgets also support the notion of a state, which impacts their appearance.
For example, a state=DISABLED option will generally stipple (gray out) a widget on
screen and make it unresponsive; NORMAL does not. Some widgets support a
READONLY state as well, which displays normally but is unresponsive to changes.

'''
