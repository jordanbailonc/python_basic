"""Python Program to Convert Celsius To Fahrenheit """
#converter class
class Converter:
    def __init__(self,celsius):
        self.celsius=celsius
    
    def calculate_farherheit(self):
        fahrenheit= (self.celsius*9/5)+32
        print('{0} ºC in Fahrenheit are {1}º Fh.'.format(self.celsius,fahrenheit))

try:
    cel_input=float(input('Write the ºC to calculate it:\t'))
    print(str(cel_input))
    conv= Converter(cel_input)
    conv.calculate_farherheit()
except:
    print('Data input must be numeric')
