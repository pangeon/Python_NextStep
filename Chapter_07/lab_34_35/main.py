import os
from shutil import copyfile
import urllib3.exceptions
import requests

import os_utils as os_utils
from os_utils import OsUtils
import url_hander as url_utils

if __name__ == "__main__":
    os_utils = OsUtils()
    
    dir_tmp = os_utils.point_file_from_cwd("tmp", "download.tmp")
    dir_html = os_utils.point_file_from_cwd("html", "file.html")
    url = "http://www.mobilo24.eu/spis/"

    try:
        if os.path.exists(dir_tmp):
            print('Removing {}'.format(dir_tmp))
            os.remove(dir_tmp)
        
        url_utils.save_url_to_file(url, dir_tmp)
        copyfile(dir_tmp, dir_html)

    except requests.exceptions.ConnectionError as e:
        print('Page from URL doesn\'t exist ! {}'.format(url))
        print('Error details: {}'.format(e))
    
    except (PermissionError, FileNotFoundError) as e:
        print('File access permission problem with:\n{}\n{}'.format(dir_html, dir_tmp))
        print('Error details: {}'.format(e))
    
    except Exception as e:
        print('Somethings is wrong !')
        print('Error details: {}'.format(e))

    else:
        print('URL downloaded successfully {}'.format("file.html"))

    finally:
        if os.path.exists(dir_tmp):
            print("Remove temporary file {}".format(dir_tmp))
            os.remove(dir_tmp)
        print('DONE!')

