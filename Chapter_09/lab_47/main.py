import os
import itertools

def point_from_cwd(rel_path):
    defined_path = os.getcwd() + "\\" + rel_path 
    print("You want point dir: ", os.getcwd() + "\\" + rel_path)
    return defined_path


def point_file_from_cwd(rel_path, file_name):
    defined_path = os.getcwd() + "\\" + rel_path + "\\" + file_name 
    print("You want point file in dir: ", os.getcwd() + "\\" + rel_path + "\\" + file_name)
    return defined_path

def scan_tree(path):
    pass

if __name___ == "__main__":
    pass