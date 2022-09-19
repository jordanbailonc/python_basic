"""Python Program to Find the Largest Among Three Numbers """
class test_largest:
    def __init__(self,num_a,num_b,num_c):
        self.num_a=num_a
        self.num_b=num_b
        self.num_c=num_c
    
    def check_max_num(self):
        if(self.num_a > self.num_b) and(self.num_a>self.num_b):
            return self.num_a
        elif (self.num_b >= self.num_a) and (self.num_b >= self.num_c):
            return self.num_b
        else:
            return self.num_c

try:

    num1= float(input('Write the 1st number:\t'))
    num2= float(input('Write the 2nd number:\t'))
    num3= float(input('Write the 3th number:\t'))

    my_tester=test_largest(num1,num2,num3)
    print('The largest one from the input numbers is: {0}'.format(my_tester.check_max_num()))
except:
    print('The program only works with numbers')