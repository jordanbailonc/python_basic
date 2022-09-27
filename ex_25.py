"""Python Program to Find HCF or GCD"""

#class to get two numbers
class getGCD:
    def __init__(self,number,another) -> None:
        self.number=number
        self.another=another

    def calculate(self):
        gcd=0
        if self.number>self.another:
            max=self.number
        else:
            max= self.another
        for i in range (2,max):
            if(self.number % i ==0)and (self.another % i ==0):
                gcd = i
        if(gcd==0):
            print("There's no GCD for {0} and {1}".format(self.number,self.another))
        else:
            print('The GCD of the {0} and {1} is {2}'.format(self.number,self.another,gcd))

try:
    first_data= int(input('Write the first number:\t'))
    second_data = int(input('Write the second number:\t'))
    myGCD= getGCD(first_data,second_data)
    myGCD.calculate()
except:
    print('Data input must be integer.')