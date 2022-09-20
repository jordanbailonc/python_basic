"""Python Program to Check Prime Number """
from tkinter.tix import ExFileSelectBox


class prime_tester:
    def __init__(self,number) -> None:
        self.number=number
    
    def check_number(self):
        flag= False

        if self.number>1:
            for i in range(2,self.number):
                if (self.number % i ==0):
                    flag=True

                    break
        
        if flag:
            print('{0} is not a prime number.'.format(self.number))
        else:
            print('{0} is a prime number.'.format(self.number))

try:
    print('uwu')
    user_input = int(input('Write the number you want to check:\t'))
    my_tester = prime_tester(user_input)
    my_tester.check_number()
except:
    print('Usage: only numbers accepted in the inputs.')