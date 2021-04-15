class Book:
    
    __LANGUAGES = ['ENG', 'PL', 'GER', 'FRA', 'SPA', 'JPN', 'RUS', 'POR']
    
    available_books = []
    
    def __init__(
        self, 
        index, 
        title, 
        author, 
        keywords, 
        lang, 
        publication_date, 
        isBooked = None, 
        ISBN = None):
        
        self.index = len(self.available_books) + 1
        self.title = title
        self.author = author
        self.keywords = keywords.copy()
        
        if lang in self.__LANGUAGES: 
            i = self.__LANGUAGES.index(lang)
            self.lang = self.__LANGUAGES[i]
        else:
            self.lang = 'OTHER'
            
        self.publication_date = publication_date
        self.available_books.append(self)
        self.__isBooked = isBooked
        self.__ISBN = ISBN
        
    
    def info_about_item(self):
        """Print about one book item in liblary"""
        
        print(
        """
        1) index: {}
        2) title: {}
        3) author: {}
        4) keywords: {}
        5) language: {}
        6) publication date: {}
        7) is booked: {}
        8) ISBN: {}
        """.format(
              self.index, 
              self.title, 
              self.author, 
              self.keywords, 
              self.lang, 
              self.publication_date, 
              self.__isBooked,
              self.__ISBN
        ))
    
        print("-"*80)
    

    def edit_index_item(self, index):
        """Change book index number"""
        self.index = index
        
    
    def add_keywords_item(self, *args):
        """Add new keywords to book instance"""
        self.keywords.extend(*args) # ! "append()" create nested list into exited list, i must pass args with *
        
        
    def __get_ISBN(self):
        """Return property ISBN""" 
        return self.__ISBN
    
    
    def __set_ISBN(self, new_ISBN):
        """Check type and set property ISBN"""   
        if(str(type(new_ISBN)) or float(type(new_ISBN))):    
            self.__ISBN = int(new_ISBN)
        elif(new_ISBN == True or new_ISBN == False):
            self.__ISBN = None
        else:  
            self.__ISBN = new_ISBN
        
    ISBN = property(__get_ISBN, __set_ISBN, None, "Setting ISBN")