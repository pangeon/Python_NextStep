import math as m

formula = str(input("Enter your formula: "))

def fill_arg_list(list=[], start=0, end=100, step=0.1):
    for i in range(start, end):
        step += 0.1
        list.append(i + step)

    return list

x = fill_arg_list()

def calc(x):
    return eval(formula)

for i in range(100):
    print(calc(x[i]))


