"""Python Program to Print the Fibonacci sequence"""

class Fibonacci:
    def execute_fibonacci():
        aux=0
        aux2=1
        for i in range(1,10):
            print(aux)
            result=aux+aux2
            aux=aux2
            aux2=result
        
print('Executing Fibonacci sequence:\t')
my_fibo= Fibonacci
my_fibo.execute_fibonacci()