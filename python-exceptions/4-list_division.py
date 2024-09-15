#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = ""
    try:
        for i in my_list_1:
            if isinstance(i, int):
                list_a += my_list_1[i]
                for j in my_list_2:
                    if isinstance(j, int):
                        list_b += my_list_2[j]
                        new_list = my_list_1 / my_list_2
            
            