
# Cap 14: Iterations and Comprehensions 

Anytime we start thinking about performing an operation on each item in a sequence,
we’re in the realm of list comprehensions.

```Python
>>> L = [1, 2, 3, 4, 5]
>>> for i in range(len(L)):
... L[i] += 10
...
>>> L
[11, 12, 13, 14, 15]
```

```Python
>>> L = [x + 10 for x in L]
>>> L
[21, 22, 23, 24, 25]
```

Es lo mismo que:
```Python
>>> res = []
>>> for x in L:
... res.append(x + 10)
...
>>> res
[31, 32, 33, 34, 35]
```

To run the expression, Python executes an iteration across L inside the interpreter,
assigning x to each item in turn, and collects the results of running the items through
the expression on the left side. The result list we get back is exactly what the list com-
prehension says—a new list containing x + 10 , for every x in L .

__list comprehensions are more concise to write__, and because this code pattern
of building up result lists is so common in Python work

depending on your Python and code, *list comprehensions
might run much faster than manual for loop statements* (often roughly twice as fast)
because their __iterations are performed at C language speed inside the interpreter__, rather
than with manual Python code. Especially for larger data sets, there is often a major
performance advantage to using this expression.


## Extended List Comprehension Syntax

### Filter clauses: `if`

As one particularly useful extension, the `for` loop nested in a comprehension expression
can have an associated `if` clause to filter out of the result items for which the test is not
true.

#### Ejemplo: crear lista con los valores mayores que 10 de una lista dada.
```Python
>>> L = [1,7,8,9]
>>> M = [ x  for x in L if x < 5 ]
>>> M
[1]
```

### Nested loops: `for`
List comprehensions can become even more complex if we need them to for instance,
they may contain nested loops, coded as a series of `for` clauses.

```Python
>>> [x + y for x in 'abc' for y in 'lmn']
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
```

Es lo mismo que:

```Python
>>> res = []
>>> for x in 'abc':
	... for y in 'lmn':
		...res.append(x + y)
		...
>>> res
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
```

As usual in programming, if something is difficult for you to understand, it’s probably not a good idea !!!

### Tuples (pag 279)
List comprehensions can also be used to convert tuples. The following, for example,
makes a list from a tuple, adding 20 to each item along the way:
```Python
>>> T = (1, 2, 3, 4, 5)
>>> L = [x + 20 for x in T]
>>> L
[21, 22, 23, 24, 25]
```

#### Ejemplo: Crea una lista de números del 0 al 9 a partir del iterable range()
```Python
>>> L = [x for x in range(0,9)]
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```

## Dictionary comprehensions in 3.X and 2.7


### Ejemplo 1:

#### zip(*iterables)

Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element 
from each of the argument sequences or iterables. The iterator stops when 
the shortest input iterable is exhausted

[funcion zip en librería Python](https://docs.python.org/3.3/library/functions.html#zip)

```Python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]

>>> L = [ x for x in range(0,5) ]
>>> M = [ x for x in range(5,10) ]
>>> [elemento for elemento in zip(L,M) ]
[(4, 9), (4, 9), (4, 9), (4, 9), (4, 9)]

>>> list(zip(['a', 'b', 'c'], [1, 2, 3]))		# Zip together keys and values
[('a', 1), ('b', 2), ('c', 3)] 
>>> D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))	# Make a dict from zip result
>>> D
{'b': 2, 'c': 3, 'a': 1}

>>> D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
>>> D
{'b': 2, 'c': 3, 'a': 1}
```

### Ejemplo 2:
```Python
>>> D = dict.fromkeys(['a', 'b', 'c'], 0)		# Initialize dict from keys
>>> D
{'b': 0, 'c': 0, 'a': 0} 

>>> D = {k:0 for k in ['a', 'b', 'c']}			# Same, but with a comprehension
>>> D
{'b': 0, 'c': 0, 'a': 0} 

>>> D = dict.fromkeys('spam')					# Other iterables, default value
>>> D
{'s': None, 'p': None, 'a': None, 'm': None} 

>>> D = {k: None for k in 'spam'}
>>> D
{'s': None, 'p': None, 'a': None, 'm': None}
```
