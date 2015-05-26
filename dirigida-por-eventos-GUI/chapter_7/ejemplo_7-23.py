# Extending Class Components

# extendemos la clase Hello y redefinimos su comportamiento
# ver clase Hello en gui6.py o ejemplo 7-20

from tkinter import *
from gui6 import Hello

class HelloExtender(Hello):
	
	# no es necesario pack() porque se ejecuta en el constructor (iniciador) de la superclase

	def make_widgets(self): 		# extend method here
		Hello.make_widgets(self)	# ejecutamos el metodo original make_widgets para crear el boton hello
		Button(self, text='Extend', command=self.quit).pack(side=RIGHT)
		# the quit method (inherited from Hello , which inherits it from Frame)
	
	def message(self):				# redefine method here
		print('hello', self.data)

if __name__ == '__main__': 
	HelloExtender().mainloop()

	'''
	This subclass’s make_widgets method here first builds the superclass’s widgets and then
	adds a second Extend button on the right

	Because it redefines the message method, pressing the original superclass’s button on
	the left now prints a different string to stdout

	Although this example is simple, it demonstrates a technique that can be powerful in
	practice: to change a GUI’s behavior, we can write a new class that customizes its parts
	rather than changing the existing GUI code in place. The main code need be debugged
	only once and can be customized with subclasses as unique needs arise.

	The moral of this story is that tkinter GUIs can be coded without ever writing a single
	new class, but using classes to structure your GUI code makes it much more reusable
	in the long run. If done well, you can both attach already debugged components to new
	interfaces and specialize their behavior in new external subclasses as needed for custom
	requirements
	'''
