"""Python program to swap two Variables"""
var_1= input('Write the content of the first variable: ')
var_2=input('Write the content of the second variable: ')

print('We will change the variables data.')

aux= var_1
var_1 = var_2
var_2 = aux

print(aux+'  '+var_1+' '+var_2)

print('The first variable after the change is '+var_1)
print('The second var afeter changing is '+var_2)