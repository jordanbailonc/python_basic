"""Python Program to Display Fibonacci Sequence Using Recursion"""

def get_next(x,y,l):
    aux=x+y
    x=y
    y=aux
    print(aux)
    if(x<l):
        get_next(x,y,l)
        if(x==l):
            aux=l+1
    elif(x>l):
        aux==l

try:
    max_num= int(input("Write the number which will be the limit to Fibonacci's sequence:\t"))
    get_next(0,1,max_num)
except Exception as ex:
    print(ex)