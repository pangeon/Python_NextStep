import os

def path(folder_location, file_name):
    path_relative = folder_location + "\\" + str(file_name)
    path_to_file = os.getcwd() + "\\" +  path_relative

    return path_to_file

# ! Function is not used
def read_scripts():
    for file_path in files_to_process:
        with open(file_path, 'r') as f:
            print("File {} ...".format(os.path.basename(file_path)))
            source = f.read()
            exec(source)

files_to_process = [
    path(r'Chapter_02\lab_14\scripts', 'math_sin_square.py'),
    path(r'Chapter_02\lab_14\scripts', 'math_square_root.py')  
]

source_1 = open(files_to_process[0], "r")
source_2 = open(files_to_process[1], "r")

exec(source_1.read())
exec(source_2.read())

