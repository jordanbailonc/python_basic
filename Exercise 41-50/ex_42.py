"""Python Program to Illustrate Different Set Operations"""
def print_func(x,y):
    print(x)
    print(y)

A={0,3,7,2}
B={2,9,8,1}

print_func(A,B)

print('The Union of A & B is: ', A|B)
print('The Interseccion of A & B is: ', A & B)
print('The difference of A & B is: ', A - B)
print('Symetric difference of A & B is: ', A ^ B)