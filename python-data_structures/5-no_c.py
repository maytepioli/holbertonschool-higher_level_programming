#!/usr/bin/python3
def no_c(my_string):
    aux_str = ''
    for characters in my_string:
        if characters != 'c' and characters != 'C':
            aux_str += characters
    return aux_str
