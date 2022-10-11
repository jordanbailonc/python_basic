"""Python Program to Find the hash of a File"""

import hashlib
from operator import ge

#this method returns thr hash code from a file input in it
def hash_sum(filename):
    #my hash
    h = hashlib.sha256()

    #load all array
    b = bytearray(128*1024)

    #load memory
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        #load while it has data
        while n := f.readinto(mv):
            #update by adding the memory loaded on each part (n)
            h.update(mv[:n])
    return h.hexdigest()

try:
    #my path
    my_path='d:/Jordan Bailon/Personal_Projects/Python/python_basic/Exercise 41-50/ex_46/'
    while(True):
        in_name = input('Write the name of the file to get hash:\t')
        if in_name==str(0):
            break
        else:
            all_path= my_path+''+in_name
            print('The hash of the file {0} written is:\t{1}'.format(in_name, hash_sum(all_path)))
except Exception as ex:
    print(ex)