"""Python Program to Merge Maills"""

path_name=r'D:\Jordan Bailon\Personal_Projects\Python\python_basic\Exercise 41-50\ex_44'
main_content = r'D:\Jordan Bailon\Personal_Projects\Python\python_basic\Exercise 41-50\ex_44'
this_name=r'\names.txt'
this_content=r'\content.txt'
all_names=""
invitation_content=""

with open(path_name,'r') as data1:
    all_names= data1.readlines()

    with open (main_content,'r') as data2:
        invitation_content= data2.read()

        for name in all_names:
            real_inv= "Hello " +name.strip() +"\n"+ invitation_content
            print(real_inv)

