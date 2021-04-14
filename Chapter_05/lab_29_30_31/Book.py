class Book:
    
    LANGUAGES = ['ENG', 'PL', 'GER', 'FRA', 'SPA', 'JPN', 'RUS', 'POR']
    
    def __init__(self, index, title, author, keywords, lang, publication_date):
        self.index = index
        self.title = title
        self.author = author
        self.keywords = keywords.copy()
        
        if lang in self.LANGUAGES: 
            i = self.LANGUAGES.index(lang)
            self.lang = self.LANGUAGES[i]
        else:
            self.lang = 'OTHER'
            
        self.publication_date = publication_date
        
    
    def info_about_item(self):
        """Print about one book item in liblary"""
        
        print("1) index: {}\n2) title: {}\n3) author: {}\n4) keywords: {}\n5) language: {}\n6) publication date: {}"
          .format(self.index, self.title, self.author, self.keywords, self.lang, self.publication_date))
    
        print("-"*80)
    
    
    def edit_index_item(self, index):
        """Change book index number"""
        self.index = index
        
    
    def add_keywords_item(self, *args):
        """Add new keywords to book instance"""
        self.keywords.extend(*args) # ! "append()" create nested list into exited list, i must pass args with *
        