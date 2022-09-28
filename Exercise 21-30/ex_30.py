"""Python Program to Shuffle Deck of Cards"""

import itertools, random

mazo = list(itertools.product(range (1,14),['Trebol','Corazon','Diamante','Picas']))

random.shuffle(mazo)

print ('Your hand is:\n')
for i in range(5):
    print('{0} de {1}'.format(mazo[i][0],mazo[i][1]))