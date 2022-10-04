"""Python Program to Sort Words in Alphabetic Order"""

my_words=[]

try:
    num_words=int(input('Write the number of words to add:\t'))
    if(num_words>=1):
        for i in range(num_words):
            world= input('Write the {0} word to add: \t'.format(i+1))
            my_words.append(world)
    my_words.sort()
    for n_words in my_words:
        print(n_words)

except Exception as ex:
    print(ex)