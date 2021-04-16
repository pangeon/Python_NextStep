from book_class import Book #? book has only one class
from extend_book_class import add_class_method, add_static_method, add_intance_method
import utils 

def add_items(*items):
    collection = []
    collection.append(items)
        
    return collection

def print_collection_info(collection, messsage):
    print(messsage + "\n")
    for item in collection:
        item.info_about_item()
        
    
def welcome(version):
    print("Welcome in Book Store version:", version, "-- by Kamil Cecherz\n")
    
if __name__ == '__main__':
    welcome("1.4 with bugs")
    
    book_1 = Book(
        1,
        "Ulysses", "James Joyce", 
        ["modernist", "puns", "parodies", "allusions", "adaptations"], 
        "ENG", 1918, True)
    
    book_2 = Book(
        2, 
        "Animal Farm", "George Orwell", 
        ["political satire", "allergorical", "sc-fi"], 
        "ENG", 1945, False)
    
    book_3 = Book(
        3, 
        "The Man in the High Castle", "Phillip P. Dick", 
        ["alternate history", "allergorical", "sc-fi"], 
        "ENG", 1962, False)
    
    #* Edit The Man in the High Castle -> book_3
    book_3.add_keywords_item(["anti-utopia", "war"])
    book_3.edit_index_item(4)
    book_3.__is_booked = True #! field is pseudo-private but I can change this field when usage -> _Book__is_booked = True
    book_3.ISBN = 9781328849861
    # del book_3.ISBN #! You can delete this property from class
    
    #* Edit The Man in the High Castle -> book_3
    
    ##*  Print collection
    books = add_items(book_1, book_2, book_3)
    print_collection_info(Book.available_books, "Print objects from book_class.py")
    ##*  Print collection
    
    #* Reading objects books from files -> bin
    Book.save_to_file(book_1, 'Chapter_05/book_store/bin/file_1.book')
    Book.save_to_file(book_2, 'Chapter_05/book_store/bin/file_2.book')
    Book.save_to_file(book_3, 'Chapter_05/book_store/bin/file_3.book')
    
    obj_1 = Book.read_from_file('Chapter_05/book_store/bin/file_1.book')
    obj_2 = Book.read_from_file('Chapter_05/book_store/bin/file_2.book')
    obj_3 = Book.read_from_file('Chapter_05/book_store/bin/file_3.book')
    
    books_objs = []
    books_objs.append(obj_1)
    books_objs.append(obj_2)
    books_objs.append(obj_3)

    print_collection_info(books_objs, "Reading objects books from files -> bin")    
    #* Reading objects books from files -> bin
    
    #* extend Book class -> no inheritance -> add method outside the class -> file extend_book_class
    
    
    # TODO: Something is wrong, I can't fix it !
    # add_class_method()
    # add_static_method(book_1)
    # add_intance_method()
    # print(dir(Book))
    # TODO: Something is wrong, I can't fix it !
    
    
    
    #* extend Book class -> no inheritance -> add method outside the class -> file extend_book_class
    
    #* Info about class properties -> utils.py
    # utils.print_info_about_class(book_3, Book)
    #* Info about class properties -> utils.py  