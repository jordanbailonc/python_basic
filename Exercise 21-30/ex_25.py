"""Python Program to Find ASCII Value of Character"""
class val_char:
    def __init__(self,char) -> None:
        self.char=char

    def print_ord(self):
        print(ord(self.char))

try:
    my_char=input('Write the characther you want ti converter: \t')
    if(len(my_char)>1):
        print('The input only admits one characther.')
    else:
        converter= val_char(my_char)
        converter.print_ord()
except:
    print('Some error occurs.')