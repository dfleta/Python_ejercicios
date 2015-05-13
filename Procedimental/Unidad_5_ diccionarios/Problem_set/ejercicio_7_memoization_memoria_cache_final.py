
import time

def time_execution(function, inputs):
	start = time.clock()
	result = function(*inputs)
	run_time = time.clock() - start
	return result, run_time

def cached_execution(cache, funcion, input):

    if input not in cache:
        cache[input] = funcion(input)
        return cache[input]
    else:
        return cache[input]

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return cached_execution(cache, cached_fibo, (n - 1)) + cached_execution(cache, cached_fibo, (n - 2))

cache = {}
print cached_execution(cache, cached_fibo, 40)

print time_execution(cached_execution, (cache, cached_fibo, 40))




