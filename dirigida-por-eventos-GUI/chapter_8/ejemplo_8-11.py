
# Letting users select colors on the fly


from tkinter import *
from tkinter.colorchooser import askcolor


def setBgColor():
	
	(triple, hexstr) = askcolor()

	if hexstr:
			push.config(bg=hexstr) 	#LEGB scope rule
			
	print(triple, hexstr)

root = Tk()

push = Button(root, text='Set Background Color', command=setBgColor)

push.config(height=3, font=('times', 20, 'bold'))

push.pack(expand=YES, fill=BOTH)

root.mainloop()


'''
55.3 The tkColorChooser module pag 168 libro tkinter.pdf 

http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html 

To give your application's user a popup they can use to select a color, import the tkColorChooser
module and call this function:
	result = tkColorChooser.askcolor(color, option=value, ...)

Arguments are:

color
The initial color to be displayed. The default initial color is a light gray.

title=text
The specified text appears in the pop-up window's title area. The default title is “Color”.

parent=W
Make the popup appear over window W. The default behavior is that it appears over your root
window.

If the user clicks the OK button on the pop-up, the returned value will be a tuple (triple, color),
where triple is a tuple (R, G, B) containing red, green, and blue values in the range [0,255] respect-
ively, and color is the selected color as a regular Tkinter color object.

If the users clicks Cancel, this function will return (None, None).
'''