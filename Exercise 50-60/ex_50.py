"""Python Program to Access by Index To A List"""

source= [41,65,3,84,396,74]

while (True):
    slc_index=int(input('Write the index: to check (num <0 to end program):\t'))
    if slc_index>=0:
        print(slc_index, source[slc_index])
    else:
        print('Thanks for using...')

#Another Way to Do The Same By Print All With For
"""
for index, val in enumerate(source):
    print(index, v
"""