CHAPTER 20: Comprehensions and Generations
==========================================

## List Comprehensions and Functional Tools

Per Python history, list comprehensions were originally inspired by a similar tool in the
functional programming language Haskell, around the time of Python 2.0. In short, list
comprehensions apply an arbitrary expression to items in an iterable, rather than applying a function. Accordingly, they can be more general tools. In later releases, the
comprehension was extended to other roles—sets, dictionaries, and even the value
generator expressions

### List Comprehensions Versus map

Python’s built-in ord function returns the integer code point of a single character
(the chr built-in is the converse—it returns the character for an integer code point).

```Python
>>> ord('s')
115
```

suppose we wish to collect the ASCII codes of all characters in an entire string.
```Python
>>> res = []
>>> for x in 'spam':
	res.append(ord(x)) 	# Manual results collection
>>> res
[115, 112, 97, 109]

>>> res = list(map(ord, 'spam'))
>>> res
[115, 112, 97, 109]
```

while `map` maps a function over an iterable, __list comprehensions map an expression over a
sequence or other iterable__:
```Python
>>> res = [ord(x) for x in 'spam']		# Apply expression to sequence (or other)
>>> res
[115, 112, 97, 109]
```
__List comprehensions collect the results of applying an arbitrary expression to an iterable
of values and return them in a new list__. Syntactically, list comprehensions are enclosed
in square brackets—to remind you that they construct lists.

List comprehensions become more convenient, though, when we wish to apply
an arbitrary expression to an iterable instead of a function:
```Python
>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
To do similar work with a map call, we would probably need to invent a little
function to implement the square operation. Because we won’t need this function else-
where, we’d typically (but not necessarily) code it inline, with a `lambda`, instead of using
a `def` statement elsewhere:
```Python
>>> list(map((lambda x: x ** 2), range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
For more advanced kinds of expressions, though, list comprehensions will
often require considerably less typing.

### Adding Tests and Nested Loops: `filter`
```Python
>>> [x for x in range(5) if x % 2 == 0]
[0, 2, 4]

>>> list(filter((lambda x: x % 2 == 0), range(5)))
[0, 2, 4]

>>> res = []
>>> for x in range(5):
		if x % 2 == 0:
			res.append(x)
>>> res
[0, 2, 4]
```
However, we can combine an `if` clause and an arbitrary expression in our list comprehension, 
to give it the effect of a `filter` and a `map`, in a single expression:
```Python
>>> [x ** 2 for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]
```
The equivalent map call would require a lot more work on our part:
```Python
>>> list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))) )
[0, 4, 16, 36, 64]
```
#### Formal comprehension syntax

**[ expression for target in iterable ]**

**[ expression for target1 in iterable1 if condition1
			 for target2 in iterable2 if condition2 ...
			 for targetN in iterableN if conditionN ]**

This same syntax is inherited by set and dictionary comprehensions as well as the
generator expressions coming up, though these use different enclosing characters (curly
braces or often-optional parentheses), and the __dictionary comprehension begins with
two expressions separated by a colon (for key and value)__.
```Python
>>> res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302]

>>> res = []
>>> for x in [0, 1, 2]:
		for y in [100, 200, 300]:
			res.append(x + y)
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302]
```
Although list comprehensions construct list results, remember that they can iterate over
any sequence or other iterable type.
```Python
>>> [x + y for x in 'spam' for y in 'SPAM']
['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM',
'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM']
```
Each `for` clause can have an associated `if` filter, no matter how deeply the loops are
nested
```Python
>>> [x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]
['sP', 'sA', 'mP', 'mA']

>>> [x + y + z 	for x in 'spam' if x in 'sm'
				for y in 'SPAM' if y in ('P', 'A')
				for z in '123' 	if z > '1']

['sP2', 'sP3', 'sA2', 'sA3', 'mP2','mP3', 'mA2', 'mA3']

>>> [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

>>> res = []
>>> for x in range(5):
		if x % 2 == 0:
			for y in range(5):
				if y % 2 == 1:
					res.append((x, y))
>>> res
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
```

### Example: List Comprehensions and Matrixes

The following, for example, defines two 3 × 3 matrixes as lists of nested lists:
```Python
>>> M = [[1, 2, 3],
		 [4, 5, 6],
		 [7, 8, 9]]

>>> N = [[2, 2, 2],
		 [3, 3, 3],
		 [4, 4, 4]]

>>> M[1]
[4, 5, 6] # Row 2

>>> M[1][2]
6 # Row 2, item 3
```
List comprehensions are powerful tools for processing such structures, though, because
they automatically scan rows and columns for us.
```Python
>>> [ row[1] for row in M ]		# Column 2
[2, 5, 8] 

>>> [ M[row][1] for row in (0, 1, 2) ]	# Using offsets
[2, 5, 8]
```
Recorrer la diagonal ppal:
```
>>> [ M[i][i] for i in range( len(M) ) ]	# Diagonals
[1, 5, 9]
```
Recorrer la diagonal inversa:
```
>>> [ M[i][len(M)-1-i] for i in range( len(M) ) ]
[3, 5, 7]
```

Changing such a matrix in place requires assignment to offsets (use range twice if shapes
differ):
```Python
>>> L = [[1, 2, 3], [4, 5, 6]]
>>> for i in range(len(L)):
		for j in range(len(L[i])):
			L[i][j] += 10			# Update in place
>>> L
[[11, 12, 13], [14, 15, 16]]

>>> [col + 10 for row in M for col in row]
[11, 12, 13, 14, 15, 16, 17, 18, 19]

>>> [ [col + 10 for col in row] for row in M]  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[[11, 12, 13], [14, 15, 16], [17, 18, 19]]
```
esta ultima list comprehension es equivalente a:
```Python
>>> res = []
>>> for row in M:
		tmp = []			# Left-nesting starts new list
		for col in row:
			tmp.append(col + 10)
		res.append(tmp)
>>> res
[[11, 12, 13], [14, 15, 16], [17, 18, 19]]
```

Finally, with a bit of creativity, we can also use list comprehensions to combine values
of multiple matrixes.
```Python
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> N
[[2, 2, 2], [3, 3, 3], [4, 4, 4]]

>>> [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[2, 4, 6, 12, 15, 18, 28, 32, 36]

>>> [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]
```
And for more fun, we can use zip to pair items to be multiplied
(and because zip is a generator of values
in 3.X, this isn’t as inefficient as it may seem):
```Python
[[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]
```

## Don’t Abuse List Comprehensions: KISS

This book demonstrates advanced comprehensions to teach, but in the real world,
using complicated and tricky code where not warranted is both bad engineering and
bad software citizenship.

programming is not about being clever and obscure—it’s about how clearly your program
communicates its purpose.
Or, to quote from Python’s import this motto:
**Simple is better than complex.**

The **“keep it simple”** rule applies here as always: _code conciseness is a much less important goal
than code readability_.

On the other hand: _performance, conciseness, expressiveness_

However, **in this case, there is currently a substantial performance advantage to the
extra complexity: based on tests run under Python today, map calls can be twice as fast
as equivalent for loops, and list comprehensions are often faster than map calls**. This
speed difference can vary per usage pattern and Python, but is generally due to the fact
that map and list comprehensions run at C language speed inside the interpreter, which
is often much faster than stepping through Python for loop bytecode within the PVM.
