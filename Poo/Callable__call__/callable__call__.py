
# para justificar este tema, explicar que Tkinter GUI pag 923 
# allows you to register functions as event handlers (a.k.a. callbacks)—
# when events occur, tkinter calls the registered objects.
# If you want an event handler to retain state between events, you
# can register either a class’s bound method, or an instance that conforms to the expected
# interface with __call__ .

# Ver el codigo de la pagina 923

class Callee:
	def __call__(self, *pargs, **kargs):
		print('Called:', pargs, kargs)


C = Callee()	# C es un objeto callable

print('clase Callee')

C(1, 2, 3)
# Called: (1, 2, 3) {}
C(1, 2, 3, x=4, y=5)
# Called: (1, 2, 3) {'y': 5, 'x': 4}

X = Callee()
X(1, 2)
X(1, 2, 3, 4)
X(a=1, b=2, d=4)
X(*[1, 2], **dict(c=3, d=4))
X(1, *(2,), c=3, **dict(d=4))

'''
class C:
	def __call__(self, a, b, c=5, d=6):  # Normals and defaults
		print('Called:', pargs, kargs)


class C:
	def __call__(self, *pargs, **kargs):  # Collect arbitrary arguments
		print('Called:', pargs, kargs)
'''

class C:
	def __call__(self, *pargs, d=6, **kargs): # 3.X keyword-only argument
		print('Called:', pargs, kargs, d)

# all match all the following instance calls:
print('clase C')
X = C()
X(1, 2)
X(1, 2, 3, 4)
X(a=1, b=2, d=4)
X(*[1, 2], **dict(c=3, d=4))
X(1, *(2,), c=3, **dict(d=4))
