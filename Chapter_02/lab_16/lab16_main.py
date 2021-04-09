import math
import time

"""
formula: abs(x**3 - x**0.5)
min = 0.0 max = 999997000002683.6
Time duration: 23.399475812911987
formula: abs(math.sin(x) * x**2)
min = 0.0 max = 9997170253.720783
Time duration: 24.921345949172974

******************************

formula: abs(x**3 - x**0.5)
min = 0.0 max = 999997000002683.6
Time duration: 1.2482812404632568
formula: abs(math.sin(x) * x**2)
min = 0.0 max = 9997170253.720783
Time duration: 1.1991429328918457
"""

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []

for i in range (1000000):
    argument_list.append(i/10)

# ? First solution without complie
def solution_1():
    for item in formulas_list:
        print("formula: {}".format(item))
        
        result_list = []

        start_time = time.time()
        for x in argument_list:
            result_list.append(eval(item))
        
        print("min = {} max = {}".format(min(result_list), max(result_list)))
        end_time = time.time()

        print("Time duration: {}".format(end_time - start_time))

# ? Second solution with complie
def solution_2():
    for item in formulas_list:
        print("formula: {}".format(item))
        
        result_list = []

        start_time = time.time()
        compiled_formula = compile(item, item, 'eval') # ! function complie
        for x in argument_list:
            result_list.append(eval(compiled_formula))
        
        print("min = {} max = {}".format(min(result_list), max(result_list)))
        end_time = time.time()

        print("Time duration: {}".format(end_time - start_time))

solution_1()
print("\n"+ "*"*30 + "\n")
solution_2()

