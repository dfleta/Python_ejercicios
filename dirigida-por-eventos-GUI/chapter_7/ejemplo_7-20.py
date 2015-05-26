# Reusable GUI Components with Classes

'''
Larger GUI interfaces are often built up as subclasses of Frame , with callback handlers
implemented as methods. 

This structure gives us a natural place to store information
between events: instance attributes record state. 

It also allows us to both specialize
GUIs by overriding their methods in new subclasses and attach them to larger GUI
structures to reuse them as general components.
'''

from tkinter import *

class Hello(Frame):							# an extended Frame
	def __init__(self, parent=None):
		Frame.__init__(self, parent)		# do superclass init => relación IS-A: HERENCIA
		self.pack()
		self.data = 42						# regitro de estado
		self.make_widgets()					# attach widgets to self
				
	def make_widgets(self):
		widget = Button(self, text='Hello frame world!', command=self.message)
		widget.pack(side=LEFT)
	
	def message(self):
		self.data += 1						# regitro de estado
		# self.data (a simple counter here) retains its state between presses.
		print('Hello frame world %s!' % self.data)	


if __name__ == '__main__': 
	Hello().mainloop()

	'''
	But by subclassing Frame as we’ve done here, the class becomes an enclosing context
for the GUI:
		• Widgets are added by attaching objects to self , an instance of a Frame container
		subclass (e.g., Button ).
		• Callback handlers are registered as bound methods of self , and so are routed back
		to code in the class (e.g., self.message ).
		• State information is retained between events by assigning to attributes of self,
		visible to all callback methods in the class (e.g., self.data ).
		• It’s easy to make multiple copies of such a GUI component, even within the same
		process, because each class instance is a distinct namespace.
		• Classes naturally support customization by inheritance and by composition
		attachment.
	'''