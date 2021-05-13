import random as rand

def random_with_sum(number_of_values, asserted_sum):

    trial = 0
    numbers = []

    while True:
        counter = 0
        trial += 1
        i = rand.randint(0, number_of_values)
        numbers.append(i)
        for num in numbers:
            counter += num
        
        if asserted_sum < counter:
            yield (trial, numbers)
            trial = 0
    pass

if __name__ == "__main__":
    for i in range(0, 100):
        print(next(random_with_sum(3, 100)))