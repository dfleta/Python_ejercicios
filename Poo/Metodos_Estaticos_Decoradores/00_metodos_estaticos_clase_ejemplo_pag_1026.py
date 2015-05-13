

class Spam:
	
	numInstances = 0 # atributo de clase => se comparte en todas las instancias

					 # es un atributo ESTATICO!!!! (puede ser accedido sin crear una instancia el objeto)
					 # aunque realmente se accede utilizando el objeto clase "Spam" ;)
	
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	
	def printNumInstances():
		print("Number of instances created: %s" % Spam.numInstances)


a = Spam()  
b = Spam()  
c = Spam()


Spam.printNumInstances()  # # Can call functions in class in 3.X - Differs in 3.X
# Number of instances created: 3
a.printNumInstances() # Calls through instances still pass a self 

#### FALLA!!!! ####  Como solucionarlo => staticmethod

# TypeError: printNumInstances() takes 0 positional arguments but 1 was given

# calls made through an instance fail in both Pythons, because an instance is automatically passed to a method
# that does not have an argument to receive it:
# Spam.printNumInstances() - # Fails in 2.X, works in 3.X
# instance.printNumInstances() - # Fails in both 2.X and 3.X (unless static)

#################################################

#  El problema: contar instancias creadas de una clase

# si no usamos metodos estaticos, crear una instancia de una clase para averiguar
# cuantas instancias de la clase existen creara una nueva instancia :/

class Spam:
	
	numInstances = 0  # atributo de clase => se comparte en todas las instancias
	
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	
	def printNumInstances(self):
		print("Number of instances created: %s" % Spam.numInstances)   # no utilizamos self para referenciar al atributo de la clase.


a, b, c = Spam(), Spam(), Spam()

a.printNumInstances()
# Number of instances created: 3
Spam.printNumInstances(a)
# Number of instances created: 3
Spam().printNumInstances()
# Number of instances created: 4 - # But fetching counter changes counter!

###################################################

class Methods:
	
	def imeth(self, x):  	# Normal instance method: passed a self
		print([self, x])
	
	def smeth(x):			# Static: no instance passed
		print([x]) 
	
	def cmeth(cls, x):		# Class: gets class, not instance
		print([cls, x]) 
	
	smeth = staticmethod(smeth) 	# Make smeth a static method (or @: ahead)
	cmeth = classmethod(cmeth) 		# Make cmeth a class method (or @: ahead)


# 1. Instance methods
# When you call it through an instance, Python passes the instance to the first (leftmost) argument auto-
# matically; when you call it through a class, you must pass along the instance manually:

obj = Methods()  # Callable through instance or class  
obj.imeth(1)
# [<bothmethods.Methods object at 0x0000000002A15710>, 1]
Methods.imeth(obj, 2) # pasar la instancia de manera manual
# [<bothmethods.Methods object at 0x0000000002A15710>, 2]

# 2. Stattic methods:

Methods.smeth(3)	# Static method: call through class - # No instance passed or expected
# [3]				
obj.smeth(4)		# Static method: call through instance - # Instance not passed
# [4]

# 3. Class methods 
# are similar, but Python automatically passes the class (not an instance)
# in to a class method’s first (leftmost) argument, whether it is called through a class or
# an instance:

Methods.cmeth(5)	# Class method: call through class - # Becomes cmeth(Methods, 5)
# [<class 'bothmethods.Methods'>, 5]
obj.cmeth(6)		# Class method: call through instance - # Becomes cmeth(Methods, 6)
# [<class 'bothmethods.Methods'>, 6]



######################################

#  El problema revisitado: contar instancias creadas de una clase: STATIC METHOD


class Spam:
	
	numInstances = 0  
	
	def __init__(self):
		Spam.numInstances += 1
	
	def printNumInstances():	# Use static method for class data
		print("Number of instances: %s" % Spam.numInstances)  # no utilizamos self para referenciar al atributo de la clase.
	
	printNumInstances = staticmethod(printNumInstances)


a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()
# Number of instances created: 3
a.printNumInstances() # Calls through instances still pass a self - ahora NO FALLA
# Number of instances: 3

# staticmethod(printNumInstances)
# 1. it also localizes the function name in the class scope (so it won’t clash with other names
# in the module); 
# 2. moves the function code closer to where it is used (inside the class 3 statement); 
# 3. and allows subclasses to customize the static method with inheritance—a
# more convenient and powerful approach than importing functions from the files in
# which superclasses are coded:

class Other(Spam): pass

c = Other()
c.printNumInstances()		# el metodo estatico se hereda
# Number of instances: 3


class Sub(Spam):
	
	def printNumInstances():	# Override a static method
		print("Extra stuff...")
		Spam.printNumInstances() # But call back to original
	
	printNumInstances = staticmethod(printNumInstances)


###############

#  El problema revisitado: contar instancias creadas de una clase: CLASS METHOD


class Spam:

	numInstances = 0
	
	def __init__(self):
		Spam.numInstances += 1 	
	
	def printNumInstances(cls):		# Use class method instead of static
		print("Number of instances: %s" % cls.numInstances)   # ATENCION al argumento CLS

	printNumInstances = classmethod(printNumInstances)


a, b = Spam(), Spam()
a.printNumInstances()		# Passes class to first argument
# Number of instances: 2
Spam.printNumInstances()	# Also passes class to first argument
# Number of instances: 2

############## ojo con la herencia y el paso de referencia a la clase en los metodos de clase en clases heredadas

class Spam:
	numInstances = 0		# Per-class instance counters
	def count(cls):			# cls is lowest class above instance
		cls.numInstances += 1
	def __init__(self):
		self.count()		# Passes self.__class__ to count
	count = classmethod(count)
	
class Sub(Spam):
	numInstances = 0
	def __init__(self):		# Redefines __init__
		Spam.__init__(self)

class Other(Spam):
	numInstances = 0		# Inherits __init__



x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
x.numInstances, y1.numInstances, z1.numInstances
# (1, 2, 3)
Spam.numInstances, Sub.numInstances, Other.numInstances
# (1, 2, 3)


###############################################

# continua en fichero ejemplo_pag_1036.py = decoradores