import time


def get_seq(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_seq(i - 1) + get_seq(i)) / 2
        return v


def seq_print_info():    
    print(get_seq(5)) # 29.9375
    print(get_seq(4)) # 16.375
    print(get_seq(3)) # 8.75
    print(get_seq(2)) # 4.5
    print(get_seq(1)) # 2.0
    print(get_seq(0)) # 1
    

def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print("function {}, during time: {}".format(a_function.__name__, time_stop - time_start))
        return v
    
    return a_wrapped_function


wrapper_get_seq = wrapper_time(get_seq)
print("result:", wrapper_get_seq(18))





