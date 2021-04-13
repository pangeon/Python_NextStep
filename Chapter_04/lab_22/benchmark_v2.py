import time
import functools

'''
# TODO: 
How print time ? 
Function takes too long
'''
def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        #? time_start = time.time()
        v = a_function(*args, **kwargs)
        #? time_stop = time.time()
        #? print("function {}, during time: {}".format(a_function.__name__, time_stop - time_start))
        return v
    
    return a_wrapped_function

@wrapper_time
def get_seq(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_seq(i - 1) + get_seq(i)) / 2
        return v


print(get_seq(18))





