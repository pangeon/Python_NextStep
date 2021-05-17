import os
import zipfile
import requests

class FileFromWeb:


    def __init__(self, url, temp_file):
        self.url = url
        self.temp_file = temp_file

 
    def download_file(self):
        response = requests.get(self.url)
        with open(self.temp_file, 'wb') as f:
            f.write(response.content)
        return self
 

    def close(self):
        # if os.path.isfile(self.temp_file):
            os.remove(self.temp_file)