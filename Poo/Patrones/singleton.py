
def singleton(claseDecorada):
	instancia = None
	def wrapper(*pargs, **kargs):
		nonlocal instancia
		if instancia == None:
			instancia = claseDecorada(*pargs, **kargs)
		return instancia
	return wrapper

@singleton
class Person:
	def __init__(self, name, hours, rate):
		self.name = name
		self.hours = hours
		self.rate = rate
	def __repr__(self):
		return "%s %d" % (self.name, self.hours)
	def pay(self):
		return self.hours * self.rate

persona_1 = Person('Basilio', 25, 5)
persona_2 = Person('Petra', 40, 8)

print(id(persona_1))
print(id(persona_2))
print(persona_2)




