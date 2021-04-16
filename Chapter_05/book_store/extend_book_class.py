from book_class import Book #? book has only one class
import types
import utils


liblary_template_header = """
<table border=1>
"""

liblary_template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Title</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Author</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Keyword</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Lang</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Pub date</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Booked</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>ISBN</td>
         <td>{}</td>
       </tr>
</table>
"""

liblary_template_footer ="""
</indent></table>
"""


def export_item_to_HTML(obj, path):
    with open(path, "w") as file:    
        content = liblary_template.format(
            obj.index, 
            obj.title, 
            obj.author,
            obj.keywords,
            obj.lang,
            obj.publication_date,
            obj._Book__is_booked,
            obj.ISBN
        )
        print(content)
        file.write(content)


def export_all_to_HTML(cls, path):   
    with open(path, "w") as file:    
        file.write(liblary_template_header)
        
        for item in cls.available_books:   
            content = liblary_template.format(
                item.index, 
                item.title, 
                item.author,
                item.keywords,
                item.lang,
                item.publication_date,
                item._Book__is_booked,
                item.ISBN
            )
            file.write(content)
            
        file.write(liblary_template_footer)


def export_this_to_HTML(self, path):   
    with open(path, "w") as file:      
        content = liblary_template.format(
            self.index, 
            self.title, 
            self.author,
            self.keywords,
            self.lang,
            self.publication_date,
            self._Book__is_booked,
            self.ISBN
        )
        file.write(content)


def add_static_method(obj, path):
    Book.export_item_to_HTML = export_item_to_HTML
    Book.export_item_to_HTML(obj, path)

def add_class_method(path):   
    Book.export_all_to_HTML = types.MethodType(export_all_to_HTML, Book)
    Book.export_all_to_HTML(path)
    
def add_intance_method(path):
    for item in Book.available_books:  
        item.export_this_to_HTML = types.MethodType(export_this_to_HTML, item)
        
    for item in Book.available_books:  
        item.export_this_to_HTML(path.format(item.title.replace(' ','_')))   
    