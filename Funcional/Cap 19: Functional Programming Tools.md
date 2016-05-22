Cap 19: Functional Programming Tools
====================================
> pag 574

By most definitions, today’s Python blends support for multiple programming paradigms: 

 - __procedural__ (with its basic statements), 
 - __object-oriented__ (with its classes),
 - and __functional__. For the latter of these, Python includes a set of built-ins used for functional programming—tools that apply functions to sequences and other iterables.

Python includes a set of built-ins used for functional programming—tools that apply functions to sequences and other iterables. This set includes:

 - tools that call functions on an iterable’s items ( `map`); 
 - filter out items based on a test function ( `filter`); 
 - and apply functions to pairs of items and running results ( `reduce` ).

Python’s functional programming arsenal also includes the first-class object model explored earlier, the nested scope __closures__ and anonymous function __lambdas__ we met earlier in this part of the book, the __generators__ and __comprehensions__ we’ll be expanding on in the next chapter, and perhaps the function and class __decorators__ of this book’s final part.

## Mapping Functions over Iterables: `map`

One of the more common things programs do with lists and other sequences is apply
an operation to each item and collect the results:


```python
>>> counters = [1, 2, 3, 4]
>>>
>>> updated = []
>>> for x in counters:
	...	updated.append(x + 10)		# Add 10 to each item
>>> updated
[11, 12, 13, 14]
>>> def inc(x): return x + 10 		# Function to be run
>>> list(map(inc, counters))		# Collect results
[11, 12, 13, 14]
```
    
`map` calls inc on each list item and collects all the return values into a new list.

Because `map` expects a function to be passed in and applied, it also happens to be one of the places where __lambda__ commonly appears:
```Python
>>> list(map((lambda x: x + 3), counters))		# Function expression
[4, 5, 6, 7]
```
As `map` is a built-in, it’s always available, always works the same way, and has some performance benefits (as we’ll prove in Chapter 21, it’s faster than a manually coded for loop in some usage modes).

### Multiple sequence arguments

For instance, given multiple sequence arguments, it sends items taken from sequences in parallel as distinct arguments to the function:
```Python
>>> pow(3, 4)		# 3**4
81
>>> list(map(pow, [1, 2, 3], [2, 3, 4])) 	# 1**2, 2**3, 3**4
[1, 8, 81]
```Python
With multiple sequences, `map` expects an N-argument function for N sequences. Here, the `pow` function takes two arguments on each call—one from each sequence passed to `map`.

### `Map` similar to comprehensions

The `map` call is similar to the list comprehension expressions we studied in Chapter 14 and will revisit in the next chapter from a functional perspective:
```Python
>>> list(map(inc, [1, 2, 3, 4]))
[11, 12, 13, 14]
>>> [inc(x) for x in [1, 2, 3, 4]]		# Use () parens to generate items instead
[11, 12, 13, 14]
```
In some cases, `map` may be faster to run than a list comprehension (e.g., when mapping a built-in function), and it may also require less coding.

Wrapping a comprehension in parentheses instead of square brackets creates an object that generates values on request to save memory and increase responsiveness.


## Selecting Items in Iterables: `filter`

__filter__ and __reduce__, select an iterable’s items based on a test function and apply functions to item pairs, respectively.

Because it also returns an iterable, `filter` (like `range` ) requires a list call to display all its results in 3.X.

The following `filter` call picks out items in a sequence that are greater than zero:
```Python
>>> list(range(−5, 5))
[−5, −4, −3, −2, −1, 0, 1, 2, 3, 4] 				# An iterable in 3.X

>>> list(filter((lambda x: x > 0), range(−5, 5)))	# An iterable in 3.X
[1, 2, 3, 4] 

>>> res = []
>>> for x in range(−5, 5):			# The statement equivalent
	... if x > 0:
		... res.append(x)
>>> res
[1, 2, 3, 4]
```

Also like `map`, filter can be emulated by __list comprehension__ syntax with often-simpler results (especially when it can avoid creating a new function), and with a similar __generator expression__ when delayed production of results is desired—though we’ll save the rest of this story for the next chapter:
```Python
>>> [x for x in range(−5, 5) if x > 0]		# Use () to generate items
[1, 2, 3, 4]
```
## Combining Items in Iterables: `reduce`

It accepts an iterable to process, but it’s not an iterable itself—it __returns a single result__. 

Here are two `reduce` calls that compute the sum and product of the items in a list:
```Python
>>> from functools import reduce			# Import in 3.X, not in 2.X
>>> reduce((lambda x, y: x + y), [1, 2, 3, 4])
10
>>> reduce((lambda x, y: x * y), [1, 2, 3, 4])
24
```

At each step, `reduce` passes the current sum or product, along with the next item from the list, to the passed-in `lambda` function. By default, the first item in the sequence initializes the starting value.
```Python
>>> L = [1,2,3,4]
>>> res = L[0]
>>> for x in L[1:]:
	... res = res + x
>>> res
10
```
Para usar `reduce` es necesario importar functools:

```python	
from functools import reduce
```

## Ejercicios propuestos

#### Longitud de las palabras de un string

For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".

[http://www.learnpython.org/en/List_Comprehensions](http://www.learnpython.org/en/List_Comprehensions)

```Python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
```

Solución:

```Python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
```

#### Funciones estadísticas

[Linuxtopia](http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch20s07.html)

 1. Temperature Table. Write a list comprehension that creates a list of tuples. Each tuple has two values, a temperature in Farenheit and a temperature in Celsius.
  - Create one list for Farenheit values from 0 to 100 in steps of 5 and the matching Celsius values.
  - Create another list for Celsius values from -10 to 50 in steps of 2 and the matching Farenheit values.

  Solucion:
  ```python
  farenheit = list(range(0, 101, 5))
  [ (x, (x - 32) *5/9) for x in farenheit] 


 2. Define max() and min(). Use reduce to create versions of the built-ins max and min.
 	You may find this difficult to do this with a simple lambda form. However, consider the following. We can pick a value from a tuple like this: (a,b)[0] == a, and (a,b)[1] == b. What are the values of (a,b)[a<b] and (a,b)[a>b]?

 3. Compute the Average or Mean. A number of standard descriptive statistics can be built with reduce. These include mean and standard deviation. The basic formulae are given in Chapter 13, Tuples.
 	Mean is a simple “add-reduction” of the values in a sequence divided by the length.

 4. Compute the Variance and Standard Deviation. A number of standard descriptive statistics can be built with reduce. These include mean and standard deviation. The basic formulae are given in Chapter 13, Tuples .
 The standard deviation has a number of alternative definitions. One approach is to sum the values and square this number, as well as sum the squares of each number. Summing squares can be done as a map to compute squares and then use a sum function based on reduce. Or summing squares can be done with a special reduce that both squares and sums.
 Also the standard deviation can be defined as the square root of the variance, which is computed as:
	Procedure 20.1. Variance of a sequence a
	Mean. m ← mean(a)
	Total Variance. s ← sum of (a[i] − m )2 for all i
	Average Variance. divide s by n−1
