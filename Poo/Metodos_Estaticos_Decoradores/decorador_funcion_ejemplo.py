
def truncar(funcion):			# On @ decoration
	def wrapper(*args):	# On wrapped function call
		# Use F and args
		return int( funcion(*args) )# F(*args) calls original function
	return wrapper 
	
	
@truncar				# func = decorator(func)
def division(x, y):
		return x / y	# func is passed to decorator's F

@truncar	
def suma(*pargs):
	return sum(pargs)

print(division(20, 3)) 	# 6, 7 are passed to wrapper's *args
print(suma(20, 3.5))