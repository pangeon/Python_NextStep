import time
import functools

'''
#? Describtion
--------------
Optimalization allow executions functions in real time. No waiting too long.
 
'''

@functools.lru_cache(maxsize=100)
def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

# print(fib(1), fib(2), fib(3), fib(4), fib(5), fib(6), fib(7), fib(8))

def fib_benchmark(limit):
    start = time.time()
    for n in range(limit):
        print("n = ", n, "result = ", fib(n))
        end = time.time()
        print("time:", end - start)
    
    print("total time = ", end - start)
    return end - start
        
total_time = fib_benchmark(10000)
print(total_time) # 8.281240940093994 with cache 0.03500723838806152
print(8.281240940093994 / 0.03500723838806152)

print(fib.cache_info())


        
    
