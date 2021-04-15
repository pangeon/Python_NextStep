def info_about_class(object_name, class_name):
    info = []
    info.append("isinstance({}, {}) {}".format(object_name, class_name, isinstance(object_name, class_name)))
    info.append("type({}) is {} {}".format(object_name, class_name, type(object_name) is class_name))
    info.append("vars {} ".format(vars(object_name)))
    info.append("vars {} ".format(vars(class_name)))
    info.append("dir {}".format(vars(object_name)))
    info.append("dir {}".format(vars(class_name)))
    
    return info

# ! Function is not neccessary it has been replaced by a method in Book class -> info_about_item
def print_info_about_book(book):
    
    print("1) index: {}\n2) title: {}\n3) author: {}\n4) keywords: {}\n5) publication date: {}"
          .format(book.index, book.title, book.author, book.keywords, book.publication_date))
    
    print("-"*80)