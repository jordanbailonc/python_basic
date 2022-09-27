"""Python Program to Find LCM"""

class LCM_Calc:
    def __init__(self,num_1,num_2) -> None:
        self.num_1=num_1
        self.num_2=num_2
    
    def get_LCM(self):
        first_lcm=self.num_1*self.num_2
        for i in range (2,first_lcm+1):
            if((i%self.num_1)==0) and ((i%self.num_2)==0):
                result=i
                break
            else:
                result=first_lcm
        print('The LCM of the {0} and {1} is: {2}.'.format(self.num_1,self.num_2,result))

try:
    first=int(input('Write the fisrt number:\t'))
    second= int(input('Write the second number:\t'))
    myLCM=LCM_Calc(first,second)
    myLCM.get_LCM()
except Exception as e:
    print(e)