banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {
    "0.01": 0.00, 
    "0.02": 0.00, 
    "0.05": 0.00, 
    "0.1": 0.0, 
    "0.2": 0.00, 
    "0.5": 0.00,
    "1": 0, 
    "2": 0, 
    "5": 0,
    "10": 0, 
    "20": 0, 
    "50": 0,
    "100": 0, 
    "200": 0, 
    "500": 0,
}

def save_money(nominal, amount):
    global dict_denominations
    dict_denominations[str(nominal)] += amount

def get_value(nominal):
    print(dict_denominations[str(nominal)])
    return dict_denominations[str(nominal)]

save_money(1, 2)
save_money(5, 8)
save_money(0.5, 4)

get_value(0.5)
get_value(1)
get_value(5)

print(dict_denominations)
print(dict_denominations.values())
print(dict_denominations.keys())