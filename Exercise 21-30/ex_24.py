"""Python Program to Convert Decimal to Binary, Octal and Hexadecimal"""

class Convertex:
    def __init__(self,number) -> None:
        self.number=number

    def dec_octal(self):
        print((oct(self.number)),' in octal')

    def dec_hex(self):
        print(hex(self.number),' in hexadecimal')

    def dec_bin(self):
        print(str(bin(self.number)),' in binary')

try:
    num_input= int(input('Write the number to convert:\t'))
    c =Convertex(num_input)
    c.dec_bin()
    c.dec_octal()
    c.dec_hex()
except:
    print('Write the data ')