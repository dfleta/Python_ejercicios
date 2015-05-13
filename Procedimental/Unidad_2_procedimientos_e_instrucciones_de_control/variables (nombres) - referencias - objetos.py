
# Extractos de codigo del libro Learning Python 5th Ed. by Mark Lutz 
# Chapter 6: The Dynamic Typing Interlude

# Los símbolos '>>>' indican que el comando se ejecuta en el intérprete de Python.
# Es necesario eliminar los símbolos '>>>' para ejecutar el codigo desde un archivo.

# OBJETOS INMUTABLES

>>> a = 3
>>> b = a

b es 3

>>> a = 3
>>> b = a
>>> a = 'spam'

b es 3



# Los objetos integer no son mutables

>>> a = 3
>>> b = a
>>> a = a + 2

b es 3



# OBJETOS MUTABLES

>>> L = [2, 3, 4]	# A mutable object
>>> M = L			# Make a reference to the same object
>>> L[0] = 24 		# An in-place change

>>> L
[24, 3, 4]
>>> M
[24, 3, 4]



# copia de objetos en vez de referencia:

>>> L = [2, 3, 4]
>>> M = L[:]		# Make a copy of L (or list(L), copy.copy(L), etc.)
>>> L[0] = 24
>>> L
[24, 3, 4]
>>> M
[2, 3, 4]			# M is not changed



# Shared References and Equality

>>> L = [1, 2, 3]
>>> M = L 			# M and L reference the same object
>>> L == M 			# Same values => operador igualdad de valores
True
>>> L is M 			# operador identidad de objetos: compara las referencias (los punteros)
True


>>> L = [1, 2, 3]
>>> M = [1, 2, 3]	# M and L reference different objects
>>> L == M 			# Same values
True
>>> L is M 			# operador identidad de objetos: compara las referencias (los punteros)
False



# CACHE:

>>> X = 42
>>> Y = 42		# Should be two different objects
>>> X  == Y
True
>>> X is Y 		# Same object anyhow: caching at work!!!!!!!!
True

# Because small integers and strings are cached and reused, though, is tells us they reference the same single object.

# averguar el numero de refencias a un objeto:

>>> import sys
>>> sys.getrefcount(1)
647						# 647 pointers to this shared piece of memory