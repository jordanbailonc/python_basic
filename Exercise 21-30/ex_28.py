"""Python Program to Find the Factors of a Number"""

class all_factors:
    def __init__(self,num) -> None:
        self.num=num

    def get_data(self):
        result =[]
        for i in range(1,self.num+1):
            if((self.num % i) ==0):
                result.append(i)
                print(i)
        return result

try:
    my_num=int(input('Write int number:\t'))
    facts=all_factors(my_num)
    ans=facts.get_data()
    if(ans.__sizeof__()>=1):
        for x in range(len(ans)):
            print(ans[x])
except Exception as e:
    print(e)
