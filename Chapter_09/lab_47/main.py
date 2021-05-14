import os
import itertools

def point_from_cwd(rel_path):
    defined_path = os.getcwd() + "\\" + rel_path 
    print("You want point dir: ", os.getcwd() + "\\" + rel_path)
    return defined_path


def scan_tree(path):
    list_dir = os.scandir(path)

    for item in list_dir:
        if item.is_dir() == True:
            yield item
            yield from scan_tree(item)
        else:
            yield item

def show_sctructure(option = "LIST"):
    dir = point_from_cwd("js")
    
    listing = scan_tree(dir)
    
    if option == "LIST":
        for item in listing:
            print('DIR' if item.is_dir() else 'FILE', item.path)
    
    listing = sorted(listing, key = lambda item: item.is_dir())

    if option == "COUNT":
        for is_dir, items in itertools.groupby(listing, key = lambda item: item.is_dir()):
            print('DIR ' if is_dir else 'FILE', len(list(items)))

if __name__ == "__main__":
    show_sctructure()
    show_sctructure(option = "COUNT")