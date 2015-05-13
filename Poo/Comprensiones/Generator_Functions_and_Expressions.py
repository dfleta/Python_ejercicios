Generator Functions and Expressions
===================================

• Generator functions (available since 2.3) are coded as normal def statements, but
use yield statements to return results one at a time, suspending and resuming their
state between each.
• Generator expressions (available since 2.4) are similar to the list comprehensions
of the prior section, but they return an object that produces results on demand
instead of building a result list.

# Generator Functions: yield Versus return

State suspension

The chief code difference between generator and normal functions is that a generator
yields a value, rather than returning one—the yield statement suspends the function
and sends a value back to the caller, but retains enough state to enable the function to
resume from where it left off. When resumed, the function continues execution im-
mediately after the last yield run. 

From the function’s perspective, this allows its code
to *produce a series of values over time, rather than computing them all at once and
sending them back in something like a list*.


Iteration protocol integration

__next__ method ( next in 2.X), which either returns the next item in the iter-
ation, or raises the special StopIteration exception to end the iteration. An iterable
object’s iterator is fetched initially with the iter built-in function,

The following code defines a
generator function that can be used to generate the squares of a series of numbers over
time:

>>> def gensquares(N):
		for i in range(N):
			yield i ** 2 	# Resume here later

>>> for i in gensquares(5):	# Resume the function
		print(i, end=' : ') # Print last yielded value
0 : 1 : 4 : 9 : 16 :

