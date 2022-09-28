"""Python Program to Make a Simple Calculator"""


def addition():
    num1=int(input('Write the first number:\t'))
    num2=int(input('Write the second number:\t'))
    print(num1+num2)

def substraction():
    num1=int(input('Write the first number:\t'))
    num2=int(input('Write the second number:\t'))
    print(num1-num2)

def product():
    num1=int(input('Write the first number:\t'))
    num2=int(input('Write the second number:\t'))
    print(num1*num2)

def remanance():
    num1=int(input('Write the first number:\t'))
    num2=int(input('Write the second number:\t'))
    print(num1/num2)

def switch(x):
    switch={
        '1': addition(),
        '2':substraction(),
        '3':product(),
        '4':remanance(),
    }



my_options=['1.-Addition','2.-Substraction','3.-Product','4.-Reminance','0.-Log Out']
while True:
    print('.... OPTIONS ....')
    for option in my_options:
        print(option)

    choice= int (input('Write the option:\t'))
    if(choice==0):
        print('End of the program.')
        break
    elif(choice==1):
        addition()
    elif(choice==2):
        substraction()
    elif(choice==3):
        product()
    elif (choice==4):
        remanance()

