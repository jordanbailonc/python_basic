"""Python Program to Find Sum of Natural Numbers Using Recursion"""

def natural_sum(x,y,l):
    #get the sume
    x=x+y

    #addition of the numbers
    y=y+1

    #check to print the max
    if(x<=l):
        print(x)

    #check if 1 more calculation si needed
    if(x<l):
        natural_sum(x,y,l)

# ask the user the max value to get and it prints data
try:
    max_num=int(input('Write the max number:\t'))
    natural_sum(0,0,max_num)

#in case of error it informs to user
except:
    print('An error ocurrs during the execution.')