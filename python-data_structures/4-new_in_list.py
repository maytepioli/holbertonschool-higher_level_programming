#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    aux_list = list(my_list)
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return aux_list
    aux_list[idx] = element
    return aux_list
