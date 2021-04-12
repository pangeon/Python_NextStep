import os

def path(folder_location, file_name):
    path_relative = folder_location + "\\" + str(file_name)
    path_to_file = os.getcwd() + "\\" +  path_relative

    return path_to_file

def log_it(*args):
    relative_path = path(r'Chapter_03\lab_18\files', 'logs.txt')

    with open(relative_path, "a") as file:

        for line in args:
            file.write(line)
            file.write(" ")

        file.write("\n")

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

