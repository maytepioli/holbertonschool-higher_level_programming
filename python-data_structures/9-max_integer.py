#!/usr/bin/python3
def max_integer(my_list=[]):
    numax = my_list[0]
    for i in range(1, len(my_list)):
        if numax < my_list[i]:
            numax = my_list[i]
    return numax
