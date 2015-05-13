# Extractos de codigo del libro Learning Python 5th Ed. by Mark Lutz 
# Chapter 17: Scopes

# GLOBAL SCOPE

# Global names are variables assigned at the top level of the enclosing module file.
# Global names must be declared only if they are assigned within a function.
# Global names may be referenced within a function without being declared.



X = 88 # Global X

def func():
	X = 99 # Local X: hides global, but we want this here

func()
print(X) # Prints 88: unchanged




X = 88 # Global X

def func():
	global X
	X = 99 # Global X: outside def

func()
print(X) # Prints 99




# Global names may be referenced within a function without being declared.

y, z = 1, 2

def all_global():
	global x
	x = y + z

# Global variables in module
# Declare globals assigned
# No need to declare y, z: LEGB rule

x existe ahora en el ambito global con valor 3




# NESTED SCOPES

X = 99
	def f1():
		X = 88
		def f2():
			print(X)
		f2()

f1()

# Global scope name: not used
# Enclosing def local
# Reference made in nested def
# f2 is a temporary function that lives only during the execution of (and is visible only to code in) the enclosing f1 .
# Prints 88: enclosing def local

salida: X = 88; X sigue valiendo 99; no se puede invocar a f2() desde el modulo principal




# Factory Functions: Closures

# a closure or a factory function, the former describing a functional programming technique, and the latter denoting a design pattern.
# the function object in question remembers values in enclosing scopes regardless of whether those scopes are still present in memory.

def f1():
	X = 88
	def f2():
		print(X)    # Remembers X in enclosing def scope
	return f2 	# Return f2 but don't call it => f1() devuelve el objeto funcion f2()

action = f1()       # Make, return function => action es ahora una función = f2()
action() 			# Call it now: prints 88

# This works because functions are objects in Python like everything else, and can be passed back as return values from other functions. 
# Most importantly, f2 remembers the enclosing scope’s X in f1 , even though f1 is no longer active


# Otro ejemplo:

def maker(N):
	def action(X):		# Make and return action
		return X ** N 	# action retains N from enclosing scope
	return action

>>> f = maker(2)  # Pass 2 to argument N
>>> f(3)		  # Pass 3 to X, N remembers 2: 3 ** 2
9
>>> f(4)		  # 4 ** 2
16

