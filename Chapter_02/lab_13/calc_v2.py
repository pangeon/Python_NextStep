import math as m

formula = str(input("Enter your formula: "))

def arg_list(list=[], start=1, end=101, step=10):
    for i in range(start, end):
        list.append(i/step)

    return list

def eval_formula(x):
    return eval(formula)

for i in range(len(arg_list())):
    print(i, eval_formula(arg_list()[i]))


