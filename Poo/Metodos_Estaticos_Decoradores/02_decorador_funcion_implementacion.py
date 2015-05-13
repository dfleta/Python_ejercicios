
# IMPLEMETACION en juego: ejemplo TRACER anterior

# mas Decorator State Retention Options: options for retaining state information provided at decoration time:
# instance attributes, global variables, nonlocal closure variables, and function
# attributes can all be used for retaining state.


'''
Tracing Calls: 
To get started, let’s revive the call tracer example we met in Chapter 32. The following
defines and applies a function decorator that counts the number of calls made to the
decorated function and prints a trace message for each call:
'''

class tracer:
	
	def __init__(self, func): 		# On @ decoration: save original func
		self.calls = 0				# State via instance attributes
		self.func = func 			# Save func for later call

	def __call__(self, *args):		# On later calls: run original func
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		self.func(*args)

@tracer
def spam(a, b, c):			# spam = tracer(spam)
	print(a + b + c) 		# Wraps spam in a decorator object: Triggers tracer.__init__ !!!!!!!!!!!!

@tracer
def eggs(x, y):				# Same as: eggs = tracer(eggs)
	print(x ** y) 			# Wraps eggs in a tracer object!!!!!!!!!!!!!


spam(1, 2, 3)
# call 1 to spam
# 6 # Really calls the tracer wrapper object
spam('a', 'b', 'c')
# call 2 to spam
# abc
eggs(2, 2)
eggs(2, 3)


###################

# el codigo anterior admitiendo argumentos keyword:

class tracer:
	def __init__(self, func):	# On @ decorator
		self.calls = 0			# State via instance attributes
		self.func = func 		# Save func for later call

	def __call__(self, *args, **kwargs):	# On call to original function
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):				# Same as: spam = tracer(spam)
	print(a + b + c) 			# Triggers tracer.__init__ !!!!!!!!!!!!

@tracer
def eggs(x, y):					# Same as: eggs = tracer(eggs)
	print(x ** y) 				# Wraps eggs in a tracer object!!!!!!!!!!

spam(1, 2, 3)					# Really calls tracer instance: runs tracer.__call__
# call 1 to spam
# 6
spam(a=4, b=5, c=6) 			# spam is an instance attribute
# call 2 to spam
# 15
eggs(2, 16)						# Really calls tracer instance, self.func is eggs
# call 1 to eggs
# 65536
eggs(4, y=4) 					# self.calls is per-decoration here
# call 2 to eggs
# 256



