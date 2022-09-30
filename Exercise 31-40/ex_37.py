"""Python Program to Transpose a Matrix"""
#instance matrix
a=[[2,1],[5,2],[3,5]]

#method called changing indexes
res=[[a[i][j] for i in range(len(a))]for j in range(len(a[0]))]

#show results
for num1 in res:
    print(num1)