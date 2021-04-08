import os
import urllib.request as req
import utils


data_dir = utils.get_file_from_relative_location(r'\Chapter_01\lab_6\files')
path = []

pages = [
    {'name':'mobilo', 'url': 'http://www.mobilo24.eu/'}, # 0
    {'name':'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'}, # 1
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'} # 2
]

for i in range(len(pages)):
    path.append(data_dir + "\\" + pages[i]['name'] + ".html")


for i in range(len(pages)):
    try:
        req.urlretrieve(pages[i]['url'], path[i])
        print('Operation success !')
    except:
        print('Operation failed !')
        break
else:
    print('-- End processing data ---')