
def half_triangle_ast(num):
    for i in range(num):
        for j in range (i+1):
            print("*", end="")
        print("\n")

def half_triangle_input(num,my_char):
    for i in range(num):
        for j in range(i+1):
            print(my_char, end="")
        print("\n")

def half_triangle_numbers(num):
    for i in range(num):
        for j in range(i+1):
            print(j+1, end="")
        print("\n")    
        

def full_triangle_ast(num):
    j=0
    for i in range(1, num+1):
        for space in range(1, (num-i)+1):
            print(end="  ")
    
        while j!=(2*i-1):
            print("*", end="")
            j += 1
    
        j = 0
        print()


def full_triangle_input(num,my_char):
    j=0
    for i in range (1,num+1):
        for space in range(1,(num-i)+1):
            print(end="   ")
            
        while j!=(2*i-1):
            print(my_char+' ', end='')
            j +=1

        j=0
        print()




try:
    while(True):
        all_Options= ['0.- Exit', '1.- Print half pyramid with *','2.- Print pyramid with characthers','3.- Print pyramid with numbers','4.- Full pyramid with *','5.- Full pyramid with characters']
        for option in all_Options:
            print(option)
        my_option= int(input('Write the option you want:\t'))
        if my_option==0:
            print('Thanks for coming...')
            break
        elif my_option==1:
            my_size= int(input('Write the long size of the piramid:\t'))
            half_triangle_ast(my_size)
        elif my_option==2:
            my_size = int(input('Write the size of pyramid:\t'))
            my_char = input('Data to write:\t')
            half_triangle_input(my_size,my_char)
        elif my_option==3:
            my_size= int(input('Write the size of the triangle:\t'))
            half_triangle_numbers(my_size)
        elif my_option==4:
            my_size = int(input('Write the size of the pyramid:\t'))
            full_triangle_ast(my_size)
        elif my_option==5:
            my_size=int(input('Write the size of the pyramid:\t'))
            my_char = input('Write the character to write:\t')
            full_triangle_input(my_size,my_char)
        else:
            print("You didn't chose any of the options available:\t")
except Exception as ex:
    print(ex)

