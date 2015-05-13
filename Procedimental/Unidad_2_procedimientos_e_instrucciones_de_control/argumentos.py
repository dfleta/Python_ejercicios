
# Extractos de codigo del libro Learning Python 5th Ed. by Mark Lutz 
# Chapter 18: Arguments

# Extractos de codigo del libro Learning Python 5th Ed. by Mark Lutz 
# Chapter 18: Arguments

# Los símbolos '>>>' indican que el comando se ejecuta en el intérprete de Python.
# Es necesario eliminar los símbolos '>>>' para ejecutar el codigo desde un archivo.


--------------------------------------

# 1. Arguments and Shared References


# Paso de objetos inmutables:

>>> def f(a):	# a is assigned to (references) the passed object
		a = 99 	# Changes local variable a only

>>> b = 88		
>>> f(b)		# a and b both reference same 88 initially
>>> print(b)	# b is not changed
88


# Paso de objetos mutables:

>>> def changer(a, b):	# Arguments assigned references to objects
		a = 2			# Changes local name's value only
		b[0] = 'spam' 	# Changes shared object in place	
					
>>> X = 1
>>> L = [1, 2]
>>> changer(X, L) # Caller: Pass immutable and mutable objects
>>> L
['spam', 2]  # X is unchanged, L is different!



# Evitar que una routina modifique los elementos mutables:

# Opción 1:

L = [1, 2]
changer(X, L[:]) 	# Pass a copy, so our 'L' does not change 

# Opción 2

def changer(a, b):
	b = b[:]		# Copy input list so we don't impact caller
	a = 2
	b[0] = 'spam'	# Changes our list copy only


# Opción 3: convert to immutable objects:

L = [1, 2]
changer(X, tuple(L))	# Pass a tuple, so changes are errors



--------------------------------------

# Special Argument-Matching Modes

# ver figura 06 en Drive

Be careful not to confuse the special name=value syntax in a function header and a
function call; in the call it means a match-by-name keyword argument, while in the
header it specifies a default for an optional argument.


# Keyword and Default Examples



# 1. Por defecto:

>>> def f(a, b, c): 
		print(a, b, c)

>>> f(1, 2, 3)
1 2 3




# 2. Keywords

>>> f(c=3, b=2, a=1)
1 2 3

# left-to-right order of the arguments no longer matters when keywords are used 
# because arguments are matched by name, not by position

 
>>> f(1, c=3, b=2)		# a gets 1 by position, b and c passed by name
1 2 3

# they make your calls a bit more self documenting
>>> func(name='Bob', age=40, job='dev')




# 3. Defaults

# defaults allow us to make selected function arguments optional; 
# if not passed a value, the argument is assigned its default before the function runs.

>>> def f(a, b=2, c=3): 	# a required, b and c optional
	print(a, b, c)


>>> f(1)
1 2 3
>>> f(a=1)
1 2 3


# If we pass two values, only c gets its default, and with three values, no defaults are used:

>>> f(1, 4)
1 4 3
>>> f(1, 4, 5)	# Override defaults
1 4 5

>>> f(1, c=6)	# Choose defaults
1 2 6



# 4. Combining keywords and defaults

def func(spam, eggs, toast=0, ham=0):
	print((spam, eggs, toast, ham)) 	# First 2 required

>>> func(1, 2)							# Output: (1, 2, 0, 0)
>>> func(1, ham=1, eggs=0)				# Output: (1, 0, 0, 1)
>>> func(spam=1, eggs=0)				# Output: (1, 0, 0, 0)
>>> func(toast=1, eggs=2, spam=3)		# Output: (3, 2, 1, 0)
>>> func(1, 2, 3, 4) 					# Output: (1, 2, 3, 4)

# Notice again that when keyword arguments are used in the call, the order in which the
# arguments are listed doesn’t matter; Python matches by name, not by position. The
# caller must supply values for spam and eggs , but they can be matched by position or by name




# 5. Python 3.X Keyword-Only Arguments

# We can also use a * character by itself in the arguments list to indicate that a function
# does not accept a variable-length argument list but still expects all arguments following
# the * to be passed as keywords.

>>> def kwonly(a, *b, c):
		print(a, b, c)

>>> kwonly(1, 2, c=3)
1 (2,) 3

>>> kwonly(a=1, c=3)
1 () 3

>>> kwonly(1, 2, 3)
TypeError: kwonly() missing 1 required keyword-only argument: 'c'


# You can still use defaults for keyword-only arguments, even though they appear after
# the * in the function header

>>> def kwonly(a, *, b='spam', c='ham'):
	print(a, b, c)

>>> kwonly(1)
1 spam ham
>>> kwonly(1, c=3)
1 spam 3
>>> kwonly(a=1)
1 spam ham
>>> kwonly(c=3, b=2, a=1)
1 2 3
>>> kwonly(1, 2)
TypeError: kwonly() takes 1 positional argument but 2 were given



>>> def kwonly(a, *, b, c='spam'):
print(a, b, c)

>>> kwonly(1, c='eggs')
TypeError: kwonly() missing 1 required keyword-only argument: 'b'


