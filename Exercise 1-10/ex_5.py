"""Python program to solve Quadratic Equation"""

#import ctmath library to solve math problems
import cmath
try:
    num_a = float(input('Enter a: '))  
    num_b = float(input('Enter b: '))  
    num_c = float(input('Enter c: '))  
    
    # calculate the discriminant  
    d = (num_b**2) - (4*num_a*num_c)  
    
    # find two solutions  
    sol1 = (- num_b-cmath.sqrt(d))/(2*num_a)  
    sol2 = (- num_b+cmath.sqrt(d))/(2*num_a)  
    print('The solution are {0} and {1}'.format(sol1,sol2))   
except:
    print('Real numbers needed')