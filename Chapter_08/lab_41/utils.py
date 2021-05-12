import csv
from os_utils import OsUtils

def open_file(rel_path, file_name):
    os_utils = OsUtils()
    location = os_utils.point_file_from_cwd(rel_path, file_name)

    with open(location, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        while True:
            try:
                print(next(csvreader))
            except StopIteration:
                break