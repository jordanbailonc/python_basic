"""Python Program to Find Numbers Divisible by Another Number"""

class Divisors:
    def __init__(self,num_max) -> None:
        self.num_max=num_max

    def show_divisibles(self):
        if(self.num_max>1):
            for i in range(2, self.num_max):
                if((self.num_max%i)==0):
                    print('{0} es multiple de {1}.'.format(self.num_max,i))
try:
    input_num= int(input('Write the number you want to check divisibles:\t'))
    my_div= Divisors(input_num)
    my_div.show_divisibles()
except Exception as ex:
    print(ex)