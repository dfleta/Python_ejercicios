
# Customizing Widgets with Classes

# You don’t have to use OOP in tkinter scripts, but it can definitely help. As we just saw,
# tkinter GUIs are built up as class-instance object trees

# OOP features can be applied to GUI models: specializing widgets by inheritance

from tkinter import *

class HelloButton(Button):
	def __init__(self, parent=None, **config):		# add callback method

		# **config recoge la configuración del botón en forma de Keyword Args.
		Button.__init__(self, parent, **config)		# and pack myself
		# Llamamamos al constructor de la superclase
		self.pack()									# could config style too
		self.config(command=self.callback)
		# al pulsar se ejecuta el método de clase callback

	def callback(self): 								# default press action
		print('Goodbye world...')						# replace in subclasses
		self.quit()

if __name__ == '__main__':
	HelloButton(text='Hello subclass world').mainloop()