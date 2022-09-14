#This prorgram add two numbers input by the user
try:
    num1=input('Write the first number: \t')
    num2=input('Write the second number: \t')
    num1=float(num1)
    num2=float(num2)
    #print("The final addion of "+str(num1)+" + "+str(num2)+" = "+str(num1+num2))
    print('The addition of {0} + {1} = {2}'.format(num1,num2,(num1+num2)))
except:
    print("Data input must be numeric")