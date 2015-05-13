from abc import ABCMeta, abstractmethod

# ver class interface techniques pag 876.py => delegation

class Super(metaclass=ABCMeta):
	def delegate(self):
		self.action()
	@abstractmethod
	def action(self):
		pass

class Sub(Super):
	def action(self): print('spam')


X = Sub()
X.delegate()
# spam

