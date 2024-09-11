#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nnew_list = []
    for i in my_list:
        if i % 2 == 0:
            nnew_list.append(True)
        else:
            nnew_list.append(False)
    return nnew_list
