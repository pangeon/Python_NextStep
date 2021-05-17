import os
import zipfile
import requests

class FileFromWeb:


    def __init__(self, url, temp_file):
        self.url = url
        self.temp_file = temp_file


    def __enter__(self):
        response = requests.get(self.url)
        with open(self.temp_file, "wb") as reading_file:
            reading_file.write(response.content)
        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == None and exc_val == None and exc_tb == None:
            print(">>>>>>>>>>> Operation complete: no errors :)")
        else:
            print('>>>>>>>>>>> Error details',exc_type, exc_val, exc_tb)
            
            if exc_type == FileNotFoundError: 
                print('>>>>> Incorrect directory/file: {}'.format(exc_val))
                return True
            elif exc_type == KeyError:
                print('>>>>> There is no file in archive! {}'.format(exc_val))
                return True
            else:
                return False 