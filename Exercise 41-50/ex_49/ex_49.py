"""Python Program to Create Safety a Nested Directory"""
#imports

import os
from pathlib import Path

### Program

name_File= input('Write the name of the directory:\t')

#gets the absolute path to the file
ROOT_DIR= os.path.dirname(os.path.abspath(__file__))

#add to the path the filename to create nested directory
all_path= str(ROOT_DIR)+'\\'+name_File

#prints the path name to check after executes the program
print(ROOT_DIR)

#create the directory with the name input
Path(all_path).mkdir(parents=True, exist_ok=True)
