
# POO: Common behavior ejemplo 7-19

'''
Example 7-18 standardizes behavior—it allows widgets to be configured by subclassing
instead of by passing in options. 
In fact, its HelloButton is a true button; we can pass
in configuration options such as its text as usual when one is made. 

But we can also specify callback handlers by overriding the callback method in subclasses, as shown
in Example 7-19.
'''

from gui5 import HelloButton

class MyButton(HelloButton):
	# subclass HelloButton
	def callback(self):				# redefine press-handler method / overriding the callback method in subclasses
		print("Ignoring press!...")

if __name__ == '__main__':
	MyButton(None, text='Hello subclass world').mainloop()