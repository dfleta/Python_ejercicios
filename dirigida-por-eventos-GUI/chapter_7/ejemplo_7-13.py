
import sys

from tkinter import *
# lambda generates a function 
# but contains just an expression

widget = Button(None, 
				text='Hello event world', 
				command=(lambda: print('Hello lambda world') or sys.exit()) )

'''
This code is a bit tricky because lambdas can contain only an expression; to emulate
the original script, this version uses an or operator to force two expressions to be run
'''

widget.pack()
widget.mainloop()