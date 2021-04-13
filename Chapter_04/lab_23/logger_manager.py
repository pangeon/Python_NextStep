import os
from datetime import datetime as dt
import functools

'''
#? Description
---------------
1. Pass parameters to wrapper
    a) action name
    b) file location
        * generates file relative location path with function path()

2. Inside "wrapper_with_log_file" is "wrapper_with_log_to_known_file" wchich invoke "the_real_wrapper":
    wrapper_with_log_file -> 
        wrapper_with_log_to_known_file -> 
            the_real_wrapper
            
3. "the_real_wrapper" has own logic:
    a) open file from path
    b) write inside information about:
        * logged action
        * path to file where we write information
        * time markdown

4. Function create_file with decorator "@wrapper_with_log_file" print log and open file "diary_log.txt" to write
 
5. Function delete_file with decorator "@wrapper_with_log_file" print log and delete file "diary_log.txt"

6. Both functions writes information in other files: 
    a) file_create.txt, 
    b) file_delete.txt

'''

def path(folder_location, file_name):
    ''' 
    You must define relative path based on the location from 
    the main project directory.

        example:
        --------
        path(r'Chapter_03\lab_18\files', 'logs.txt')
    '''
    path_relative = folder_location + "\\" + str(file_name)
    path_to_file = os.getcwd() + "\\" +  path_relative

    return path_to_file

location_create = path(r'Chapter_04\lab_23\logs', 'file_create.txt')
location_delete = path(r'Chapter_04\lab_23\logs', 'file_delete.txt')
diary_log = path(r'Chapter_04\lab_23\logs', 'diary_log.txt')

##* wrapper_with_log_file -> wrapper_with_log_to_known_file -> the_real_wrapper
def wrapper_with_log_file(logged_action, log_file_path):
    
    ##* wrapper_with_log_to_known_file -> the_real_wrapper
    def wrapper_with_log_to_known_file(func):
        
        ##* the_real_wrapper
        def the_real_wrapper(path):
            
            ##* wrapper body
            with(open(log_file_path, 'a')) as file:
                file.write('Action {} executed on {} on {}\n'
                           .format(logged_action, 
                                   path, 
                                   dt.now().strftime("%Y-%m-%d %H:%M:%S")
                                   )
                           )
            ##* wrapper body
            
            return func(path)
        ##* the_real_wrapper
        
        return the_real_wrapper
    ##* wrapper_with_log_to_known_file -> the_real_wrapper
    
    return wrapper_with_log_to_known_file
##* wrapper_with_log_file -> wrapper_with_log_to_known_file -> the_real_wrapper

@wrapper_with_log_file('FILE_CREATE', str(location_create))
def create_file(path):
    print('creating file: {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', str(location_delete))
def delete_file(path):
    print('deleting file: {}'.format(path))
    os.remove(path)

create_file(diary_log)
delete_file(diary_log)