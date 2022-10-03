"""Python Program to Remove Punctuations From a String"""

import string

sata= input('Write the content to fill: \t')

sata_tre = sata.translate(str.maketrans('','',string.punctuation))

print(sata_tre)