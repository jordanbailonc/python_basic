"""Python Program to Check Whether a String is Palindrome or Not"""
def reverse_slicing(s):
    return s[::-1]


class meditor():
    def __init__(self,name) -> None:
        self.name=name

    def check_palindrome(self):
        if(self.name ==(reverse_slicing(self.name))):
            print('{0} is a palindrome.'.format(self.name))
        else:
            print('{0} is not a palindrome.'.format(self.name))

try:
    my_data= input('Write the data to check palindrome:\t')
    cheker= meditor(my_data)
    cheker.check_palindrome()
except Exception as ex:
    print(ex)