
# Message

'''
The Message widget is simply a place to display text. Although the standard showinfo
dialog we met earlier is perhaps a better way to display pop-up messages, Message splits
up long strings automatically and flexibly and can be embedded inside container widg-
ets any time you need to add some read-only text to a display.
'''


from tkinter import *

msg = Message(text="Oh by the way, which one's Pink?")

msg.config(bg='pink', font=('times', 16, 'italic'))

msg.pack(fill=BOTH, expand=YES)		# BOTH para que llene de rosa todo el espacio

mainloop()