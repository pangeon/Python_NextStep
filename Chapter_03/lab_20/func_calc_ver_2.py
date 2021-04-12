def double(x):
    return 2 *x

    
def root(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x/2


def generate_values_sum(func, arg_num_list):
    """Return sum list results"""

    end_result = 0
    for i in range(len(arg_num_list)):
        end_result += func(arg_num_list[i])

    return end_result

x_table = list(range(11))


def generate_values_list(func, arg_num_list):
    """Return unit list results"""

    end_result = []
    for i in arg_num_list:
        end_result.append(func(i))

    return end_result

x_table = list(range(11))

print(generate_values_list(double, x_table))
print(generate_values_sum(double, x_table))

print(generate_values_list(root, x_table))
print(generate_values_sum(root, x_table))

print(generate_values_list(negative, x_table))
print(generate_values_sum(negative, x_table))

print(generate_values_list(div2, x_table))
print(generate_values_sum(div2, x_table))
