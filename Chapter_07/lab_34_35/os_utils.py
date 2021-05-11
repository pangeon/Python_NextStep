import os

class OsUtils:


    @staticmethod    
    def cwd():
        print("You are in: ", os.getcwd())
        return os.getcwd()


    @staticmethod
    def point_from_cwd(rel_path):
        defined_path = os.getcwd() + "\\" + rel_path 
        print("You want point dir: ", os.getcwd() + "\\" + rel_path)
        return defined_path


    @staticmethod
    def point_file_from_cwd(rel_path, file_name):
        defined_path = os.getcwd() + "\\" + rel_path + "\\" + file_name 
        print("You want point file in dir: ", os.getcwd() + "\\" + rel_path + "\\" + file_name)
        return defined_path
