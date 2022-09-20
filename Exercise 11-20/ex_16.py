"""Python Program to Find the Factorial of a Number"""
from math import factorial


class Factorial:
    def __init__(self,num_input) -> None:
        self.num_input=num_input

    def get_factorial(self):
        if self.num_input==0:
            print("The factorial of 1 is 0")
        else:
            fact_result=1
            for i in range(1,self.num_input+1):
                fact_result = fact_result * i
            print("The factorial of {0} is {1}".format(self.num_input, fact_result))

try:
    number_to_calc=int(input('Write the number to calculate his factorial:\t'))
    my_Factorial= Factorial(number_to_calc)
    result= my_Factorial.get_factorial()
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
