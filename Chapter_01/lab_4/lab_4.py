import os

file_location_folders = ['Chapter_01', 'lab_4', 'files', 'piesn_o_zolnierzach_z_westerplatte.txt']

def get_file_from_relative_location(path_arg_list):
    path_to_file = os.getcwd()
    for item in path_arg_list:
        path_to_file += os.path.join("\\" + item)

    return path_to_file

def is_file_exits(path):
    if os.path.isfile(path):
        print('File %s exists' % path)
    else:
        print('File %s don\'t exists in ' % path)

def read_file_from_location(location):
    opened_file = open(location, 'r', encoding="utf-8")
    readed_file = opened_file.read()

    return readed_file

def word_stat(file_location):
    splited_text = read_file_from_location(file_location)
    print("Words in file: " + str(len(splited_text)))

file_location = get_file_from_relative_location(file_location_folders)

if __name__ == "__main__":
    is_file_exits(file_location)
    print(read_file_from_location(file_location))
    word_stat(file_location)




