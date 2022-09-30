"""Python Program to Add Two Matrices"""


#matrix definition
a=[[5 , 4 , 0],[4 , 6 , 8]]

b=[[6 , 2 , 5],[3 , 8 , 2]]

#intance of the result variable
ans = [[0,0,0],[0,0,0]]

#load of all data matrice 1
for i in range(len(a)):
    # load of all data matrice 2
    for elem in range(len(a[0])):
        #addition by indexes
        ans[i][elem]= a[i][elem]+b[i][elem]

#show result
for num in ans:
    print(num)

