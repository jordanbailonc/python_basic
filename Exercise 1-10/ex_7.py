"""Python Program to Generate a Random Number"""
import random

#class to generate the random number
class Generator:
    def __init__(self):
        self.num_1=random.random()

    def print_random(self):
        print('The number generated is: '+str(self.num_1*100))
        print('Round it will be: '+ str(round(self.num_1*100)))

gen=Generator()
gen.print_random()