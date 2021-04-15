from book_class import Book #? book has only one class
import utils 

def welcome(version):
    print("Welcome in Book Store version:", version, "-- by Kamil Cecherz\n")
    
if __name__ == '__main__':
    welcome(1.1)
    
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
    
    #? Edit The Man in the High Castle -> book_3
    book_3.add_keywords_item(["anti-utopia", "war"])
    book_3.edit_index_item(4)
    book_3.__isBooked = True #! field is pseudo-private but I can change this field when usage -> _Book__isBooked = True  
    
    books = []
    
    books.append(book_1)
    books.append(book_2)
    books.append(book_3)
    
    for item in Book.AVAILABLE_BOOKS:
        item.info_about_item()
    
    #? Info about class properties -> utils.py
    # utils.print_info_about_class(book_3, Book)
    
        
