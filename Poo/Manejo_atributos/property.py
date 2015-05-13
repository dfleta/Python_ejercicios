
# ejemplo pag 1222 | Chapter 38: Managed Attributes

'''
The property protocol allows us to route a specific attribute’s get, set, and delete op-
erations to functions or methods we provide, enabling us to insert code to be run au-
tomatically on attribute access, intercept attribute deletions, and provide documenta-
tion for the attributes if desired.

Properties are created with the property built-in and are assigned to class attributes,
just like method functions. Accordingly, they are inherited by subclasses and instances,
like any other class attributes.

A property is created by assigning the result of a built-in function to a class attribute:
attribute = property(fget, fset, fdel, doc)
None of this built-in’s arguments are required, and all default to None if not passed.
'''

class Person:
	def __init__(self, name):
		self._name = name
	def getName(self):
		print('fetch...')
		return self._name
	def setName(self, value):
		print('change...')
		self._name = value
	def delName(self):
		print('remove...')
		del self._name

	# name es un atributo de clase. Lo estamos decorando con el operador sobrecargado property:
	name = property(getName, setName, delName, "name property docs")

bob = Person('Bob Smith') 	# bob has a managed attribute
print(bob.name)				# Runs getName
bob.name = 'Robert Smith'	# Runs setName
print(bob.name)

del bob.name 				# Runs delName
print('-'*20)
sue = Person('Sue Jones')	# sue inherits property too
print(sue.name)
print(Person.name.__doc__) 	# Or help(Person.name)