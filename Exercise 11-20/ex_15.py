"""Python Program to Print all Prime Numbers in an Interval"""

class writter:
    def __init__(self,start_num,end_num) -> None:
        self.start_num= start_num
        self.end_num= end_num

    def to_print(self):
        print('The prime numbers between {0} and {1} are : \t '.format(self.start_num,self.end_num))
        for numbers in range(self.start_num, self.end_num+1):
            #check range is bigger than 1
            if (numbers >1):
                #load range
                for i in range (2,numbers):
                    #if is not prime break and keeps checking
                    if(numbers % i) ==0:
                        break
                #if it's prime write content
                else:
                    print(str(numbers))
    
try:
    num_a= int(input('Write the first number: \t'))
    num_b= int(input('Write the last number: \t'))
    if(num_a>num_b):
        print('We change the order of number to make it work')
        my_writter= writter(num_b,num_a)
        my_writter.to_print()
    else:
        my_writter=writter(num_a,num_b)
        my_writter.to_print()
except:
    print('Only number accepted on this program.')