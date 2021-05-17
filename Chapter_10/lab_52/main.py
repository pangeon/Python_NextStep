import os
import zipfile
import contextlib
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
    file_in_dir = point_file_from_cwd("temp", "eurofxref.zip")
    path = point_from_cwd("temp")

    with contextlib.suppress(FileNotFoundError):

        with contextlib.closing(FileFromWeb(url, file_in_dir)) as file_to_download: 
            file_to_download.download_file()

            with zipfile.ZipFile(file_to_download.temp_file, "r") as z:
                a_file = z.namelist()[0]
                print(a_file)
                os.chdir(path)
                z.extract(a_file, '.', None)

            os.remove(file_to_download.temp_file)



