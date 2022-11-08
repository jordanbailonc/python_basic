"""Python Program to Flatten a Nested List"""

#first array
initial_list =[[1],[2,3],[4,5,6,7]]
try:
    #result
    same_level_list = []
    #every list
    for sublist in initial_list:
        #every number in list to add
        for number in sublist:
            same_level_list.append(number)
    print(same_level_list)
except Exception as ex:
    print(ex)