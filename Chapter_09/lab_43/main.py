def add_sequnence(min_value, step, max_value):
    sequence_list = []
    next_value = 0
    next_step = 0

    while True:
        if min_value < max_value or step < max_value:
            next_step = min_value + step
            next_value += next_step
            if next_value < max_value:
                sequence_list.append(next_value)       
            else:
                break
        else:
            break
    
    return sequence_list

def yield_add_sequnence(min_value, step, max_value, operator="+"):
    sequence_list = []
    next_value = 0
    next_step = 0

    while True:
        if min_value < max_value or step < max_value:
            next_step = min_value + step
            next_value += next_step
            if next_value < max_value:
                yield next_value
                sequence_list.append(next_value)       
            else:
                break
        else:
            break
    
    return sequence_list


yield_list = yield_add_sequnence(1, 2, 10)

# print(next(yield_list))
# print(next(yield_list))
# print(next(yield_list))

for item in yield_list:
    print(item, end= " ")




    
    
