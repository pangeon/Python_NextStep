import book_class as Library
import utils 
    
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
    
    for item in Library.Book.AVAILABLE_BOOKS:
        item.info_about_item()
    
    #? Info about class properties -> utils.py
    for i in utils.info_about_class(book_1, Library.Book):
        print(i + "\n")
        
