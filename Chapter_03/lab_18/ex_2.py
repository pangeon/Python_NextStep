import os


def input_to_list(arguments = "", arguments_list = []):
    while True:
        if arguments == "":
            option = input("Enter aguments with separator and press enter to exit: ")
            arguments += str(option)
            
            if not option:
                arguments_list = arguments.split(',')
                return list(arguments_list)
        else:
            arguments_list = arguments.split(',')
            return list(arguments_list)


def path(folder_location, file_name):
    path_relative = folder_location + "\\" + str(file_name)
    path_to_file = os.getcwd() + "\\" +  path_relative

    return path_to_file


def wrtite_to_file(location, file_name, data):
    try:
        file = open(path(location, file_name), "a")
        file.write(data + "\n")
        file.close()
    except:
        print("This file is exist !")


def log_it(*args, sep=""):
    args_list = list(*args)
    logs = ""
    for i in args_list:
        logs += i + sep 
    
    wrtite_to_file(r'Chapter_03\lab_18\files', 'logs.txt', logs)
    print("You write", "\"{}\"".format(logs), "in file:", r'Chapter_03\lab_18\files\logs.txt')



log_it(input_to_list(arguments= "a, b, c"))
log_it(input_to_list(arguments= "adam, artur, nowak"))
log_it(input_to_list(), sep = " ")

