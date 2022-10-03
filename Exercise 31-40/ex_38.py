"""Python Program to Multiply Two Matrices"""


A =[[4,5,8],[3,2,8]]

B= [[5,3],[9,1]]

my_result= [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] 
    for A_row in A]

for i in my_result:
    print(i)