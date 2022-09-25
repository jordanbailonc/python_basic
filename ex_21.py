"""Python Program to Find the Sum of Natural Numbers"""
class nat_calculator:
    def __init__(self,last_num) -> None:
        self.last_num=last_num

    def get_sumatory(self):
        sumatory=0
        if(self.last_num>0):
            for i in range(1,self.last_num):
                sumatory=sumatory+i
            print('{0} is sume of all naturall number from 0 to {1}'.format(sumatory,self.last_num))
        else:
            print('The number must be bigger than 0')
try:
    num_user=int(input('Write the number you want to be the max to get the sume:\t'))
    my_nat_cal=nat_calculator(num_user)
    my_nat_cal.get_sumatory()
except:
    print('Your input must be an integer number to make it work.')