import requests 
import utils
import os
    
data_dir = utils.get_file_from_relative_location(r'\Chapter_04\lab_25\web')
    
def save_url_file(url, dir, file,msg):
        
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
        
    with open(file_path, "wb") as f: 
        f.write(r.content)
        
msg = "Please wait - the file {} will be downloaded"
    
url = 'http://mobilo24.eu/spis'
dir = data_dir
file = 'spis.html'
save_url_file(url, dir, file,msg)
    
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = data_dir
file = 'logo.png'
save_url_file(url, dir, file,msg)