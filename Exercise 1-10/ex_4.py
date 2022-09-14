"""This program calculate the area of a triangle by user inputs"""
from email.mime import base

#definition of a class Triangle
class Triangle:
    #constructor
    def __init__(self,site1,site2,site3):
        self.site1=int(site1)
        self.site2=int(site2)
        self.site3=int(site3)

    #funtion to calculate perimeter and area
    def calculate_area(self):
        perimeter=float((self.site1+self.site2+self.site3)/2)
        print('The perimeter of a triangle with {0}, {1}, {2} is : {3} cm.'.format(self.site1,self.site2,self.site3, perimeter))
        area= ((perimeter*(perimeter-self.site1)*(perimeter-self.site2)*(perimeter-self.site3))**0.5)
        print('The area of a trinagle with this data will be:\n base {0}\n helth {1}\n weith {2}\n area {3}'.format(self.site1,self.site2,self.site3,area))

try:
    a=float(input('Write the base:\t'))
    b= float(input('Write the site b:\t'))
    c= float(input('Write the site c:\t'))
    t1= Triangle(a,b,c)
    t1.calculate_area()
except:
    print('All data input must be numeric')