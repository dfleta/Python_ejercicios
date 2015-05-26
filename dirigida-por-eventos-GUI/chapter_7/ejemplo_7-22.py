# Attaching Class Components

'''
Igual que el ejemplo 7-21 pero en un estilo más orientado a objetos

Example 7-22 is yet
another specialized Frame itself, but it attaches an instance of the original Hello class in
a more object-oriented fashion.
'''

from tkinter import *			# get Tk widget classes

from gui6 import Hello 			# get the subframe class

class HelloContainer(Frame):
	
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		self.makeWidgets()
	
	def makeWidgets(self):
		Hello(self).pack(side=RIGHT) 	# attach a Hello to me
		Button(self, text='Attach', command=self.quit).pack(side=LEFT)

if __name__ == '__main__': 
	HelloContainer().mainloop()


	'''
	This looks and works exactly like gui6b but registers the added button’s callback han-
	dler as self.quit , which is just the standard quit widget method this class inherits from
	Frame . The window this time represents two Python classes at work—the embedded
	component’s widgets on the right (the original Hello button) and the container’s
	widgets on the left.

	But in more practical user interfaces, the set of widget class objects attached in this way
	can be much larger. If you imagine replacing the Hello call in this script with a call to
	attach an already coded and fully debugged calculator object, you’ll begin to better
	understand the power of this paradigm. If we code all of our GUI components as classes,
	they automatically become a library of reusable widgets, which we can combine in other
	applications as often as we like.
	'''

