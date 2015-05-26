
# propiedades de config de los widgets

'''
all the buttons and labels in examples have been rendered with a default look-
and-feel that is standard for the underlying platform
'''

from tkinter import *

root = Tk()

labelfont = ('times', 20, 'bold') 	# tupla: family, size, style

widget = Label(root, text='Hello config world')

widget.config(bg='black', fg='yellow')		# yellow text on black label
widget.config(font=labelfont)				# use a larger font
widget.config(height=3, width=20)			# initial size: lines,chars	

widget.pack(expand=YES, fill=BOTH)

root.mainloop()

'''
we can call a widget’s config method to reset its options at any time, instead
of passing all of them to the object’s constructor.

Color
	These color options work on most tkinter widgets and accept either a sim-
ple color name (e.g., 'blue' ) or a hexadecimal string.

Size
	The label is given a preset size in lines high and characters wide by setting its
height and width attributes.

Font
	This script specifies a custom font for the label’s text by setting the label’s font
attribute to a three-item tuple giving the font family, size, and style
	Font style can be normal , bold , roman , italic , underline , over
strike ,or combinations of these (e.g., “bold italic”).
	tkinter guarantees that Times , Courier , and Helvetica font family names exist on all platforms,
	20-point
	Font settings like this
work on all widgets with text, such as labels, buttons, entry fields, listboxes, and
Text

Layout and expansion
	the label is made generally expandable and stretched by setting the pack
expand and fill options


'''