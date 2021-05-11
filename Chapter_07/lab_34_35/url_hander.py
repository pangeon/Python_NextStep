import requests
import os
import shutil

def save_url_to_file(url, file_path):
    response = requests.get(url, stream = True)     
    with open(file_path, "wb") as working_file: 
        working_file.write(response.content)