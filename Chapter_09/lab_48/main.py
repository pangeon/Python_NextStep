import itertools
import operator

def get_factors(x):
    
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)

    return ret_list

def check_if_has_dividers(x):
    
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False

def perfect_number(num_range):
    candidate_list = list(range(1, num_range + 1))

    filtered_list = itertools.filterfalse(
        lambda x: sum(get_factors(x)) != x, 
        candidate_list
    )
    print(list(filtered_list))


def prime_number(num_range):
    prime_numbers = list(
        itertools.filterfalse(lambda x: check_if_has_dividers(x), 
        range(1, num_range + 1)
        )
    )
    print(prime_numbers)

def prime_number_sliced(num_range, limit):
    prime_numbers = itertools.islice(
        itertools.filterfalse(
                lambda x: check_if_has_dividers(x), 
                range(num_range)
            ), 
            limit
        )
    print(list(prime_numbers))

if __name__ == "__main__":
    perfect_number(100)
    prime_number(10000)
    prime_number_sliced(1000, 10)