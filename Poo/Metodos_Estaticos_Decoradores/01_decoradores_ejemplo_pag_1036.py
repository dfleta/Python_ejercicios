
class C:
	@staticmethod # Function decoration syntax
	def meth():
		...

class C:
	def meth():
		...
	meth = staticmethod(meth) # Name rebinding equivalent


# ejemplo pag 1036 = decoradores

class Spam:
	numInstances = 0
	
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	
	@staticmethod
	def printNumInstances():
		print("Number of instances created: %s" % Spam.numInstances)


a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()
# Number of instances created: 3
a.printNumInstances()
# Number of instances created: 3


############################

# ejemplo anterior reescrito con este syntactic sugar

# ya que es lo mismo que:
# def smeth(): ...
# smeth = staticmethod( smeth )

class Methods(object):			# object needed in 2.X for property setters
	def imeth(self, x):			# Normal instance method: passed a self
		print([self, x])		
	
	@staticmethod
	def smeth(x):				 # Static: no instance passed
		print([x])
	
	@classmethod
	def cmeth(cls, x):			# Class: gets class, not instance
		print([cls, x]) 
	
	@property 					# Property: computed on fetch => explicar esta propiedad mas adelante: ejemplo property.py
	def name(self):
		return 'Bob ' + self.__class__.__name__

obj = Methods()
obj.imeth(1)
# [<bothmethods_decorators.Methods object at 0x0000000002A256A0>, 1]
obj.smeth(2)
# [2]
obj.cmeth(3)
# [<class 'bothmethods_decorators.Methods'>, 3]
obj.name
# 'Bob Methods'

##############################

'''
Recall from Chapter 30 that the __call__ operator overloading method implements a
function-call interface for class instances. The following code uses this to define a call
proxy class that saves the decorated function in the instance and catches calls to the
original name. Because this is a class, it also has state information—a counter of calls
made:
'''

# The net effect is to add a layer of logic to the original function

class tracer:
	def __init__(self, func):		# Remember original, init counter
		self.calls = 0
		self.func = func
	
	def __call__(self, *args):		# On later calls: add logic, run original => el objeto que devuelve tracer es este: call()
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		return self.func(*args)

@tracer							# Same as spam = tracer(spam)
def spam(a, b, c):				# Wrap spam in a decorator object
	return a + b + c 			

print(spam(1, 2, 3))				# Really calls the tracer wrapper object
# call 1 to spam
# 6
print(spam('a', 'b', 'c')) 			# Invokes __call__ in class
# call 2 to spam ===========>>>>>>> # it also has state information—a counter of calls: 
									# Un objeto de la clase tracer se crea la primera vez que invocamos a spam() (1)
# abc								# Llamadas posteriores a spam() trabajan con este mismo objeto 


# (1) Because the spam function is run through the tracer decorator, when the original
# spam name is called it actually triggers the __call__ method in the class

# Note how the *name argument syntax is used to pack and unpack the passed-in arguments;
# because of this, this decorator can be used to wrap any function with any number of
# positional arguments.

# The net effect is to add a layer of logic to the original spam function

# Este ejemplo:
# 1. it does not handle keyword arguments
# 2. and cannot decorate class-level method functions (in short, for methods its
# __call__ would be passed a tracer instance only). 


######################################

# la TEORIA - 1. FUNCTION DECORATORS:

# they are largely just syntactic sugar that runs one function through another
# (at the end of a def statement), and rebinds the original function name to the result.

@decorator
def F(arg):
	... # Decorate function

F(99) # Call function

# es lo mismo que:
# decorator is a one-argument callable object that returns a callable object 
# with the same number of arguments as F (in not F itself)

def F(arg):
	...

F = decorator(F) # Rebind function name to decorator result

F(99) # Essentially calls decorator(F)(99)

# IMPLEMENTACION: la teoria

# A decorator itself is a callable that returns a callable:
# either a wrapper object to intercept later calls, or the original function augmented in some way

def decorator(F):
	# Process function F: save or use function F
	# Return a different callable: nested def, class with __call__, etc.
	return F

@decorator
def func(): ... 	# func = decorator(func)

F(99)

# here’s one common coding pattern that captures this idea:
# the decorator returns a wrapper that retains the original function in an enclosing scope:

def decorator(F):			# On @ decoration
	def wrapper(*args):	...	# On wrapped function call
		# Use F and args
		# F(*args) calls original function
	return wrapper 
	
	
@decorator 				# func = decorator(func)
def func(x, y):	... 	# func is passed to decorator's F
	
func(6, 7) 	# 6, 7 are passed to wrapper's *args

# y tambien de este modo podemos aplicar el decorador a lo metodos de una clase:

class C:
	@decorator
	def method(self, x, y):		# method = decorator(method)
		... 					# Rebound to simple function		

X = C()
X.method(6, 7)


# IMPLEMETACION en juego: ejemplo TRACER anterior

# ver el codigo ejemplo en el fichero 02_decorador_funcion_implementacion.py


