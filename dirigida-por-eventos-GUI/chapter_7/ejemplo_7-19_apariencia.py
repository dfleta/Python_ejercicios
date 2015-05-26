
# POO: Common appearance

from tkinter import *

class ThemedButton(Button):
	# config my style too
	def __init__(self, parent=None, **configs):			# used for each instance
		Button.__init__(self, parent, **configs)		# see chapter 8 for options
		self.pack()
		self.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)

def onSpam(): print('Spam')
def onEggs(): print('Eggs')

B1 = ThemedButton(text='spam', command=onSpam)			# normal button widget objects
B2 = ThemedButton(text='eggs', command=onEggs)							# but same appearance by inheritance
B2.pack(expand=YES, fill=BOTH)

B2.mainloop()

'''
class MyButton(ThemedButton):              # subclasses inherit prefs too
    def __init__(self, parent=None, **configs):
        ThemedButton.__init__(self, parent,  **configs)
        self.config(text='subclass')

MyButton(command=onSpam)
mainloop()
'''