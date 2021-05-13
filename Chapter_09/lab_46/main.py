import itertools as tools

def split(str_sequence):
    return [char for char in str_sequence]

def check_sequence_type(str_sequence):
    strong_mult = 0

    str_sign_sequence = "!@#$%^&*()-=[]\;',./`"
    str_num_sequence = "1234567890"
    str_lower_sequence = "abcdefghjklmnoprstuwyz"
    str_upper_sequence = "ABCDEFGHIJKLMNOPRSTUWYZ"

    for letter in split(str_sequence):
        if str_sign_sequence.find(letter) != -1:
            strong_mult += len(str_sign_sequence)
        if str_num_sequence.find(letter) != -1:
            strong_mult += len(str_num_sequence)
        if str_lower_sequence.find(letter) != -1:
            strong_mult += len(str_lower_sequence)
        if str_upper_sequence.find(letter) != -1:
            strong_mult += len(str_upper_sequence)
    
    return strong_mult



if __name__ == "__main__":
    password = input("Enter password to check for computer: ")
    
    #str_full_sequence = "ABCDEFGHIJKLMNOPRSTUWYZabcdefghjklmnoprstuwyz1234567890!@#$%^&*()-=[]\;',./`"
    strong_mult = check_sequence_type(password)

    combinations = tools.combinations_with_replacement(password, len(password))
    
    strong = 0

    for combination in combinations:
        print(combination)
        strong += 1

    print("Your password strong:", strong * strong_mult)
