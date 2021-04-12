def double(x):
    return 2 *x
    
def root(x):
    return x**2
    
def negative(x):
    return -x
    
def div2(x):
    return x/2

number = 8
transformations = [double, root, negative, div2]

temp_return_value = number

for func in transformations:
    temp_return_value = func(8)
    print(temp_return_value)

print("@"*50)

for func in [root, root, div2, double]:
    temp_return_value = func(8)
    print(temp_return_value)