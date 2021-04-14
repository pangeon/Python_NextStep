import Book as Library

# ! Function is not neccessary it has been replaced by a method in Book class -> info_about_item
def print_info_about_book(book):
    
    print("1) index: {}\n2) title: {}\n3) author: {}\n4) keywords: {}\n5) publication date: {}"
          .format(book.index, book.title, book.author, book.keywords, book.publication_date))
    
    print("-"*80)
    
if __name__ == '__main__':
    
    book_1 = Library.Book(
        1,
        "Ulysses", "James Joyce", 
        ["modernist", "puns", "parodies", "allusions", "adaptations"], 
        "ENG", 1918)
    
    book_2 = Library.Book(
        2, 
        "Animal Farm", "George Orwell", 
        ["political satire", "allergorical", "sc-fi"], 
        "ENG", 1945)
    
    book_3 = Library.Book(
        3, 
        "The Man in the High Castle", "Phillip P. Dick", 
        ["alternate history", "allergorical", "sc-fi"], 
        "ENG", 1962)
    
    #? Edit The Man in the High Castle -> book_3
    book_3.add_keywords_item(["anti-utopia", "war"])
    book_3.edit_index_item(4)
    
    books = []
    
    books.append(book_1)
    books.append(book_2)
    books.append(book_3)
    
    for item in books:
        # print_info_about_book(item) <- off function 
        Library.Book.info_about_item(item)