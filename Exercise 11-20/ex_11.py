"""Python Program to Check if a Number is Odd or Even """

class Classifier:
    def __init__(self,intro_num):
        self.intro_num=intro_num

    def getClassification(self):
        index_num= self.intro_num%2
        if(index_num==0):
            print('The number {0} is odd'.format(index_num))
        else:
            print('The number {0} is even'.format(index_num))

try:
    input_num =float(input('Write the number input:\t'))
    my_classi= Classifier(input_num)
    my_classi.getClassification()
except:
    print('Content must be numeric')