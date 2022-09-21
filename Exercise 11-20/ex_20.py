"""Python Program to Find Armstrong Number in an Interval"""


class Armstrong:
    def __init__(self,input_num, num2) -> None:
        self.input_num=input_num
        self.num2=num2

    def check_armstrong(self):
        for number in range(self.input_num,self.num2):
            
            index = len(str(number))

            sume= 0

            aux = number
            while aux>0:
                my_digit = aux % 10
                sume += my_digit ** index
                aux //=10
            
            if number==sume:
                print('{0} is an Armstrong number.'.format(number))


try:
    number_check=int(input('Write the 1st number to check:\t'))
    second = int(input('Write the second:\t'))
    my_Armstrong=Armstrong(number_check,second)
    my_Armstrong.check_armstrong()
except Exception as ex:
    print(ex)