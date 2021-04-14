import requests
import functools as fx 
import utils
import os
    
data_dir = utils.get_file_from_relative_location(r'\Chapter_04\lab_25\web')
print(data_dir)
    
def save_url_file(url, dir, file, msg):
    
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
        
    with open(file_path, "wb") as f: 
        f.write(r.content)
        
msg = "Please wait - the file {} will be downloaded"

'''
#? Description
1. Invoke partly function "save_url_file" and given parameters dir and msg

2. "save_url_to_dir" has parametrs dir and msg. I must add only two parameters:
    a) url
    b) file
'''

save_url_to_dir = fx.partial(save_url_file, dir=data_dir, msg=msg)    

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url = url, file = file)
    
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
save_url_to_dir(url = url, file = file)