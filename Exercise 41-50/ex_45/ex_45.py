"""python Program to Find the Size (Resolution) of a Image"""

import os
from os.path import exists
from pathlib import Path

try:
    local_path='d:/Jordan Bailon/Personal_Projects/Python/python_basic/Exercise 41-50/ex_45/'
    while(True):
        variable= input('Write the name of the file(with the extension) to get the data:\t ')
        variable=local_path+''+variable
        if(variable==str(0)):
            print('End of the program')
            break
        else:
            my_path= Path(variable)
            my_path.is_file()
            flag= os.path.exists(my_path)
            if flag:
                print ('The size of the File is:\ ',os.stat(my_path).st_size)
            else:
                print('The input path is not correct.')


except Exception as ex:
    print(ex)