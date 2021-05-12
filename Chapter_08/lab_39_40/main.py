import time
import sys
from pprint import pprint 
from combinations_class import Combinations

def test_1():

    products = ["Products: {}".format(i) for i in range(1, 500)]
    promototions = ["Promotions: {}".format(i) for i in range(1, 50)]
    customers = ["Customers: {}".format(i) for i in range(1, 500)]

    combinations = []

    for product in products:
        for promotion in promototions:
            for customer in customers:
                combinations.append("{} - {} - {}".format(product, promotion, customer))

    for combination in combinations:
        pass

    time.sleep(10)
    pprint("test 1 - memory uage: {}".format(sys.getsizeof(combinations)))


def test_2():
    products = ["Products: {}".format(i) for i in range(1, 500)]
    promototions = ["Promotions: {}".format(i) for i in range(1, 50)]
    customers = ["Customers: {}".format(i) for i in range(1, 500)]
    
    combinations = Combinations(products, promototions, customers)

    for combination in combinations:
        pass

    time.sleep(10)
    pprint("test 2 - memory uage: {}".format(sys.getsizeof(combinations)))


def item_example():
    products = ["Products: {}".format(i) for i in range(1, 4)]
    promototions = ["Promotions: {}".format(i) for i in range(1, 3)]
    customers = ["Customers: {}".format(i) for i in range(1, 6)]
    
    combinations = Combinations(products, promototions, customers)

    for i in range(1, 30):
        print(i, combinations[i])


if __name__ == "__main__":
    # test_1()
    # test_2()
    item_example()