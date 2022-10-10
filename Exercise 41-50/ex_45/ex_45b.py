"""python Program to Find the Size (Resolution) of a Image"""

import os
from os.path import exists
from pathlib import Path

try:
    #change on your local computer
    local_path='d:/Jordan Bailon/Personal_Projects/Python/python_basic/Exercise 41-50/ex_45/'
    
    while(True):
        variable= input('Write the name of the file(with the extension) to get the data:\t ')
        if(variable==str(0)):
            print('End of the program')
            break
        else:
            variable=local_path+''+variable
            my_path= Path(variable)
            my_path.is_file()
            flag= os.path.exists(my_path)
            if flag:
                with open (my_path,'rb') as img:
                    img.seek(163)
                    loaded= img.read(2)
                    height = (loaded[0]<<8)+loaded[1]
                    loaded=img.read(2)
                    width= (loaded[0]<<8)+loaded[1]
                    print('The height is {0} px and the widht is {1} px.'.format(height,width))
            else:
                print('The input path is not correct.')


except Exception as ex:
    print(ex)