"""Python Program to Check if a Number is Positive, Negative or 0"""
import numbers


class Checker:
    def __init__(self,num_check):
        self.num_check =num_check

    def comparision(self):
        if(self.num_check>0):
            print('{0} is positive because is bigger than 0'.format(self.num_check))
        elif(self.num_check==0):
            print('{0} is not positive or negative.'.format(self.num_check))
        elif(self.num_check<0):
            print('{0} is a negative number because is lower than 0.'.format(self.num_check))
try:
    num_input=float(input('Write the number to check:\t'))
    my_check=Checker(num_input)
    my_check.comparision()
except:
    print('The data must be numeric.')