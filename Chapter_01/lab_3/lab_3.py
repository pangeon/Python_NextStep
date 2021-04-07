import sys

def display_options(option_list):
    i = 0
    for item_option in option_list:
        print(str(i) + " - ", item_option)
        i += 1

    option = input("Write data to console or press enter to exit: ")
    return option

option = "x"
option_list = ['load data', 'export data', 'analyze & predict']

while option:
    
    option = display_options(option_list)

    if option:
        try:
            option_choice = int(option) - 1
            if option_choice >= 0 and option_choice < len(option_list):
                print("You selected {} - {}".format(option_choice + 1), option_list[option_choice])
            else:
                print("Choose a option from a option list or press enter")
        except:
            print("You need to enter a number")
    else:
        print("----- END -----")
