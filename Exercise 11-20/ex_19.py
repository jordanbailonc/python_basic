"""Python Program to Check Armstrong Number"""

class Armstrong:
    def __init__(self,input_num, num2) -> None:
        self.input_num=input_num
        self.num=num2

    def check_armstrong(self):
        sum=0
        index =(len(str(self.input_num)))
        aux=self.input_num
        while aux >0:
            my_digit = aux % 10
            sum += my_digit ** index
            aux //=10

        if self.input_num==sum:
            print('{0} is an Armstrong number'.format(self.input_num))
        else:
            print('{0} is not an Armstong number.'.format(self.input_num))

try:
    number_check=int(input('Write the integer number to check:\t'))
    my_Armstrong=Armstrong(number_check)
    my_Armstrong.check_armstrong()
except Exception as ex:
    print(ex)