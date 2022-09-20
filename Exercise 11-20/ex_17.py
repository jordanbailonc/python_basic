"""Python Program to Display the multiplication Table"""

class Multipliyer:
    def __init__(self,num_table) -> None:
        self.num_table=num_table

    def print_table(self):
        for i in range(0,11):
            print('{0} * {1} = {2}'.format(self.num_table,i,(self.num_table*i)))

try:
    num_input=float(input('Write the number to show the multiplication table:\t'))
    my_multipliyer= Multipliyer(num_input)
    my_multipliyer.print_table()
except:
    print('Data input must be numeric.')