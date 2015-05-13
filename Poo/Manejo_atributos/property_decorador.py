class Person:
	def __init__(self, name):
		self._name = name
	
	@property
	def name(self):
		"name property docs"
		print('fetch...')
		return self._name
	
	@name.setter
	def name(self, value):
		print('change...')
		self._name = value

	@name.deleter
	def name(self):
		print('remove...')
		del self._name

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)