import os
import zipfile
from file_from_web_class import FileFromWeb

### -------------------------------- @UTILS@ ----------------------------- ###

def point_from_cwd(rel_path):
    defined_path = os.getcwd() + "\\" + rel_path 
    print("You want point dir: ", os.getcwd() + "\\" + rel_path)
    return defined_path


def point_file_from_cwd(rel_path, file_name):
    defined_path = os.getcwd() + "\\" + rel_path + "\\" + file_name 
    print("You want point file in dir: ", os.getcwd() + "\\" + rel_path + "\\" + file_name)
    return defined_path

### -------------------------------- @UTILS@ ----------------------------- ###

if __name__ == "__main__":
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
    dir = point_file_from_cwd("temp", "eurofxref.zip")

    with FileFromWeb(url, dir) as f:
        with zipfile.ZipFile(f.temp_file, "r") as z:
            path = point_from_cwd("temp")
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir(path)
            z.extract(a_file + "x", '.', None)



