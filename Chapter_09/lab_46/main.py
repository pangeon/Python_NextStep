import itertools as tools

def split(str_sequence):
    return [char for char in str_sequence]

def check_sequence_type(symbol):
    strong_mult = ""
    split_symbol = split(symbol)

    str_sign_sequence = "!@#$%^&*()-=[]\;',./`"
    str_num_sequence = "1234567890"
    str_lower_sequence = "abcdefghjklmnoprstuwyz"
    str_upper_sequence = "ABCDEFGHIJKLMNOPRSTUWYZ"

    for s in split_symbol:
        if s.find("S") == 0:
            strong_mult += str_sign_sequence
        if s.find("N") == 0:
            strong_mult += str_num_sequence
        if s.find("L") == 0:
            strong_mult += str_lower_sequence
        if s.find("U") == 0:
            strong_mult += str_upper_sequence
    
    return strong_mult

if __name__ == "__main__":
    symbol = input("Enter sequence type symbol: \nS - signs\nN - numbers\nU - uppercase letter\nL - lowercase letter\n")
    password = input("Enter password to check for computer: ")
    
    password_combinations = tools.combinations_with_replacement(password, len(password))
    all_combinations = tools.combinations_with_replacement(check_sequence_type(symbol), len(password))
    
    password_combinations_counter = 0
    all_combinations_counter = 0

    for pass_combination in password_combinations:
        password_combinations_counter += 1

    for one_in_all_combination in all_combinations:
        all_combinations_counter += 1

    print("password combinations:", password_combinations_counter)
    print("all combinations from", check_sequence_type(symbol) , all_combinations_counter)
    password_strong = all_combinations_counter / password_combinations_counter 
    print("Your password strong:", password_strong)

