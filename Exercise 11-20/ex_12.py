"""Python Program to Check Leap Year """

class Leap_year_tester:
    def __init__(self,year):
        self.year=year

    def test_input_year(self):
        result=self.year%4
        if(result!=0):
            print('{0} is not a leap year.'.format(self.year))
        else:
            print('{0} is a leap year wiht a total of 366 days.'.format(self.year))

try:
    number_year=int(input('Write the year to check: \t'))
    my_checker=Leap_year_tester(number_year)
    my_checker.test_input_year()
except:
    print('Usage of the program needs numbers.')