import os
import requests

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

def generate():
    path_to_generate = point_from_cwd("generated")
    file_pl_location = point_file_from_cwd("generated", "pl.txt")
    file_com_location = point_file_from_cwd("generated", "com.txt")

    try:
        os.mkdir(path_to_generate)
    except:
        pass
     
    with open(file_pl_location, 'w') as file_pl:
        file_pl.write('http://www.wykop.pl/\n')
        file_pl.write('http://www.ale-beka-jest-taki-adres.pl/\n')
        file_pl.write('http://www.demotywatory.pl')
     
    with open(file_com_location, 'w') as file_com:
        file_com.write('http://www.realpython.com/\n')
        file_com.write('http://www.nonexistenturl.com/\n')
        file_com.write('http://www.stackoverflow.com')


def gen_get_file(dir):
    path = point_from_cwd(dir)
    list_of_files = os.listdir(path)

    for file_item in list_of_files:
        yield file_item  


def gen_get_file_lines(rel_path, file_name):
    path_to_file = point_file_from_cwd(rel_path, file_name)
    with open(path_to_file, "r") as lines:
        for line in lines:
            yield line.replace("\n", "").strip()


def check_webpage(url):
    try:
        if requests.get(url).status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False

def simply_test():
    temp_file_list = gen_get_file("temp")

    print(next(temp_file_list))
    print(next(temp_file_list))
    print(next(temp_file_list))

    file_1_temp_content = gen_get_file_lines("temp", "file_3.txt")

    print(next(file_1_temp_content))
    print(next(file_1_temp_content))
    print(next(file_1_temp_content))
    print(next(file_1_temp_content))
    
    print("---------------------------------------")
    
    web_page = "http://cecherz.pl"
    if check_webpage(web_page):
        print(web_page, "is exist")
    else:
        print(web_page, "not exist !")

    generate()


if __name__ == "__main__":
    file_list = gen_get_file("generated")
    
    for file_name in file_list:
        links_to_check = gen_get_file_lines("generated", file_name)
        
        for link in links_to_check:
            if check_webpage(link) == True:
                print(link, check_webpage(link))
            else:
                print(link, check_webpage(link))

    
    
