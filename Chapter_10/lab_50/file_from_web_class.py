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
            reading_file.writelines(response.content)
        return self
    

    def __exit__(self):
        pass