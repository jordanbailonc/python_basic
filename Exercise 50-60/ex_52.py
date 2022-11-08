"""Python program to slice list depending on the option"""

# app methods
def print_all(list):
    print(list[:])

def print_after_index(list, index):
    print(list[:index])

def print_before_index(list,index):
    print(list[index:])

# app attributes    
flag = False
test = False
my_main_list = [1,2,3,4,5,6,7,8]

while flag==False:
    print("====READER APP=====:\n0.- Exit \n1.- Read All\n2.- Read after index:\n3.- Read before")
    option = int(input("Write you option:\t"))
    if (option == 0):
        print("Closing program....")
        exit()
    elif (option ==1):
        print_all(my_main_list,)
    elif (option ==2):
        print("Option 2")
        index = int(input("Write the index to write all data from it till the end:\t"))
        if index < my_main_list.__sizeof__() or index == my_main_list.__sizeof__() and index >0:
            print_after_index(my_main_list, index)
    elif (option == 3):
        print("Option 3")
        index = int(input ("Write the index to write it till the begginig:\t "))
        if index < my_main_list.__sizeof__() or index == my_main_list.__sizeof__() and index >0:
            print_before_index(my_main_list,index)

