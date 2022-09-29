"""Python Program to Convert Decimal to Binary Using Recursion"""

def convert_binary(x):
    if x>1:
        convert_binary(x//2)
    print(x%2,end=' ')

try:
    my_num=int(input('Write the number to convert binary:\t'))
    convert_binary(my_num)
except:
    print('The data input is not conversible.')