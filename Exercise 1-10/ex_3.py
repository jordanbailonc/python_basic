"""Python Program to Find the Square Root to a number"""
#import cmath library to make math executions
import cmath
try:
    #input information ask
    number_base= input('Write the number you want to know square root: \t')
    #in this case we use eval instead of float what should be the method used
    #for real numbers
    number_base= eval(number_base)

    number_result= cmath.sqrt(number_base)
    print('The square root of {0} is {1}.'.format(number_base,number_result))
except:
    print('input data not able to be loaded as a number')