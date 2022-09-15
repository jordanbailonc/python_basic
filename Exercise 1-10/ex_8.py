"""Python Porgram to Convert Km to Miles"""

#converter class
class Converter:
    def __init__(self,distance):
        self.distance=distance
    
    def calculate_miles(self):
        miles= self.distance*0.621371
        print('{0} km in miles are {1} ml.'.format(self.distance,miles))

try:
    input_data=float(input('Write the km to convert:\t'))
    conv=Converter(input_data)
    conv.calculate_miles()
except:
    print('Only numeric content able')