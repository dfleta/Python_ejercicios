# A “smart” and reusable Quit button

# es el ejemplo 8-7

"""
a Quit button that verifies exit requests;
to reuse, attach an instance to other GUIs, and re-pack as desired

Because it’s
a class, it can be attached and reused in any application that needs a verifying Quit
button.

"""

from tkinter import *							# get widget classes
from tkinter.messagebox import askokcancel		# get canned std dialog


class Quitter(Frame):
	# subclass our GUI
	def __init__(self, parent=None):
		# constructor method
		Frame.__init__(self, parent)
		self.pack()
		widget = Button(self, text='Quit', command=self.quit)
		widget.pack(side=LEFT, expand=YES, fill=BOTH)

	def quit(self):
		ans = askokcancel('Verify exit', "Really quit?")
		if ans: 				# salimos si la respuesta /askokcancel devuelve true
			Frame.quit(self)

if __name__ == '__main__':
	Quitter().mainloop()

