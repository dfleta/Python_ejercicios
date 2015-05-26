# Standalone Container Classes

'''
it’s possible to reap most of the class-based
component benefits previously mentioned by creating standalone classes not derived
from tkinter Frames or other widgets.
'''

from tkinter import *

class HelloPackage: 					# not a widget subbclass
	def __init__(self, parent=None):
		self.top = Frame(parent)		# embed a Frame: es una relación HAS A / composición o agregación
		self.top.pack()
		self.data = 0
		self.make_widgets()				# attach widgets to self.top
			
	def make_widgets(self):
		Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)  # pack() en el frame, no en el self como antes
		Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)

	def message(self):
		self.data += 1
		print('Hello number', self.data)  # retencion de estado

if __name__ == '__main__': 
	HelloPackage().top.mainloop()

	'''
	Unlike before, the HelloPackage class is not itself
	a kind of Frame widget. In fact, it’s not a kind of anything— it serves only as a generator
	of namespaces for storing away real widget objects and state. Because of that, widgets
	are attached to a self.top (an embedded Frame ), not to self . Moreover, all references
	to the object as a widget must descend to the embedded frame, as in the top.main
	loop call to start the GUI at the end of the script.

	This makes for a bit more coding within the class, but it avoids potential name clashes
	with both attributes added to self by the tkinter framework and existing tkinter widget
	methods:
		I’ve never seen a real tkinter name clash in widget subclasses 
		in some 18 years of Python coding

	using standalone classes is not without other downsides!!
	Although they can generally be attached and subclassed as before, 
	they are not quite plug-and-play compatible with real widget
	objects
	'''