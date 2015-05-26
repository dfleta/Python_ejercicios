
import sys

from tkinter import *

def quit():
	print('Hello, I must be going...')
	sys.exit()
	# a custom callback handler
	# kill windows and process

widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()