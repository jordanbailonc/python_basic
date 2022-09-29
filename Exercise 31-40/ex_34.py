"""Python Program to Find Factorial of Number Using Recursion"""

def get_next_product(x,y):
    aux=x*y
    y=y-1
    x=aux
    if(y>0):
        get_next_product(x,y)
    elif(y==0):
        print(x)

        

try:
    num1_= int(input('Write the number you want to get factorial:\t'))
    get_next_product(num1_,num1_-1)
except Exception as ex:
    print(ex)