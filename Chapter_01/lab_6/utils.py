import os

def get_file_from_relative_location(location):
    path_to_file = os.getcwd()
    raw_path = path_to_file + location

    return raw_path