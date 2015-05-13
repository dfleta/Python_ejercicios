
import time


def time_execution(function, inputs):
	start = time.clock()
	result = function(inputs)
	run_time = time.clock() - start
	return result, run_time

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return cached_fibo(n - 1) + cached_fibo(n - 2)

print time_execution(cached_fibo, 40)

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

# print time_execution(factorial, 800)


